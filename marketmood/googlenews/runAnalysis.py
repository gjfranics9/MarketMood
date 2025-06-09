from marketmood.googlenews.analyser import analyze_sentiment
from marketmood.googlenews.scraper import get_headlines
from collections import Counter


def run_analysis(keyword):
    headlines = get_headlines(keyword)
    results = analyze_sentiment(headlines)


    return headlines, results

