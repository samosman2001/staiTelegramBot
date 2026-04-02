# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from telegram import Update
from telegram.ext import ApplicationBuilder,CommandHandler,ContextTypes
TOKEN = "8155567969:AAF4X57d0J7N6WSiHZDD9gfwWz8sHvLbPHE"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", helper_command))
    app.run_polling()

async def start(update:Update,context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How are you doing sir ")
async def helper_command(update:Update,context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("How Can we assist you")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
