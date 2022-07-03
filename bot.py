
# while True:
#     ser()
# print('eerer')

# Подключаем модуль для Телеграма
import time
print('yees1')
import pyglet
from paho.mqtt.client import Client
import datetime
import random
import telebot
now = datetime.datetime.now()

global er
global last_er
er = ['хор.', "ясно", "утро", "вых.", "кух."]
print(1)
last_er = ['хор.', "ясно", "утро", "вых.", "кух."]
mqtt_message=''
def ser():
    last_er = ['хор.', "ясно", "утро", "вых.", "кух."]
    if er != last_er:
        last_er = er
        print('данные изменены')
bot = telebot.TeleBot('5556225060:AAHUCMGNj-0om9bIl8YudbsdwnavpEC6LJY')
# Импортируем типы из модуля, чтобы создавать кнопки
from telebot import types
global g
mqtt_message1 = ''
g=random.randint(0,2)
def gg1(device, userdata, message):
    global mqtt_message1
    mqtt_message1= message.payload.decode()
    print(mqtt_message1)
    if mqtt_message1 == 'go':
        song = pyglet.media.load('prekras.mp3')
        song.play()
        time.sleep(1.5)
        song1 = pyglet.media.load('den.mp3')
        song1.play()
        time.sleep(1.5)
        song2 = pyglet.media.load('vih.mp3')
        song2.play()
        time.sleep(1.5)
def receive_message(device, userdata, message):
    global mqtt_message
    global mqtt_message1
    mqtt_message = message.payload.decode()
    print(mqtt_message)

    # Если юзер прислал 1, выдаем ему случайный факт
    if mqtt_message == 'kitchen':
        er = ['хор.', "ясно", "утро", "вых.", "кух."]
        bot.send_message(id, text='Вы на кухне')
        if mqtt_message == 'go':
            song = pyglet.media.load('kuh.mp3')

            song.play()

    if mqtt_message == 'bedroom':

        er = ['хор.', "ясно", "утро", "вых.", "спал."]
        bot.send_message(id, text='Вы в спальне')
        if mqtt_message1 == 'go':
            song = pyglet.media.load('spal.mp3')
            song.play()
    if mqtt_message == 'hall':
        er = ['хор.', "ясно", "утро", "вых.", "кор."]
        bot.send_message(id, text='Вы в коридоре')
        if mqtt_message1 =='go':
            song = pyglet.media.load('kor.mp3')
            song.play()

    if mqtt_message == '1' :
        keyboard = types.InlineKeyboardMarkup()

        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='задача', callback_data='zodiac')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='тренировка', callback_data='zodiac1')
        keyboard.add(key_telec)

        bot.send_message(id, text='Ты весёлый!Твоё настроение на высоте\n Выбери своё развлечение', reply_markup=keyboard)
        er = ['хор.', "ясно", "утро", "вых.", "спал."]
        ser()
        if mqtt_message1 == 'go':
            song = pyglet.media.load('ves.mp3')
            song.play()
    # Если юзер прислал 2, выдаем умную мысль
    elif mqtt_message == '0':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='анекдот', callback_data='zodiac2')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='фильм', callback_data='zodiac12')
        keyboard.add(key_telec)

        bot.send_message(id, text='Ты грустный.Очень жалко:(,но я подниму тебе настроение!\nВыбери своё развлечение', reply_markup=keyboard)
        er = ['плох.', "ясно", "утро", "вых.", "спал."]
        ser()
        if mqtt_message1 == 'go':
            song = pyglet.media.load('ploh.mp3')
            # songp=pyglet.Player()
            # songp.pyglet
            song.play()
    # Если юзер прислал 2, выдаем умную мысль
    # Отсылаем юзеру сообщение в его чат
# Указываем токен
@bot.message_handler(commands=["start"])
def start(m):
        global id, q_f, dsfgy, rw, mqtt_message1
        # Добавляем две кнопки
        id = m.chat.id
        dsfgy=0
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ov212en = types.InlineKeyboardButton(text='настройка', callback_data='u71')
        # И добавляем кнопку на экран
        keyboard.add(key_ov212en)
        key_t11elec = types.InlineKeyboardButton(text='запуск робота', callback_data='u61')
        keyboard.add(key_t11elec)
        bot.send_message(m.chat.id,
                         'я робот-соцпсихолог!Я помогу людям с низкой социальностью!\nНапиши /anekdot чтобы узнать смешной анекдот.\nНапиши /film чтобы узнать какой фильм тебе посмотреть.', reply_markup=keyboard)
        # if mqtt_message1 == 'go':
        #     song = pyglet.media.load('priv.mp3')
        #     song.play()

    # bot.send_message(id,'По ощущению - +23Ветер\n-4 м/c, СВ \nДавление - 752 мм рт. ст.\nВлажность - 41 %\nГ/м активность - 2 балла\n Вода - +16,4')

@bot.message_handler(commands=["anekdot"])
def sanekdot(m, res=False):
    first2 = [ 'Ещё в годы правления императрицы Елизаветы был издан указ, запрещающий взяточничество государственных чиновников. Скажите, а когда этот указ вступит в силу?',
               'Если ребенок не хочет есть мясо, чем его заменить? — Собакой. Собака всегда хочет есть мясо.',
               'Есть французская пословица: всю первую половину жизни мы ждём вторую, а всю вторую — вспоминаем первую...',
               'Победитель тот, кто встает на один раз больше, чем падает.']


    msg = random.choice(first2)

    # Отправляем текст в Телеграм
    print(msg)
    bot.send_message(m.chat.id, 'Вы выбрали анекдот.\nАндекдот: ' + msg )

@bot.message_handler(commands=["film"])
def sfilm(m, res=False):
    first12 = ['бегущий в лабиринте\nПодростки пытаются выбраться из изолированного «приюта». Начало молодежной саги по бестселлеру Джеймса Дэшнера.',
               'люси\nНаивная студентка превращается в сверхчеловека. Экшен со Скарлетт Йоханссон о возможностях человеческого мозга.',
               'человек паук нет пути домой\nЖизнь и репутация Питера Паркера оказываются под угрозой, поскольку Мистерио раскрыл всему миру тайну личности Человека-паука.',
               'конек горбунок\nПростой парень Иван и волшебный конь служат царю-самодуру. Фильм-сказка с уникальной компьютерной графикой.']
    msg = random.choice(first12)
    # Отправляем текст в Телеграм
    bot.send_message(m.chat.id, 'Вы выбрали фильмы: \nФильм: ' + msg)
# Получение сообщений от юзера
# @bot.message_handler(content_types=["text"])
# def handle_text(message):



@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):

    first = ['Сколько месяцев в году имеют 28 дней?',
             'Что в огне не горит и в воде не тонет?',
             'Кого австралийцы называют морской осой?']

    first1 = [  'отжмись 20 раз', 'присядь 40 раз', 'пробеги километр','планка 40 секунд']
    first2 = [ 'Ещё в годы правления императрицы Елизаветы был издан указ, запрещающий взяточничество государственных чиновников. Скажите, а когда этот указ вступит в силу?  ',
               'Если ребенок не хочет есть мясо, чем его заменить? — Собакой. Собака всегда хочет есть мясо.',
               'Есть французская пословица: всю первую половину жизни мы ждём вторую, а всю вторую — вспоминаем первую...',
               'Победитель тот, кто встает на один раз больше, чем падает.']
    first12 = ['бегущий в лабиринте', 'люси', 'человек паук нет пути домой','конек горбунок','люди в черном']
    if call.data == "zodiac2":
        # Формируем гороскоп

        msg = random.choice(first2)

        # Отправляем текст в Телеграм
        print(msg)
        bot.send_message(call.message.chat.id, 'Вы выбрали анекдот.\nАндекдот: ' + msg )


    if call.data == "zodiac12":
        # Формируем гороскоп
        msg = random.choice(first12)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Вы выбрали фильмы: \nФильм: ' +msg)
    if call.data == "zodiac":
        # Формируем гороскоп

        msg = first[g]

        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'вы выбрали задачу. \nЗадача:'+ msg)
    if call.data == "zodiac1":
        # Формируем гороскоп
        msg = random.choice(first1)
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'вы выбрали тренировку. \nТренировка:' +msg)
# Запускаем бота
    if call.data == "u0":
        # Формируем гороскоп
        ewqr=1
        er = ['хор.', "дождливо", "утро", "вых.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Плохая погода:(')
        ser()
        # if mqtt_message1 == 'go':
        #     song = pyglet.media.load('ploho.mp3')
        #
        #     song.play()
        print(random.randint(0,106))

    if call.data == "u61":
        device.publish("client_sasha/social_bot", 'start')
    if call.data == "u71":

        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ov212en = types.InlineKeyboardButton(text='утро', callback_data='u7')
        # И добавляем кнопку на экран
        keyboard.add(key_ov212en)
        key_t11elec = types.InlineKeyboardButton(text='день', callback_data='u6')
        keyboard.add(key_t11elec)
        key_tele22c = types.InlineKeyboardButton(text='вечер', callback_data='u5')
        keyboard.add(key_tele22c)
        bot.send_message(id, text='Выбери время суток.', reply_markup=keyboard)
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ov212en = types.InlineKeyboardButton(text='выходные', callback_data='u4')
        # И добавляем кнопку на экран
        keyboard.add(key_ov212en)
        key_t11elec = types.InlineKeyboardButton(text='будни', callback_data='u3')
        keyboard.add(key_t11elec)

        bot.send_message(id, text='Выбери часть недели.', reply_markup=keyboard)
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ov212en1 = types.InlineKeyboardButton(text='пасмурно', callback_data='u2')
        # И добавляем кнопку на экран
        keyboard.add(key_ov212en1)
        key_t11elec1 = types.InlineKeyboardButton(text='ясно', callback_data='u1')
        keyboard.add(key_t11elec1)

        key_tele22c13 = types.InlineKeyboardButton(text='дождливый', callback_data='u0')
        keyboard.add(key_tele22c13)
        bot.send_message(id, text='Выбери погоду.', reply_markup=keyboard)
    if call.data == "u1":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "ясно", "утро", "вых.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Прекрасная погода!')
        ser()


        print(random.randint(0, 106))

    if call.data == "u2":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "пас.", "утро", "вых.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Грустная погода')
        ser()
        # if mqtt_message1 == 'go':
        #     song = pyglet.media.load('grusna.mp3')
        #     song.play()
        print(random.randint(0, 106))
        device.publish("ak/start", 'start')
    if call.data == "u3":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "ясно", "утро", "буд.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Сегодня рабочий день, успешного рабочего дня!')
        ser()
        # if mqtt_message1 == 'go':
        #     song = pyglet.media.load('rab.mp3')
        #     song.play()
        print(random.randint(0, 106))
    if call.data == "u4":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "ясно", "утро", "вых.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Сегодня выходной день, хорошего дня!')
        ser()

        print(random.randint(0,106))
    if call.data == "u5":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "ясно", "вечер", "вых.", "спал."]
        # Отправляем текст в Телеграм
        bot.send_message(call.message.chat.id,'Доброго вечера,всего самого лучшего!')
        ser()

        print(random.randint(0, 106))
    if call.data == "u6":
        ewqr = 1
        er = ['хор.', "ясно", "день", "вых.", "спал."]

        bot.send_message(call.message.chat.id, 'Прекрассный день,отличного настроения и дня!')
        ser()


        print(random.randint(0, 106))
    if call.data == "u7":
        # Формируем гороскоп
        ewqr = 1
        er = ['хор.', "ясно", "утро", "вых.", "спал."]
        # Отправляем текст в Телеграм

        bot.send_message(call.message.chat.id,'Отличное утро,хорошего дня!')
        ser()
        print(random.randint(0, 106))
        if mqtt_message1 == 'go':
            song = pyglet.media.load('prekras.mp3')
            song.play()
            time.sleep(2.5)
            song1 = pyglet.media.load('den.mp3')
            song1.play()
            time.sleep(2.5)
            song2 = pyglet.media.load('vih.mp3')
            song2.play()


# Pt2-6eh-g9Y-8i5

@bot.message_handler(content_types=['text'])
def text(message):
        q_f = ['все', 'лёд', 'медуза']
        q = q_f[g]
        print(id,q)
        if message.text == q:
            bot.send_message(id, 'правильно')
        else:
            bot.send_message(id, 'неправильно')
        print(message.chat.id, message.text)

        device.publish("client_sasha/social_bot", message.text)
# uk2-gEK-mLV-Qiy
device = Client('ddddsdsss')

device.username_pw_set("client_sasha", "dsr4mn")
device.connect("mqtt.pi40.ru", 1883)
device.subscribe("client_sasha/social_bot")
device.subscribe("client_sasha/go")
device.message_callback_add("client_sasha/go",gg1)
device.message_callback_add("client_sasha/social_bot",receive_message)
device.on_message = receive_message
device.loop_start()
bot.polling()