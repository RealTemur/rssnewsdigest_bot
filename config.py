import os

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

RSS_FEEDS = {
    "РБК": "https://rssexport.rbc.ru/rbcnews/news/30/full.rss",
    "ТАСС": "https://tass.ru/rss/v2.xml",
    "Коммерсант": "https://www.kommersant.ru/RSS/main.xml",
    "Ведомости": "https://www.vedomosti.ru/rss/news",
    "Интерфакс": "https://www.interfax.ru/rss.asp",
    "Lenta.ru": "https://lenta.ru/rss",
    "Газета.ru": "https://www.gazeta.ru/export/rss/first.xml",
    "Известия": "https://iz.ru/xml/rss/all.xml",
    "РИА Новости": "https://ria.ru/export/rss2/archive/index.xml",
    "Meduza": "https://meduza.io/rss/all",
}