import pyowm
import telebot
from telebot import types

#pyowm API key
owm = pyowm.OWM('22ab75f800d278c86e42b0ee15ad66b3', language = "ro")
bot = telebot.TeleBot("994585889:AAFQk9C3JhwrkEwMey_PrkAQbjLnOCYEah8")


def send_temp(message_chat_id, message_text):
    observation = owm.weather_at_place(message_text)
    w = observation.get_weather()
    temp = w.get_temperature('celsius')["temp"]
    answ = "In localitatea " + message_text + " sunt " + str(temp) + " grade!" + "\n"
    answ += "Status: " + w.get_detailed_status() + "\n"
    bot.send_message(message_chat_id, answ)
