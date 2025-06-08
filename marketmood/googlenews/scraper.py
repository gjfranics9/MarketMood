import feedparser

def get_headlines(keyword, max_items=20):
    url = f"https://news.google.com/rss/search?q={keyword}"
    feed = feedparser.parse(url)
    headlines = [entry.title for entry in feed.entries[:max_items]]
    return headlines
