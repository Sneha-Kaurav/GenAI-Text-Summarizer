import requests
from bs4 import BeautifulSoup
import re

def fetch_text_from_url(url):
    """
    Fetches and cleans main content from a URL.
    Returns plain text or None on error.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Could not retrieve URL: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')

    for tag in soup(['script', 'style', 'header', 'footer', 'nav', 'aside']):
        tag.decompose()

    text = soup.get_text(separator=' ', strip=True)
    text = re.sub(r'\s+', ' ', text).strip()

    if len(text) > 3000:  # distilBART safe limit
        text = text[:3000]

    return text
