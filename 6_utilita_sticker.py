
import telebot

bot = telebot.TeleBot('5088221163:AAEqI9PCV5oU_wNOtBj2htFr03FRHjEuziQ')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message_stiker):
    print(message_stiker.sticker.file_id)

bot.polling()