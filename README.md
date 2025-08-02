# Text & URL Summarizer App

An intelligent NLP-based web app that summarizes long texts or online articles using Hugging Face's `distilBART` transformer model. Built with Gradio for an intuitive interface and deployed-ready for Hugging Face Spaces or local use.

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
```bash
1. **Clone the repository**

git clone https://github.com/your-username/text-url-summarizer.git
cd text-url-summarizer

2. ***Create a virtual environment***

python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate

3. ***Install dependencies***

pip install -r requirements.txt

4. ***Run the app***

python app.py

## Deploy on Hugging Face Spaces

This app is compatible with Hugging Face Spaces. To deploy:
<ol>
<li>Create a new Gradio Space</li>

<li>Upload:</li>
<ul>
<li>app.py</li>

<li>url_input.py</li>

<li>requirements.txt</li>

<li>(Optional) README.md</li>
</ul>
<li>Click "Create Space".<li>
</ol> 



python app.py

5. Open your browser and go to http://localhost:7860 to use the app.
