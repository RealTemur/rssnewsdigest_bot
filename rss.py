import feedparser
from datetime import datetime, timedelta, timezone
from config import RSS_FEEDS

def fetch_news(hours=3):
    since = datetime.now(timezone.utc) - timedelta(hours=hours)
    items = []

    for source, url in RSS_FEEDS.items():
        feed = feedparser.parse(url)

        for e in feed.entries:
            published = getattr(e, "published_parsed", None)
            if not published:
                continue

            published_dt = datetime(*published[:6], tzinfo=timezone.utc)
            if published_dt < since:
                continue

            items.append({
                "source": source,
                "title": e.title,
                "summary": getattr(e, "summary", ""),
                "published_at": published_dt.isoformat()
            })

    return items