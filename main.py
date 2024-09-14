from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = "7511311155:AAHnvfAIu6YBhdtpXsquSp1Dym8DM2mgAXQ"
UNAME: Final = "@asgharabot"

my_text = "hello im asghar ale im a web and AI developer how can i help you?\nyou can contact me with this bot, just choose from the option buttons."
my_text_fa = "سلام من اصغر اله هستم برنامه نویس پایتون و متخصص برنامه نویسی وب و هوش مصنوعی چطور میتونم کمکتون کنم؟\nبا این ربات میتونید با من ارتباط برقرار کنید کافیه تو گزینه ها انتخاب کنید."

# commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(my_text_fa+"\n"+my_text)

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(my_text_fa+"\n"+my_text)

# handling responses
def handle_response(text: str) -> str:
    preprocessed_text = text.lower()
    if 'to asghar:' in preprocessed_text:
        return "Your message was sent!"
    return my_text_fa+"\n"+my_text

# message handler
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text
    
    print(f"user ({update.message.chat.id}) in {message_type}: {text}")
    
    if message_type == "group":
        if UNAME in text:
            new_t: str = text.replace(UNAME, '').strip()
            response: str = handle_response(new_t)
        else:
            return
    else:
        response: str = handle_response(text)
    
    print("BOT: ", response)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error: {context.error}")

if __name__ == '__main__':
    print("bot is running...")
    app = Application.builder().token(TOKEN).build()
    
    # commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    
    # messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    
    # errors
    app.add_error_handler(error)
    
    # polls
    print("polling...")
    app.run_polling(poll_interval=5)
