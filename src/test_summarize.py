import pytest
from unittest.mock import patch
from core import handle_article,handle_link, answer_user_question
from parse_article import handle_parsed_article

# Helper to run with mocks
@patch("core.answer_query")
@patch("core.summarize_text")
def test_normal_case(mock_summarize, mock_answer):
    mock_summarize.return_value = "Mock summary"
    mock_answer.return_value = "Relevant answer"
    result = handle_article("This is a valid article.", "What is it about?")
    assert result["summary"] == "Mock summary"
    assert result["answer"] == "Relevant answer"
    assert result["question"] == "What is it about?"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_no_question_provided(mock_summarize, mock_answer):
    mock_summarize.return_value = "Mock summary"
    result = handle_article("This is a valid article.")
    assert result["summary"] == "Mock summary"
    assert result["answer"] is None

@patch("core.answer_query")
@patch("core.summarize_text")
def test_empty_article_text(mock_summarize, mock_answer):
    mock_summarize.return_value = ""
    mock_answer.return_value = None
    result = handle_article("", "What's it about?")
    assert result["summary"] == ""
    assert result["answer"] is None or result["answer"] == ""

@patch("core.answer_query")
@patch("core.summarize_text")
def test_very_short_article(mock_summarize, mock_answer):
    mock_summarize.return_value = "Short summary"
    mock_answer.return_value = "Short answer"
    result = handle_article("Dogs bark.", "What do dogs do?")
    assert result["summary"] == "Short summary"
    assert result["answer"] == "Short answer"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_irrelevant_question(mock_summarize, mock_answer):
    mock_summarize.return_value = "Article about cats"
    mock_answer.return_value = "I don't know"
    result = handle_article("Cats are independent animals.", "What is the stock price of Tesla?")
    assert result["answer"] == "I don't know"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_complex_ambiguous_content(mock_summarize, mock_answer):
    mock_summarize.return_value = "Complex summary"
    mock_answer.return_value = "Partial answer"
    article = "Quantum computing and healthcare trends intersect in ambiguous ways."
    result = handle_article(article, "How are they connected?")
    assert result["answer"] == "Partial answer"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_ambiguous_question(mock_summarize, mock_answer):
    mock_summarize.return_value = "Summary"
    mock_answer.return_value = "Can you clarify your question?"
    result = handle_article("A news article about many topics.", "What about it?")
    assert "clarify" in result["answer"].lower()

@pytest.mark.parametrize("bad_input", [None, 123, [], {}, 5.5])
def test_non_string_inputs(bad_input):
    with pytest.raises(Exception):
        handle_article(bad_input, "Valid question")

@patch("core.answer_query")
@patch("core.summarize_text")
def test_very_long_article(mock_summarize, mock_answer):
    mock_summarize.return_value = "Condensed summary"
    mock_answer.return_value = "Detailed answer"
    article = "Lorem ipsum " * 5000
    result = handle_article(article, "What is this?")
    assert result["summary"] == "Condensed summary"
    assert result["answer"] == "Detailed answer"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_special_characters(mock_summarize, mock_answer):
    mock_summarize.return_value = "Cleaned summary"
    mock_answer.return_value = "Handled special content"
    article = "<p>Hello 🌍! &copy;</p>"
    result = handle_article(article, "What's in it?")
    assert "summary" in result
    assert "answer" in result

@patch("core.answer_query")
@patch("core.summarize_text")
def test_multilingual_text(mock_summarize, mock_answer):
    mock_summarize.return_value = "Résumé du texte"
    mock_answer.return_value = "Je ne sais pas"
    article = "Ceci est un texte en français."
    result = handle_article(article, "Quel est le sujet ?")
    assert "Résumé" in result["summary"] or "texte" in result["summary"]
    assert result["answer"] == "Je ne sais pas"

@patch("core.answer_query")
@patch("core.summarize_text")
def test_empty_question_string(mock_summarize, mock_answer):
    mock_summarize.return_value = "Mock summary"
    result = handle_article("Some article text.", question="")
    assert result["summary"] == "Mock summary"
    assert result["answer"] is None

@patch("core.answer_query", side_effect=Exception("QA model crashed"))
@patch("core.summarize_text", return_value="Some summary")
def test_model_failure(mock_summarize, mock_answer):
    with pytest.raises(Exception) as e:
        handle_article("Some text", "Why?")
    assert "QA model crashed" in str(e.value)

@patch("core.answer_query", return_value="answer")
@patch("core.summarize_text", side_effect=MemoryError("Out of memory"))
def test_timeout_or_memory_error(mock_summarize, mock_answer):
    with pytest.raises(MemoryError):
        handle_article("a" * 10_000_000, "Summarize")

# 1. Normal Case — Valid URL and Relevant Question
@patch("core.answer_query", return_value="Mock answer")
@patch("core.summarize_text", return_value="Mock summary")
@patch("core.extract_text_from_url", return_value="Article content")
def test_handle_link_normal(mock_extract, mock_summary, mock_answer):
    result = handle_link("https://valid.com/article", "What happened?")
    assert result["summary"] == "Mock summary"
    assert result["answer"] == "Mock answer"

# 2. No Question Provided
@patch("core.summarize_text", return_value="Mock summary")
@patch("core.extract_text_from_url", return_value="Some article")
def test_handle_link_no_question(mock_extract, mock_summary):
    result = handle_link("https://valid.com/article")
    assert result["summary"] == "Mock summary"
    assert result["answer"] is None

# 3. Invalid or Broken URL
@patch("core.extract_text_from_url", side_effect=Exception("404 Not Found"))
def test_handle_link_invalid_url(mock_extract):
    result = handle_link("https://invalid-url.com", "What?")
    assert "error" in result
    assert "404" in result["error"]


# 4. Non-Article URL
@patch("core.extract_text_from_url", side_effect=Exception("no article found"))
def test_handle_link_non_article_url(mock_extract):
    result = handle_link("https://homepage.com")
    assert "error" in result
    assert "no article" in result["error"]


# 5. URL Timeout / Connection Error
@patch("core.extract_text_from_url", side_effect=Exception("Connection timed out"))
def test_handle_link_timeout(mock_extract):
    result = handle_link("https://slow-website.com")
    assert "error" in result
    assert "timed out" in result["error"]


# 6. URL Points to Very Long Article
@patch("core.extract_text_from_url", return_value="Long " * 10_000)
@patch("core.summarize_text", return_value="Concise summary")
@patch("core.answer_query", return_value="Accurate answer")
def test_handle_link_long_article(mock_extract, mock_summary, mock_answer):
    result = handle_link("https://long.com", "What is it about?")
    assert result["summary"] == "Concise summary"
    assert result["answer"] == "Accurate answer"


# 7. Article is Not in English
@patch("core.extract_text_from_url", return_value="Ceci est un texte.")
@patch("core.summarize_text", return_value="Résumé du texte")
@patch("core.answer_query", return_value="Je ne sais pas")
def test_handle_link_non_english(mock_extract, mock_summary, mock_answer):
    result = handle_link("https://frenchsite.fr", "De quoi s'agit-il ?")
    assert "Résumé" in result["summary"] or "texte" in result["summary"]
    assert result["answer"] == "Je ne sais pas"


# 8. Question is Unrelated to Article
@patch("core.extract_text_from_url", return_value="This is about cats.")
@patch("core.summarize_text", return_value="Summary about cats")
@patch("core.answer_query", return_value="I don't know")
def test_handle_link_irrelevant_question(mock_extract, mock_summary, mock_answer):
    result = handle_link("https://cats.com", "What's Tesla's stock price?")
    assert result["answer"] == "I don't know"


# 9. Empty URL String
def test_handle_link_empty_url():
    result = handle_link("")
    assert "error" in result


# 10. Non-String URL or Question
@pytest.mark.parametrize("bad_url", [None, 123, 5.5, [], {}])
def test_handle_link_non_string_inputs(bad_url):
    with pytest.raises(Exception):
        handle_link(bad_url, "Some question")


# 11. Question is Empty String
@patch("core.extract_text_from_url", return_value="Some article")
@patch("core.summarize_text", return_value="Mock summary")
def test_handle_link_empty_question(mock_extract, mock_summary):
    result = handle_link("https://site.com", "")
    assert result["summary"] == "Mock summary"
    assert result["answer"] is None


# 12. Duplicate or Cached URL (simulated by repeated calls)
@patch("core.extract_text_from_url", return_value="Article")
@patch("core.summarize_text", return_value="Summary")
@patch("core.answer_query", return_value="Answer")
def test_handle_link_cached_url(mock_extract, mock_summary, mock_answer):
    url = "https://repeated.com"
    result1 = handle_link(url, "Question?")
    result2 = handle_link(url, "Question?")
    assert result1 == result2

# 12. Duplicate or Cached URL (simulated by repeated calls)
@patch("core.extract_text_from_url", return_value="Article")
@patch("core.summarize_text", return_value="Summary")
@patch("core.answer_query", return_value="Answer")
def test_handle_link_cached_url(mock_extract, mock_summary, mock_answer):
    url = "https://repeated.com"
    result1 = handle_link(url, "Question?")
    result2 = handle_link(url, "Question?")
    assert result1 == result2


# 13. Article With HTML Tags / Ads / Garbage Text
@patch("core.extract_text_from_url", return_value="<html><body>Article 📰 with ads & junk</body></html>")
@patch("core.summarize_text", return_value="Clean summary")
@patch("core.answer_query", return_value="Clean answer")
def test_handle_link_dirty_article(mock_extract, mock_summary, mock_answer):
    result = handle_link("https://messy.com", "What is it?")
    assert result["summary"] == "Clean summary"
    assert result["answer"] == "Clean answer"
# 14. Error in extract_text_from_url()
@patch("core.extract_text_from_url", side_effect=Exception("Extraction failed"))
def test_handle_link_extractor_failure(mock_extract):
    result = handle_link("https://fails.com", "Why?")
    assert "error" in result
    assert "Extraction" in result["error"]


# 15. Error in handle_article (summarization or QA failure)
@patch("core.extract_text_from_url", return_value="Some article")
@patch("core.summarize_text", side_effect=Exception("Summarizer crashed"))
def test_handle_link_internal_failure(mock_extract, mock_summary):
    with pytest.raises(Exception) as e:
        handle_link("https://boom.com", "What happened?")
    assert "crashed" in str(e.value)






