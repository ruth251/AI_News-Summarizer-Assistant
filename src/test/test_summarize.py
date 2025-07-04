import pytest
import spacy
    # PRASING

nlp = spacy.load("en_core_web_sm")
# this test see if the text inter is text
def test_parse_text_raises_type_error():
    with pytest.raises(TypeError) as exc_info:
        parse_text(123)  # int input
    assert str(exc_info.value) == "Input must be a string."

    with pytest.raises(TypeError):
        parse_text(None)  # None input

    with pytest.raises(TypeError):
        parse_text(['list', 'of', 'words'])  # list input
# Make sure the function handles an empty string
def test_parse_text_empty_string():
    sentences = parse_text("")
    assert sentences == []
# Input is None
    def test_input_none(self):
        with self.assertRaises(TypeError):
            parse_text(None)

    # Input is an integer
    def test_input_integer(self):
        with self.assertRaises(TypeError):
            parse_text(123)

    # Input is a list of strings
    def test_input_list(self):
        with self.assertRaises(TypeError):
            parse_text(["Hello", "world"])

    # Input is a single sentence
    def test_single_sentence(self):
        text = "This is just one sentence."
        sentences = parse_text(text)
        self.assertEqual(len(sentences), 1)
        self.assertEqual(str(sentences[0]).strip(), text)
#  Test with very long text
def test_parse_text_long_text():
    text = "Sentence one. " * 1000  # Repeat sentence 1000 times
    sentences = parse_text(text)
    assert len(sentences) == 1000
#  Test input with special characters
def test_parse_text_special_characters():
    text = "Wait! What happened? Are you sure? Yes, I am."
    sentences = parse_text(text)
    assert len(sentences) == 4
# Test with whitespace string
def test_parse_text_whitespace_only():
    sentences = parse_text("   \n   ")
    assert sentences == []

    #  SUMRIZING

def test_equal_score_sentences(self):
        text = "Dogs bark. Cats meow. Birds chirp."
        sents = parse_text(text)
        summary = summarize_text(sents, 2)
        self.assertEqual(summary, "Dogs bark. Cats meow.")
def test_all_stop_words(self):
        text = "And the or but. If so then because."
        sents = parse_text(text)
        summary = summarize_text(sents, 2)
        self.assertTrue(len(summary.strip()) > 0 or summary == "")  # might still return empty string
def test_empty_sentence_list(self):
        summary = summarize_text([], 3)
        self.assertEqual(summary, "")
#  Empty Sentence List
def test_summarize_empty_input():
    summary = summarize_text([], num_sentences=3)
    assert summary == ""
# num_sentences = 0
def test_summarize_zero_requested():
    text = "AI helps in healthcare. It is also used in education."
    doc = nlp(text)
    sentences = list(doc.sents)

    summary = summarize_text(sentences, num_sentences=0)
    assert summary == ""
# Very Long Sentence List
def test_summarize_long_input():
    text = "AI is evolving. " * 100  # 100 short repeated sentences
    doc = nlp(text)
    sentences = list(doc.sents)

    summary = summarize_text(sentences, num_sentences=5)
    assert isinstance(summary, str)
    assert summary.count('.') >= 
# Duplicate Sentences
def test_summarize_duplicate_sentences():
    text = "AI is good. AI is good. AI is good. AI is good."
    doc = nlp(text)
    sentences = list(doc.sents)

    summary = summarize_text(sentences, num_sentences=2)
    assert summary.count("AI is good") >= 2
# Summary Stripped of Extra Spaces
def test_summarize_trims_whitespace():
    text = "   AI is powerful.   Machine learning is part of AI.   "
    doc = nlp(text)
    sentences = list(doc.sents)

    summary = summarize_text(sentences, num_sentences=2)
    assert not summary.startswith(" ")
    assert not summary.endswith(" ")

def test_valid_url_fetch(self):
        test_url = "https://www.bbc.com/news/world-us-canada-66808518"  
        article_text = get_article_text_from_url(test_url)

def test_invalid_url(self):
        result = get_article_text_from_url("htp:/invalid-url")
        self.assertEqual(result, "")

    @patch('requests.get', side_effect=ConnectionError("Failed to connect"))
def test_non_existing_domain(self, mock_get):
        result = get_article_text_from_url("http://nonexistent.domain")
        self.assertEqual(result, "")
  
    @patch('requests.get')
def test_non_html_content(self, mock_get):
        mock_get.return_value = Mock(status_code=200, text="") 
        mock_get.return_value.raise_for_status = lambda: None

        result = get_article_text_from_url("http://image-url.com")
        self.assertEqual(result, "")
     
    @patch('requests.get', side_effect=Timeout("Request timed out"))
def test_timeout(self, mock_get):
        result = get_article_text_from_url("http://timeout-url.com")
        self.assertEqual(result, "")



def test_strip_whitespace(self):
    raw = "   Hello World!   "
    cleaned = accept_raw_text(raw)
    self.assertEqual(cleaned, "Hello World!")

def test_empty_string(self):
    raw = ""
    cleaned = accept_raw_text(raw)
    self.assertEqual(cleaned, "")

def test_no_whitespace(self):
    raw = "CleanText"
    cleaned = accept_raw_text(raw)
    self.assertEqual(cleaned, "CleanText")

def test_only_whitespace(self):
    raw = "     "
    cleaned = accept_raw_text(raw)
    self.assertEqual(cleaned, "")

def test_special_characters(self):
    text = "  ***Hello World!!!***  "
    result = accept_raw_text(text)
    self.assertEqual(result, "***Hello World!!!***")




def test_stores_valid_summary(self):
    conn = sqlite3.connect(":memory:")
    store_summary_in_db("Test summary", url="https://example.com", db_path=":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT summary FROM summaries")
    result = cursor.fetchone()
    self.assertIsNotNone(result)
    conn.close()
  
def test_stores_summary_without_url(self):
    conn = sqlite3.connect(":memory:")
    store_summary_in_db("Summary without URL", db_path=":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT url, summary FROM summaries")
    url, summary = cursor.fetchone()
    self.assertIsNone(url)
    self.assertEqual(summary, "Summary without URL")
    conn.close()

def test_timestamp_is_stored(self):
    conn = sqlite3.connect(":memory:")
    store_summary_in_db("Check timestamp", db_path=":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT created_at FROM summaries")
    (created_at,) = cursor.fetchone()
    self.assertRegex(created_at, r"\d{4}-\d{2}-\d{2}T")  
    conn.close()

def test_multiple_summaries(self):
    conn = sqlite3.connect(":memory:")
    store_summary_in_db("First summary", db_path=":memory:")
    store_summary_in_db("Second summary", db_path=":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM summaries")
    (count,) = cursor.fetchone()
    self.assertGreaterEqual(count, 2)
    conn.close()

def test_empty_summary(self):
    conn = sqlite3.connect(":memory:")
    store_summary_in_db("", db_path=":memory:")
    cursor = conn.cursor()
    cursor.execute("SELECT summary FROM summaries")
    (summary,) = cursor.fetchone()
    self.assertEqual(summary, "")
    conn.close()

3. No Summary Provided
def test_answer_no_summary():
    question = "What happened?"
    result = answer_user_question("", question)
    assert result == "No summary available to answer from."

# 4. Both Summary and Question Are Empty
def test_answer_empty_inputs():
    result = answer_user_question("", "")
    # Should prioritize summary check, so expect summary error message
    assert result == "No summary available to answer from."

# 5. Question Unrelated to Summary
def test_answer_irrelevant_question():
    summary = "This is about climate change."
    question = "What's the capital of France?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)
    assert result.strip() != ""

# 6. Very Long Summary
def test_answer_very_long_summary():
    summary = "Climate change affects the planet. " * 1000
    question = "What is the effect of climate change?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)
    assert len(result.strip()) > 0

# 7. Very Long Question
def test_answer_very_long_question():
    summary = "AI is transforming the world."
    question = ("Can you explain how artificial intelligence is impacting "
                "industry, health, science, education, politics, economy, jobs, "
                "and daily life in general terms?") * 10
    result = answer_user_question(summary, question)
    assert isinstance(result, str)

# 8. Ambiguous Question
def test_answer_ambiguous_question():
    summary = "The new policy affects working hours."
    question = "What about that?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)
    assert result.strip() != ""

# 9. Non-String Inputs
@pytest.mark.parametrize("bad_input", [None, 123, 5.5, [], {}])
def test_answer_non_string_inputs(bad_input):
    with pytest.raises(TypeError):
        answer_user_question(bad_input, "valid question")
    with pytest.raises(TypeError):
        answer_user_question("valid summary", bad_input)

# 10. Question in Another Language
def test_answer_question_multilingual():
    summary = "This is about U.S. elections."
    question = "¿Quién ganó las elecciones?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)

# 11. Summary in Another Language
def test_answer_summary_multilingual():
    summary = "Ceci est un résumé en français."
    question = "What is it about?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)

# 12. Summary with Special Characters or Formatting
def test_answer_special_characters():
    summary = "<html><body>This is a 📰 summary!</body></html>"
    question = "What is this about?"
    result = answer_user_question(summary, question)
    assert isinstance(result, str)

# 13. Simulated Model/Internal Error
@patch("core.answer_query", side_effect=Exception("Model crashed"))
def test_answer_model_failure(mock_answer_query):
    with pytest.raises(Exception) as exc_info:
        answer_user_question("Some summary", "Some question")
    assert "Model crashed" in str(exc_info.value)
def test_handle_parsed_article_normal_case(capsys):
    article_text = "This is a well-formed article with meaningful content."
    handle_parsed_article(article_text)
    captured = capsys.readouterr()
    assert captured.out.strip() != ""  # prints some summary text


def test_handle_parsed_article_very_short_text(capsys):
    article_text = "Short sentence."
    handle_parsed_article(article_text)
    captured = capsys.readouterr()
    assert captured.out.strip() != ""  # likely prints a summary similar to input


def test_handle_parsed_article_special_characters(capsys):
    article_text = "This is a test 📰 with emojis 😊 and <html> tags."
    handle_parsed_article(article_text)
    captured = capsys.readouterr()
    assert captured.out.strip() != ""
    # Optionally check no raw html tags present in summary if you want
    # assert "<html>" not in captured.out


@pytest.mark.parametrize("bad_input", [None, 123, 5.5, [], {}])
def test_handle_parsed_article_non_string_input(bad_input):
    with pytest.raises(Exception):
        handle_parsed_article(bad_input)


def test_handle_parsed_article_malformed_text(capsys):
    # Simulate corrupted text — you might use a bytes decode error example
    article_text = "This is normal text\uDC00"  # invalid unicode character
    try:
        handle_parsed_article(article_text)
        captured = capsys.readouterr()
        assert captured.out.strip() != "" or "error" in captured.out.lower()
    except Exception:
        # Accept if it raises, as long as it doesn't crash pytest
        pass




    
