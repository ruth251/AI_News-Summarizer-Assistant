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
