import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import id_cred_bot

logging.basicConfig(filename='bot.log', level=logging.INFO)

def greet_user(update, context):
    print("Вызван /start")
    print(update)
    #print(2/0)
    update.message.reply_text('Привет, пользь! Ты вызвал команду /start')

def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    #mybot = Updater("2139767614:AAFhmNIgNRRrlbzKfb3Vd2H_CsR3N7PWr08", use_context=True)
    mybot = Updater(id_cred_bot.API_KEY, use_context=True)
    # Командуем боту начать ходить в Telegram за сообщениями
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()
if __name__ == "__main__":
    main()
