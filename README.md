# Text & URL Summarizer App

An intelligent NLP-based web app that summarizes long texts or online articles using Hugging Face's `distilBART` transformer model. Built with Gradio for an intuitive interface and deployed-ready for Hugging Face Spaces or local use.

<b> Try the Live App on Hugging Face Spaces: </b> 
---

## Project Overview

This project allows users to:
- Paste long paragraphs or documents for instant summarization
- Input article URLs — the app fetches and cleans the content automatically
- Choose between **narrative** or **bullet-point** summary formats

Ideal for readers, researchers, students, or professionals who need quick, readable summaries of verbose content.

---

## ✨ Key Features

- Supports **raw text** *and* **web article URLs**
- Uses `sshleifer/distilbart-cnn-12-6` summarization model from Hugging Face
- Built with **Gradio** for a clean, fast, interactive interface
- Cleans and pre-processes messy web data using **BeautifulSoup**
- Bullet-point summaries with **NLTK sentence tokenization**

---

## 🛠 Tech Stack

| Tool         | Description |
|--------------|-------------|
| `transformers` | Load Hugging Face summarization model |
| `Gradio`     | Interactive front-end interface |
| `BeautifulSoup` | Scrape and clean article text from URLs |
| `NLTK`       | Sentence tokenization (for bullet summaries) |
| `textwrap`   | Handles text chunking for long inputs |
| `Torch`      | Backend model support (auto CPU/GPU selection) |

---

## 📦 Setup Instructions

### 🔧 Local Installation

1. **Clone the repository**

 git clone https://github.com/Sneha-Kaurav/GenAI-Text-Summarizer.git
cd text-url-summarizer

2. **Create a virtual environment**

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3. **Install dependencies**

pip install -r requirements.txt

4. **Run the app**

python app.py

5. Open your browser and go to http://localhost:7860 to use the app.
   
---

## Deploy on Hugging Face Spaces

This app is compatible with Hugging Face Spaces. To deploy:
1.Create a new Gradio Space

2.Upload:
<ul>
<li>app.py</li>

<li>url_input.py</li>

<li>requirements.txt</li>

<li>(Optional) README.md</li>
</ul>
3.Click "Create Space".

---

## Screenshots

---

## Author
<b> Sneha Kaurav </b><br>
    AI Graduate, 2025 | Passionate about practical NLP and real-world ML applications
    🔗 LinkedIn
    🤗 Hugging Face

---

## Future Improvements
<ul>
<li> Better boilerplate removal from websites (readability, lxml)</li>

<li> Save/export summaries (copy/download)</li>

<li> Multilingual support and detection</li>
</ul>
