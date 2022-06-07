from random import choice,randint
import telebot

bot = telebot.TeleBot('5402004472:AAEfYo2R_0kFKNAHOLemY2T7eboXKDi4h10')
#CAACAgIAAxkBAAIER2Ke9PE50VqljBGdw6YC3UE6Hg2wAAIfAAPANk8T5Dgz94RSmZIkBA no
#CAACAgIAAxkBAAIESGKe9POvkPiLllFc55zxMs4-9HO2AAIVAAPANk8TzVamO2GeZOckBA ya

from telebot import types
@bot.message_handler(commands=["start"])
def start(m):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="запустить полив")
    keyboard.add(button_1)
    button_2 = "остановить полив"
    keyboard.add(button_2)
    bot.send_message(m.chat.id,"Если хотите росмотреть состояние люков напишите /hatches,если состояние поливальниц /waterings\nЕсли хотите узнать координаты напишите /cordinats", reply_markup=keyboard)






@bot.message_handler(commands=["hatches"])
def start(m ):
    iu=['всё ок']
    waqs=choice(iu)
    bot.send_message(m.chat.id,waqs)
@bot.message_handler(commands=["waterings"])
def start(m):
    global waqs1
    iu=['проблема!!']
    waqs1=choice(iu)
    bot.send_message(m.chat.id,waqs1)
    bot.send_message(m.chat.id, 'http://172.20.10.6:3000 ')


@bot.message_handler(commands=["cordinats"])
def start(m):

    war1=randint(-100,100)
    war12 = randint(-100,100)

    bot.send_message(m.chat.id,  war1 )
    bot.send_message(m.chat.id,  war12)
@bot.message_handler(content_types=['text'])
def text(m):

    if m.text == 'запустить полив':
        bot.send_message(m.chat.id,'полив запущен')
    elif m.text == 'остановить полив':
        bot.send_message(m.chat.id,"полив остановлен")
bot.polling()