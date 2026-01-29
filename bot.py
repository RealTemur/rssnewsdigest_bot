import uuid
from telegram import (
    Update,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    InlineQueryHandler,
    ContextTypes
)

from config import TELEGRAM_BOT_TOKEN
from rss import fetch_news
from llm import build_digest


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Напиши @rssnewsdigest_bot в любом чате — получишь дайджест."
    )


async def digest_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⏳ Собираю дайджест...")
    news = fetch_news(hours=3)
    text = build_digest(news)
    await update.message.reply_text(text, disable_web_page_preview=True)


async def inline_query(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.inline_query.query.lower()
    hours = 3

    if "1" in query:
        hours = 1
    elif "6" in query:
        hours = 6

    news = fetch_news(hours=hours)
    text = build_digest(news)

    result = InlineQueryResultArticle(
        id=str(uuid.uuid4()),
        title=f"Дайджест за {hours}ч",
        description="Ключевые новости и темы",
        input_message_content=InputTextMessageContent(
            text,
            disable_web_page_preview=True
        )
    )

    await update.inline_query.answer([result], cache_time=0)


def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("digest", digest_cmd))
    app.add_handler(InlineQueryHandler(inline_query))

    app.run_polling()


if __name__ == "__main__":
    main()