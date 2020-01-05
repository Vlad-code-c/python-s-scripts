import telebot
from telebot import types
import bot_temp
import exchange as exc


bot = telebot.TeleBot("994585889:AAFQk9C3JhwrkEwMey_PrkAQbjLnOCYEah8")
temp_n = "Temperature"
curs_val = "Curs Valutar"
mess = ''

#welcome message from /start command
@bot.message_handler(commands=['start'])
def start_keyboard(message):
     markup = types.ReplyKeyboardMarkup(row_width=1)
     itembtn1 = types.KeyboardButton(temp_n)
     itembtn2 = types.KeyboardButton(curs_val)
     markup.add(itembtn1)
     markup.add(itembtn2)
     bot.send_message(message.chat.id, "Choose one option:", reply_markup=markup)


#welcome message from /help command
@bot.message_handler(commands=['help'])
def send_welcome(message):
     bot.send_message(message.chat.id, """Avaliable commands: \n
     Temperature, Curs Valutar""")


#Get temperature on Temperature command
@bot.message_handler(content_types=['text'])
def temp(message):
     if message.text == temp_n:
         bot.send_message(message.chat.id, "Enter your city: ")
         bot.register_next_step_handler(message, get_city)
     elif message.text == curs_val:
          bot.send_message(message.chat.id, "Enter first valute: ")
          bot.register_next_step_handler(message, get_first_value)
          bot.send_message(message.chat.id, "Enter second valute: ")
          bot.register_for_reply(message, get_second_value)
     else:
          bot.send_message(message.chat.id, "Enter a valid option, or type /help")
          #keyboard:
          keyboard = types.InlineKeyboardMarkup() 
          key_1 = types.InlineKeyboardButton(text=temp_n, callback_data='temp')
          keyboard.add(key_1) 
          key_2 = types.InlineKeyboardButton(text=curs_val, callback_data='curs_val')
          keyboard.add(key_2)
          question = "Enter another command please!"
          bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)



def get_city(message):
     global city
     city = message.text
     try:
          bot_temp.send_temp(message.chat.id, message.text)
     except:
          bot.send_message(message.chat.id,"Something went wrong!")
          
def get_first_value(message):
     print("Test1")

def get_second_value(message):
     print("test2")

     

bot.polling(none_stop = True)