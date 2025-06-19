from marketmood.googlenews.analyser import analyze_sentiment
from marketmood.googlenews.scraper import get_headlines
from urllib.parse import quote


def run_analysis(keyword):
    keyword_encoded = quote(keyword)
    headlines = get_headlines(keyword_encoded)
    results = analyze_sentiment(headlines)


    return headlines, results

