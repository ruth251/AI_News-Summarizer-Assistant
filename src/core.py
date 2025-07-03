from summarizer_utils import summarize_text
from qa_utils import answer_query
from summarizer_from_url import extract_text_from_url


def handle_article(text: str, question: str = None) -> dict:
    
    summary = summarize_text(text)
    answer = answer_query(summary, question) if question else None
    return {
        "summary": summary,
        "question": question,
        "answer": answer
    }


def handle_link(url: str, question: str = None) -> dict:

    try:
        article_text = extract_text_from_url(url)
    except Exception as e:
        return {"error": str(e)}

    return handle_article(article_text, question)


def answer_user_question(summary: str, question: str) -> str:
    return answer_query(summary, question)
