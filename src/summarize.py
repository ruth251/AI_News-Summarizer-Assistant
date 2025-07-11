from summarizer_utils import summarize_text


text = "In Italy, two construction workers in Tezze sul Brenta, in the province of Vicenza, were rushed to hospital at 15:30 local time on Tuesday because they fell ill as a result of the heat while working in a hole.One of the workers is in a coma, according to reports by Italian news agency Ansa, who report that he was resuscitated, intubated and taken to San Bassiano hospital by helicopter.Intense heat on Tuesday led to power outages in Florence city centre, due to a peak in consumption from air conditioners and some underground electrical cables overheating, Italian media reported.The blackout on Tuesday afternoon meant homes, hotels and shops were without power. ATMs were also out of action and alarm systems in shops and other business premises were deactivated.In Bergamo, the overheating of underground cables also caused a power outage in half of the city. On one side towards Piazza della Liberta, the lights were on and people could congregate outside, while on the other, towards Sentierone, no electricity meant dark shop fronts and little to no nightlife.The blackout in Bergamo on Tuesday spanned several hours, with no power between 16:00 and 22:46 local time.Heatwaves are becoming more common due to human-caused climate change, according to the UN's Intergovernmental Panel on Climate Change.Extreme hot weather will happen more often – and become even more intense - as the planet continues to warm, it has said.The World Meteorological Organization (WMO), which is the UN's weather and climate agency, said on Tuesday that human-induced climate change means\"extreme heat is becoming more frequent and intense\"."


if __name__ == "__main__":
    print("\nSummary:\n")
    print(summarize_text(text))

