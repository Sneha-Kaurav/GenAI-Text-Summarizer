import torch
import gradio as gr
import textwrap
from transformers import pipeline
import nltk
from newspaper import Article
from url_input import fetch_text_from_url


nltk.download('punkt')
nltk.download('punkt_tab')

from nltk.tokenize import sent_tokenize

## Summarizer pipeline

model_path = ("Models/models--sshleifer--distilbart-cnn-12-6/snapshots"
              "/a4f8f3ea906ed274767e9906dbaede7531d660ff")

summarizer = pipeline("summarization", model=model_path, torch_dtype=torch.bfloat16)


## function to enter as input in gradio
def summarizer_text(text, summary_type):
    max_chunk_length = 1000

    # Detect if the input is a URL
    if text.strip().lower().startswith("http"):
        fetched = fetch_text_from_url(text.strip())
        if not fetched:
            return "Could not fetch or process the URL content."
        text = fetched

    chunks = textwrap.wrap(text, max_chunk_length)

    summaries = []
    for chunk in chunks:
        result = summarizer(chunk,
                            max_length=300,
                            min_length=50,
                            do_sample=False,
                            truncation=True)[0]['summary_text']
        summaries.append(result)

    combined_summary = " ".join(summaries)

    # Optional: only re-summarize if input was long
    if len(summaries) > 1:
        combined_summary = summarizer(combined_summary,
                                      max_length= 400,
                                      min_length=50,
                                      do_sample=False)[0]['summary_text']

    if summary_type == "Bullet Points":
        bullet_lines = sent_tokenize(combined_summary)
        bullet_summary = "\n• " + "\n• ".join(bullet_lines)
        return bullet_summary

    return combined_summary

# UI using gradio
sum_text = gr.Interface(
    fn=summarizer_text,
    inputs=[
        gr.Textbox(lines=12, label="Input Text", placeholder="Paste your text or URL(full address) here..."),
        gr.Radio(["Narrative", "Bullet Points"], label="Summary Type")
    ],
    outputs=gr.Textbox(lines=10, label="Summarized Output"),
    title= "Text Summarizer",
    description= "Paste a long text or an article URL. Choose summary type: narrative or bullet points."
)

sum_text.launch()

