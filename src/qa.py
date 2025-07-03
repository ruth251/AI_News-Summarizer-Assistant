from summarizer_utils import summarize_text
from qa_utils import answer_query

text = """
In Italy, two construction workers in Tezze sul Brenta were hospitalized after falling ill due to extreme heat while working in a hole.
One of the workers is in a coma. The intense heat also led to power outages in Florence due to overuse of air conditioners and overheating of underground electrical cables.
Similar outages happened in Bergamo. Experts say these heatwaves are becoming more frequent due to human-induced climate change.
"""

summary = summarize_text(text)

question = "What happened to the two construction workers?"
answer = answer_query(summary, question)

print("Summary:\n", summary)
print("\nQuestion:", question)
print("Answer:", answer)
