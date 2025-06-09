from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(headlines):
    results = []
    for text in headlines:
        score = analyzer.polarity_scores(text)
        results.append({
            "compound": score["compound"],
            "label": label_from_score(score["compound"])
        })
    return results

def label_from_score(compound):
    if compound >= 0.05:
        return "positive"
    elif compound <= -0.05:
        return "negative"
    else:
        return "neutral"
