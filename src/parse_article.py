from summarizer_utils import summarize_text


def handle_parsed_article(article_text):
    summary = summarize_text(article_text)
    print(summary)
