from transformers import pipeline

# Load the QA pipeline (DistilBERT fine-tuned on SQuAD)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_query(summary: str, question: str) -> str:
    if not isinstance(summary, str):
        raise TypeError("Summary must be a string.")
    if not isinstance(question, str):
        raise TypeError("Question must be a string.")

    if not summary.strip():
        return "No summary available to answer from."
    if not question.strip():
        return "No question provided."

    result = qa_pipeline(question=question, context=summary)
    return result['answer']

