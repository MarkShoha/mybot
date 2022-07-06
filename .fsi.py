import telebot
bot = telebot.TeleBot('r1461769848:AAFDZwVcmPJVbkymh9qhr2dq6cz22AxQvLv')
users=set()

@bot.message_handler(func=lambda message: not message.from_user.is_bot)
def on_message(message):
    print(message)
    bot.send_message(message.from_user.id, "Сообщение отправлен-: 1 ")
    for user in users:
        if user != message.from_user.id:
            bot.send_message(user. message.text)
            users.add(message.from_user.id)
bot.polling(none_stop=True)