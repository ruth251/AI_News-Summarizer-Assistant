# AI_News-Summarizer-Assistant
<!-- Testing Tools & Libraries -->
The tests are written using the pytest framework, and the spaCy library is used for natural language processing, specifically for sentence segmentation and token-level filtering. The tests focus on verifying the behavior and robustness of two core functions: parse_text(text) and summarize_text(sentences, num_sentences=3).

 <!-- Tests for parse_text(text) -->
# test_parse_text_raises_type_error
This test checks if the parse_text function raises a TypeError when it receives non-string inputs such as integers, None, or lists. This ensures the function validates its input type properly.

# test_parse_text_empty_string
Verifies that when an empty string ("") is passed to parse_text, the result is an empty list. This confirms the function doesn't break or misbehave on blank inputs.

# test_parse_text_whitespace_only
Similar to the empty string case, this test checks if a string made entirely of whitespace or newline characters returns an empty list.

# test_parse_text_single_sentence
Ensures that a well-formed single sentence returns a list containing exactly one sentence. This confirms basic sentence parsing is working correctly.

# test_parse_text_long_text
Tests the function with a long input consisting of the same sentence repeated many times (e.g., 1000 times). This confirms the function's scalability and performance under high-load input.

# test_parse_text_special_characters
Verifies that text containing sentences with different punctuation marks (!, ?, .) is split correctly into individual sentences.

<!-- Tests for summarize_text(sentences, num_sentences=3) -->
# test_equal_score_sentences
Checks if the function returns the first N sentences when all sentences have equal importance scores. This helps ensure ordering is preserved in the case of ties.

# test_all_stop_words
This test uses sentences made entirely of stop words to see if the summary handles "low-value" text gracefully, either returning an empty string or including such sentences anyway.

# test_empty_sentence_list & test_summarize_empty_input
These two tests ensure that when an empty list of sentences is passed to summarize_text, the result is an empty string. It protects against crashes when the input is invalid or empty.

# test_summarize_zero_requested
Checks what happens if the number of sentences requested is zero. The function should return an empty string without errors.

# test_summarize_long_input
Passes a long list of sentences (e.g., repeating "AI is evolving." 100 times) and ensures that the function returns a proper summary with the correct number of sentences. This confirms efficiency and stability.

# test_summarize_duplicate_sentences
Ensures that if the input contains duplicated sentences, the summary still includes them as appropriate, without any filtering or deduplication unless explicitly handled.

# test_summarize_trims_whitespace
Confirms that the output summary does not have leading or trailing whitespace, even if the original sentences were padded.