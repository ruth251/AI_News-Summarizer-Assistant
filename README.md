# 📰 AI News Summarizer Assistant

An AI-powered assistant that summarizes news articles from user-provided URLs or plain text using Natural Language Processing (NLP) with spaCy. The system extracts key points from content and answers user questions about the summary.

---

## 📌 Features

- ✅ Accepts input via **URL** or **raw text**
- ✂️ Extracts clean article content using **BeautifulSoup**
- 🧠 Summarizes key sentences using **spaCy**
- 💬 Answers user questions based on the summary
- 🧪 Fully tested with `pytest`

---

## 🛠️ Tech Stack

- **Python 3.11**
- [spaCy](https://spacy.io) for NLP
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for HTML parsing
- `pytest` for unit testing
- Flask (optional integration for UI - future work)

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/ruth251/AI_News-Summarizer-Assistant.git
cd AI_News-Summarizer-Assistant

2. Create a Virtual Environment
    python -m venv venv
    source venv/bin/activate   On Windows: venv\Scripts\activate

3. Install Dependencies
    pip install -r requirements.txt

4. Run the Application
    python app.py
