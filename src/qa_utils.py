from transformers import pipeline

# Load the QA pipeline (DistilBERT fine-tuned on SQuAD)
qa_pipeline = pipeline("question-answering", model="distilbert-base-uncased-distilled-squad")

def answer_query(summary: str, question: str) -> str:
    if len(summary.strip()) == 0:
        return "No summary available to answer from."

    result = qa_pipeline(question=question, context=summary)
    return result['answer']
