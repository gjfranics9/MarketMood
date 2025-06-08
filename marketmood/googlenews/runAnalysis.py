from analyser import analyze_sentiment
from scraper import get_headlines
from collections import Counter

if __name__ == "__main__":
    keyword = input("Enter a keyword you want to search google news for: ")
    headlines = get_headlines(keyword)
    results = analyze_sentiment(headlines)

    counts = Counter([r['label'] for r in results])
    print(f"\nSentiment Summary for '{keyword}':")
    for label in ["positive", "neutral", "negative"]:
        print(f"{label.capitalize()}: {counts.get(label, 0)}")

    # Print top headlines
    print("\nSample Headlines:")
    for r in results[:5]:
        print(f"[{r['label'].upper()}] {r['text']}")
