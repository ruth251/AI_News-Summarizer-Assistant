from transformers import pipeline

try:
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
except Exception as e:
    raise RuntimeError(f"Failed to load BART summarizer: {e}")



def summarize_text(text: str, max_tokens: int = 130) -> str:
    if len(text.split()) < 50:
        return "Text too short to summarize."
    
    # Truncate long input (BART supports max ~1024 tokens)
    text = ' '.join(text.split()[:1024])
    
    summary = summarizer(
        text,
        max_length=max_tokens, 
        min_length=30, 
        do_sample=False)
    
    return summary[0]['summary_text']
