from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Привет {update.effective_user.first_name}')

async def tukto(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Я человек')


app = ApplicationBuilder().token("paste token").build()

app.add_handler(CommandHandler("hello", hello))

app.add_handler(CommandHandler("tukto", tukto))
app.run_polling()