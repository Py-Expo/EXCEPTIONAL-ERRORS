import feedparser

def get_news_feed(feed_url):
    # Parse the RSS feed
    feed = feedparser.parse(feed_url)

    # Check if parsing was successful
    if feed.get('bozo', 0) == 0:
        # Iterate through entries in the feed
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Published: {entry.published}")
            print(f"Summary: {entry.summary}")
            print(f"Link: {entry.link}")
            print("\n")

    else:
        print("Error parsing feed")

if __name__ == "__main__":
    # Example usage: BBC News RSS feed
    bbc_news_feed_url = "http://feeds.bbci.co.uk/news/rss.xml"
    get_news_feed(bbc_news_feed_url)
