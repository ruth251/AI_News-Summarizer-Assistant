from core import handle_article, handle_link, answer_user_question

# Test 1: Handle plain article text
article_text = """
In Italy, two construction workers in Tezze sul Brenta were hospitalized after falling ill due to extreme heat.
One of the workers is in a coma. The intense heat also led to power outages in Florence due to overuse of air conditioners and overheating of underground cables.
Experts say heatwaves are becoming more common due to climate change.
"""

result1 = handle_article(article_text, question="What caused the power outage in Florence?")
print("Test 1: handle_article")
print("Summary:\n", result1["summary"])
print("Answer:\n", result1["answer"])
print("\n" + "="*50 + "\n")

# Test 2: Handle article from URL
url = "https://edition.cnn.com/2025/07/02/business/trump-japan-trade-deal-intl-hnk"
result2 = handle_link(url, question="What did Trump say about Japan?")
print("Test 2: handle_link")
if "error" in result2:
    print("Error fetching URL:", result2["error"])
else:
    print("Summary:\n", result2["summary"])
    print("Answer:\n", result2["answer"])
print("\n" + "="*50 + "\n")

# Test 3: Ask a question from existing summary only
sample_summary = "Trump questioned the progress of a trade deal with Japan and indicated no plans to extend tariff pauses."
answer3 = answer_user_question(sample_summary, "What did Trump question?")
print("Test 3: answer_user_question")
print("Answer:\n", answer3)
