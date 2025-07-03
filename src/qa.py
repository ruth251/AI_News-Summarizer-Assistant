from transformers import pipeline

# Load question-answering model
qa_pipeline = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

def answer_question(summary: str, question: str) -> str:
    if not summary.strip():
        return "Summary is empty. Cannot answer the question."
    
    result = qa_pipeline(question=question, context=summary)
    return result["answer"]
