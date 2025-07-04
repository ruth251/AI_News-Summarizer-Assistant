from summarizer_utils import summarize_text
from qa_utils import answer_query
from summarize_from_url import extract_text_from_url
#from database import save_summary, save_question

def handle_article(text: str, question: str = None) -> dict:
    summary = summarize_text(text)
    

    answer = None
    if question:
        answer = answer_query(summary, question)
       

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

    summary = summarize_text(article_text)
    

    answer = None
    if question:
        answer = answer_query(summary, question)
        

    return {
        "summary": summary,
        "question": question,
        "answer": answer
    }

def answer_user_question(summary: str, question: str) -> str:
    return answer_query(summary, question)
