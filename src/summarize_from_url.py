import requests
from bs4 import BeautifulSoup
from summarizer_utils import summarize_text

def extract_text_from_url(url: str) -> str:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception as e:
        raise RuntimeError(f"Failed to fetch the article: {e}")
    
    soup = BeautifulSoup(response.text, 'html.parser')
    paragraphs = soup.find_all('p')
    
    if not paragraphs:
        raise ValueError("No readable content found in the article.")

    text = ' '.join(p.get_text().strip() for p in paragraphs if len(p.get_text().strip()) > 40)
    return text

if __name__ == "__main__":
    url = "https://edition.cnn.com/2025/07/02/business/trump-japan-trade-deal-intl-hnk"

    try:
        article_text = extract_text_from_url(url)
        print("\nSummary:\n")
        print(summarize_text(article_text))
    except Exception as e:
        print(f"Error: {e}")
