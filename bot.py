from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user (bot, update):
    text = "Нажали на старт"
    logging.info(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет {}, ты ляпнул: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.first_name, update.message.chat_id, update.message.text )
    update.message.reply_text(user_text)


#тело
def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.REQUEST_KWARGS)

    logging.info('Bot starting')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling() #регулярно ходи на телеграм и проверяй обновления
    mybot.idle() #работай до принудительного завершения



main()



