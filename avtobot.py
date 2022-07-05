import time

from aiogram.types import ParseMode

global prov
prov =0
import telebot
from paho.mqtt.client import Client
bot = telebot.TeleBot('5423912192:AAGJoP0B7lor-9cHkTx1SdXdVYyFtMfYjVE')
#5423912192:AAGJoP0B7lor-9cHkTx1SdXdVYyFtMfYjVE
from telebot import types
def receive_message(device, userdata, message):
    global mqtt_message

    mqtt_message = message.payload.decode()
    print(mqtt_message)

@bot.message_handler(commands=["start"])
def start(m):

        bot.send_message(m.chat.id,'Я — Бот АМК Автосеть рф.В считанные мгновения могу\n– познакомить с автомобилями в наличии;\n– рассказать , как легко и выгодно продать ваш автомобиль\n- подать предварительную заявку на кредит\n- записать на сервис\n- уведомить об актуальных акциях')
        # Со мной легко! Выберите из предложенных ниже вариантов, с чем я могу вам помочь.request_contact=True
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_oven1 = types.KeyboardButton(text='отправить телефон',request_contact=True)
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)
        bot.send_message(m.chat.id, 'Авторизуйтесь!',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def oshibka(message):
    if prov != 1:
        bot.send_message(message.chat.id, 'Неверно, нажмите на кнопку.')
@bot.message_handler(content_types=['contact'])
def contact(message):
    global prov
    prov = 1
    keyboard = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, 'Авторизация успешна!', reply_markup=keyboard)

    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_oven = types.InlineKeyboardButton(text='АВТО В НАЛИЧИИ', callback_data='v_nal')
    # И добавляем кнопку на экран
    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text='ПОЛУЧИТЬ ПРЕДВАРИТЕЛЬНОЕ  РЕШЕНИЕ ПО КРЕДИТУ',
                                           callback_data='pprpk')
    keyboard.add(key_telec)
    key_telec1 = types.InlineKeyboardButton(text='АВТО ПОДБОР', callback_data='avto_podbor')
    keyboard.add(key_telec1)
    key_telec11 = types.InlineKeyboardButton(text='ПРОДАТЬ АВТО', callback_data='prod_avto')
    keyboard.add(key_telec11)
    key_telec111 = types.InlineKeyboardButton(text='ЗАПИСАТЬСЯ НА СЕРВИС', callback_data='zap_na_serv')
    keyboard.add(key_telec111)
    key_telec1111 = types.InlineKeyboardButton(text='ДОПОЛНИТЕЛЬНОЕ ОБОРУДОВАНИЕ', callback_data='dop_ob')
    keyboard.add(key_telec1111)
    key_telec11111 = types.InlineKeyboardButton(text='АКЦИИ', callback_data='sale')
    keyboard.add(key_telec11111)
    key_telec111111 = types.InlineKeyboardButton(text='ОФОРМИТЬ ОСАГО ОНЛАЙН', callback_data='oso')
    keyboard.add(key_telec111111)
    bot.send_message(message.chat.id,
                     text='Со мной легко!\nВыберите из предложенных ниже вариантов, с чем я могу вам помочь.',
                     reply_markup=keyboard)
    text = message.contact.phone_number
    device.publish("amk_avtoset1/phones", text)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zap_na_serv":
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Техническое обслуживание (ТО)', callback_data='to')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_oven1 = types.InlineKeyboardButton(text='Ремонт и обслуживание двигателей', callback_data='r_and_o_d')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)
        key_oven11 = types.InlineKeyboardButton(text='Диагностика, обслуживание и ремонт АКПП', callback_data='akpp')
        # И добавляем кнопку на экран
        keyboard.add(key_oven11)
        key_oven111 = types.InlineKeyboardButton(text='Ремонт трансмиссии', callback_data='r_t')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111)
        key_oven1111 = types.InlineKeyboardButton(text='Ремонт рулевого управления', callback_data='rru')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1111)
        key_oven11111 = types.InlineKeyboardButton(text='Ремонт подвески', callback_data='rp')
        # И добавляем кнопку на экран
        keyboard.add(key_oven11111)
        key_oven111111 = types.InlineKeyboardButton(text='Диагностика', callback_data='diagnos')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111)
        key_oven1111111 = types.InlineKeyboardButton(text='Автоэлектрика', callback_data='avto_electro')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1111111)
        key_oven11111111 = types.InlineKeyboardButton(text='Заправка кондиционера', callback_data='z_k')
        # И добавляем кнопку на экран
        keyboard.add(key_oven11111111)
        key_oven111111111 = types.InlineKeyboardButton(text='Шиномонтаж,развал-схождения', callback_data='sh_r-s')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111)
        key_oven1111111111 = types.InlineKeyboardButton(text='Кузовной ремонт', callback_data='kuz_remont')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1111111111)
        key_oven11111111111 = types.InlineKeyboardButton(text='Детейлинг', callback_data='deteling')
        # И добавляем кнопку на экран
        keyboard.add(key_oven11111111111)
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Выбрать услугу',
                         reply_markup=keyboard)
    if call.data == "v_menu":
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='АВТО В НАЛИЧИИ', callback_data='v_nal')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='ПОЛУЧИТЬ ПРЕДВАРИТЕЛЬНОЕ  РЕШЕНИЕ ПО КРЕДИТУ',
                                               callback_data='pprpk')
        keyboard.add(key_telec)
        key_telec1 = types.InlineKeyboardButton(text='АВТО ПОДБОР', callback_data='avto_podbor')
        keyboard.add(key_telec1)
        key_telec11 = types.InlineKeyboardButton(text='ПРОДАТЬ АВТО', callback_data='prod_avto')
        keyboard.add(key_telec11)
        key_telec111 = types.InlineKeyboardButton(text='ЗАПИСАТЬСЯ НА СЕРВИС', callback_data='zap_na_serv')
        keyboard.add(key_telec111)
        key_telec1111 = types.InlineKeyboardButton(text='ДОПОЛНИТЕЛЬНОЕ ОБОРУДОВАНИЕ', callback_data='dop_ob')
        keyboard.add(key_telec1111)
        key_telec11111 = types.InlineKeyboardButton(text='АКЦИИ', callback_data='sale')
        keyboard.add(key_telec11111)
        key_telec111111 = types.InlineKeyboardButton(text='ОФОРМИТЬ ОСАГО ОНЛАЙН', callback_data='oso')
        keyboard.add(key_telec111111)
        bot.send_message(call.message.chat.id,
                         text='Со мной легко!\nВыберите из предложенных ниже вариантов, с чем я могу вам помочь.',
                         reply_markup=keyboard)
    if call.data == "to":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)


        device.publish("amk_avtoset1/uslugi",'Тех. обслуж.')
    if call.data == "r_and_o_d":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Ремонт и обслуж. двигат.')
    if call.data == "akpp":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'АКПП')
    if call.data == "r_t":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Ремонт трансмис.')
    if call.data == "rru":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Ремонт рул. управ.')
    if call.data == "rp":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Ремонт подвески')
    if call.data == "diagnos":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Диагностика')
    if call.data == "avto_electro":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Авто электрика')
    if call.data == "sh_r-s":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Шиномонтаж,развал-схождения')
    if call.data == "kuz_remont":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'куз. ремонт')
    if call.data == "deteling":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi",'Детейлинг')
    if call.data == 'v_nal':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Екатеринбург',url='https://auto.ru/diler/cars/used/autoset_rf_ekaterinburg/?from=dealer-listing-list&geo_radius=200 ')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_oven1 = types.InlineKeyboardButton(text='Самара',url='https://www.avito.ru/i216871666/samara?page_from=from_shops_list')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)
        key_oven12 = types.InlineKeyboardButton(text='Связаться со специалистом',url='https://t.me/sashakhasanova')
        keyboard.add(key_oven12)
        bot.send_message(call.message.chat.id, 'Выберите город', reply_markup=keyboard)


device = Client('d656894767ss')

device.username_pw_set("amk_avtoset1", "amk_avtoset1")
device.connect("mqtt.pi40.ru", 1883)

device.on_message = receive_message
device.loop_start()
bot.polling(none_stop=True)