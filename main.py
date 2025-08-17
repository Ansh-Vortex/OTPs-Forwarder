import os
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")        # Bot token from @BotFather
FORWARD_CHAT_ID = int(os.getenv("FORWARD_CHAT_ID"))  # Your Telegram ID (@userinfobot)

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Forward any message the bot receives to your main account."""
    if update.message:
        # Forward text
        if update.message.text:
            await context.bot.send_message(
                chat_id=FORWARD_CHAT_ID,
                text=f"📩 OTP Forwarded:\n{update.message.text}"
            )
        # Forward media (photo, video, document, etc.)
        elif update.message.photo:
            await update.message.forward(chat_id=FORWARD_CHAT_ID)
        elif update.message.document:
            await update.message.forward(chat_id=FORWARD_CHAT_ID)
        elif update.message.audio:
            await update.message.forward(chat_id=FORWARD_CHAT_ID)
        elif update.message.voice:
            await update.message.forward(chat_id=FORWARD_CHAT_ID)
        elif update.message.video:
            await update.message.forward(chat_id=FORWARD_CHAT_ID)

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, forward_message))
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()