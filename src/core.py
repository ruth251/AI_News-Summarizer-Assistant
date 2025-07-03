from summarizer_utils import summarize_text
from qa_utils import answer_query
from summarize_from_url import extract_text_from_url


def handle_article(text: str, question: str = None) -> dict:
    
    summary = summarize_text(text)
    answer = answer_query(summary, question) if question else None
    return {
        "summary": summary,
        "question": question,
        "answer": answer
    }


def handle_link(url: str, question: str = None) -> dict:
    # Validate input types
    if not isinstance(url, str):
        raise TypeError("URL must be a string")
    if question is not None and not isinstance(question, str):
        raise TypeError("Question must be a string or None")

    try:
        article_text = extract_text_from_url(url)
    except Exception as e:
        return {"error": str(e)}

    return handle_article(article_text, question)



def answer_user_question(summary: str, question: str) -> str:
    return answer_query(summary, question)
