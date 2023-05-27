import telebot
import subprocess
bot = telebot.TeleBot('6047924096:AAGFRLTu_9uq7lc3BKX2s6bpNLFwZa3wVdw')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    if message.text=="/start":
        bot.send_message(message.from_user.id, "Введите запрос который хотите найти: ")
    elif message.text == "":
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)