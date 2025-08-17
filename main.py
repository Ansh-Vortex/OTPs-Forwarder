import os
import re
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")        # Bot token from @BotFather
FORWARD_CHAT_ID = int(os.getenv("FORWARD_CHAT_ID"))  # Your Telegram ID (@userinfobot)

# Regex to detect OTP (4–8 digit numbers)
OTP_REGEX = r"\b\d{4,8}\b"

async def forward_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Forward any message the bot receives to your main account, and make OTPs copy-friendly."""
    if update.message:
        if update.message.text:
            text = update.message.text
            otp_match = re.findall(OTP_REGEX, text)

            if otp_match:
                otp_code = otp_match[0]  # first detected OTP
                # Send OTP in monospace for one-tap copy
                await context.bot.send_message(
                    chat_id=FORWARD_CHAT_ID,
                    text=f"🔑 OTP: `{otp_code}`",
                    parse_mode="Markdown"
                )
            else:
                # Forward normal text
                await context.bot.send_message(
                    chat_id=FORWARD_CHAT_ID,
                    text=f"📩 Message:\n{text}"
                )
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
