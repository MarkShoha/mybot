name = ''
surname = ''
age = 0

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
        global id
        id = m.chat.id
        bot.send_message(m.chat.id,'Я — Бот АМК Автосеть рф.В считанные мгновения могу\n✓ познакомить с автомобилями в наличии;\n✓ рассказать , как легко и выгодно продать ваш автомобиль\n✓ подать предварительную заявку на кредит\n✓ записать на сервис\n✓ уведомить об актуальных акциях')
        # Со мной легко! Выберите из предложенных ниже вариантов, с чем я могу вам помочь.request_contact=True
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        key_oven1 = types.KeyboardButton(text='отправить телефон',request_contact=True)
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)
        bot.send_message(m.chat.id, 'Авторизуйтесь!',reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def oshibka(m):
    if prov != 1:
        bot.send_message(m.chat.id, 'Неверно, нажмите на кнопку.')
    if m.text == 'Выбрать автомобиль 🚗':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Екатеринбург',
                                              url='https://auto.ru/diler/cars/used/autoset_rf_ekaterinburg/?from=dealer-listing-list&geo_radius=200 ')
        # И добавляем кнопку на экран
        keyboard.add(key_oven)
        key_oven1 = types.InlineKeyboardButton(text='Самара',
                                               url='https://www.avito.ru/i216871666/samara?page_from=from_shops_list')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)

        bot.send_message(m.chat.id, 'Выберите город', reply_markup=keyboard)
@bot.message_handler(content_types=['contact'])
def contact(message):

    global prov
    prov = 1
    keyboard = types.ReplyKeyboardMarkup()
    key_oven321 = types.KeyboardButton(text='Выбрать автомобиль 🚗')
    # И добавляем кнопку на экран
    keyboard.add(key_oven321)
    bot.send_message(message.chat.id, 'Авторизация успешна!', reply_markup=keyboard)



    keyboard = types.InlineKeyboardMarkup()
    # По очереди готовим текст и обработчик для каждого знака зодиака
    key_oven = types.InlineKeyboardButton(text='АВТО В НАЛИЧИИ', callback_data='v_nal')
    # И добавляем кнопку на экран
    keyboard.add(key_oven)
    key_telec = types.InlineKeyboardButton(text='ЗАЯВКА НА КРЕДИТ',
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
    
    bot.send_message(message.chat.id,
                     text='Со мной легко!\nВыберите из предложенных ниже вариантов, с чем я могу вам помочь.',
                     reply_markup=keyboard)
    text = message.contact.phone_number
    device.publish("amk_avtoset1/phones", text)
@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    global prov
    prov = 1
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
        key_oven121111111 = types.InlineKeyboardButton(text='Заправка кондиционера', callback_data='z_k')
        # И добавляем кнопку на экран
        keyboard.add(key_oven121111111)
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
        key_telec = types.InlineKeyboardButton(text='ЗАЯВКА НА КРЕДИТ',
                                               callback_data='pprpk')
        keyboard.add(key_telec)
        key_telec11 = types.InlineKeyboardButton(text='ПРОДАТЬ АВТО', callback_data='prod_avto')
        keyboard.add(key_telec11)
        key_telec1 = types.InlineKeyboardButton(text='АВТО ПОДБОР', callback_data='avto_podbor')
        keyboard.add(key_telec1)

        key_telec111 = types.InlineKeyboardButton(text='ЗАПИСАТЬСЯ НА СЕРВИС', callback_data='zap_na_serv')
        keyboard.add(key_telec111)
        key_telec1111 = types.InlineKeyboardButton(text='ДОПОЛНИТЕЛЬНОЕ ОБОРУДОВАНИЕ', callback_data='dop_ob')
        keyboard.add(key_telec1111)
        key_telec11111 = types.InlineKeyboardButton(text='АКЦИИ', callback_data='sale')
        keyboard.add(key_telec11111)

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
    if call.data == "z_k":
        keyboard = types.InlineKeyboardMarkup()
        key_oven0987 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven0987)
        bot.send_message(call.message.chat.id,
                         text='Благодарим за заявку! Специалист сервиса в скором времени свяжется с вами.\n @sashakhasanova  ',
                         reply_markup=keyboard)
        device.publish("amk_avtoset1/uslugi", 'Заправка кондиционера')
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
    if call.data == 'pprpk':



        def get_surname(message):
            global surname
            surname = message.text
            bot.send_message(call.message.chat.id,'В каком году вы родились?\nПример:13.10.10')
            bot.register_next_step_handler(message, get_age)
        def get_name(message):  # получаем фамилию
            global name
            name = message.text
            bot.send_message(message.chat.id, 'Какая у вас фамилия?')
            bot.register_next_step_handler(message, get_surname)

        bot.send_message(call.message.chat.id, "Как вас зовут?")
        bot.register_next_step_handler(call.message, get_name)  # следующий шаг – функция get_name

        def get_age(message):
            global age
            # проверяем что возраст изменился

            age = message.text  # проверяем, что возраст введен корректно



            if len(age) == 8 :

                keyboard = types.InlineKeyboardMarkup() # наша клавиатура
                key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
                keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
                key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
                keyboard.add(key_no)
                question = 'Ваша дата рождения ' + str(age) + ', Вас зовут ' + name + ' ' + surname + '?'
                bot.send_message(call.message.chat.id, text=question, reply_markup=keyboard)
            else:
                keyboard = types.InlineKeyboardMarkup()
                key_oven23 = types.InlineKeyboardButton(text='Вернуться в основное меню',
                                                                  callback_data='v_menu')
                # И добавляем кнопку на экран
                keyboard.add(key_oven23)
                bot.send_message(call.message.chat.id,'Данные введены некоректно',reply_markup=keyboard)

    if call.data == "yes":
        global surname,name,age # call.data это callback_data, которую мы указали при объявлении кнопки
        # код сохранения данных, или их обработки
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)

        bot.send_message(call.message.chat.id,'Благодарим! \nНаш специалист свяжется с вами, чтобы завершить процедуру подачи заявки ' )
        device.publish('amk_avtoset1/kredit','Дата рождения   ' + str(age) + '  ФИ  '+name+'  ' + surname)
    elif call.data == "no":
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id,'Предварительная кредитная заявка отменена',reply_markup=keyboard)

        bot.send_message(call.message.chat.id, 'Оформить осаго онлайн', reply_markup=keyboard)
    if call.data == 'sale':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_oven = types.InlineKeyboardButton(text='Екатеринбург',
                                              callback_data='akcii')
        keyboard.add(key_oven)
        key_oven1 = types.InlineKeyboardButton(text='Самара',
                                               callback_data='akcii')
        # И добавляем кнопку на экран
        keyboard.add(key_oven1)

        bot.send_message(call.message.chat.id, 'Выберите город', reply_markup=keyboard)
    if call.data == 'akcii':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ove1n = types.InlineKeyboardButton(text='Особые условия для тех, кто только получил права',
                                              callback_data='osob')
        keyboard.add(key_ove1n)
        key_oven41 = types.InlineKeyboardButton(text='Сделка через салон',
                                               callback_data='salon')
        # И добавляем кнопку на экран
        keyboard.add(key_oven41)
        key_oven412 = types.InlineKeyboardButton(text='Скидка по трейд-ин',callback_data='treid_in')
        keyboard.add(key_oven412)

        key_oven21 = types.InlineKeyboardButton(text='Сервисные акции',
                                               callback_data='servis')
        # И добавляем кнопку на экран
        keyboard.add(key_oven21)
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)

        bot.send_message(call.message.chat.id, 'Действующие акции', reply_markup=keyboard)
    if call.data =='osob':
        bot.send_message(call.message.chat.id,'Особые условия для тех, кто только получил права\nДарим страховой полис на автомобиль, если стаж вашего вождения не превышает 3 х месяцев')
    if call.data =='treid_in':
        bot.send_message(call.message.chat.id, 'Скидка по трейд-ин\nПри сдачи авто в трейд ин, получите выгоду на новый автомобиль до 50 000р')
    if call.data =='salon':
        bot.send_message(call.message.chat.id,'Сделка через салон\nНашли автомобиль на досках объявлений (авто ру, авито или дром)?\n Или хотите купить авто у друга?\n Оформите кредит через наш автосалон и получите дополнительную выгоду 20 000р ')
    if call.data =='servis':
        bot.send_message(call.message.chat.id,'Сервисные акции\nСкидка при первом посещении 30%\nМасляный сервис за 3750р\nБесплатная диагностика автомобиля\n(предварительные акции) ')
    if call.data == 'dop_ob':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ove1n = types.InlineKeyboardButton(text='Дополнительное оборудование',
                                               url='https://www.avito.ru/i198746418/ekaterinburg?page_from=from_shops_list')
        keyboard.add(key_ove1n)
        key_oven12 = types.InlineKeyboardButton(text='Связаться со специалистом', url='https://t.me/sashakhasanova')
        keyboard.add(key_oven12)
        bot.send_message(call.message.chat.id,'Дополнительное оборудование',reply_markup=keyboard)
    if call.data =='avto_podbor':

        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ove1n = types.InlineKeyboardButton(text='Да',
                                               callback_data='ya')
        keyboard.add(key_ove1n)
        key_ove12n = types.InlineKeyboardButton(text='Нет',
                                               callback_data='noo')
        keyboard.add(key_ove12n)
        bot.send_message(call.message.chat.id,'Хотите, чтобы наш специалист связался с вами\nИ рассказал об условиях?',reply_markup=keyboard)
    if call.data == 'ya':
        bot.send_message(call.message.chat.id,'Благодарим за обращение!\nОжидайте звонка от специалиста')
        device.publish('amk_avtoset1/pozvon','Позвонить')
    if call.data == 'noo':
        keyboard = types.InlineKeyboardMarkup()
        key_oven111111111111 = types.InlineKeyboardButton(text='Вернуться в основное меню', callback_data='v_menu')
        # И добавляем кнопку на экран
        keyboard.add(key_oven111111111111)
        bot.send_message(call.message.chat.id, 'Выберите ', reply_markup=keyboard)
    if call.data =='prod_avto':
        keyboard = types.InlineKeyboardMarkup()
        # По очереди готовим текст и обработчик для каждого знака зодиака
        key_ove1n = types.InlineKeyboardButton(text='Да',
                                               callback_data='ya')
        keyboard.add(key_ove1n)
        key_ove12n = types.InlineKeyboardButton(text='Нет',
                                               callback_data='noo')
        keyboard.add(key_ove12n)
        bot.send_message(call.message.chat.id,'Хотите, чтобы наш специалист связался с вами\nИ рассказал об условиях?',reply_markup=keyboard)
device = Client()

device.username_pw_set("amk_avtoset1", "amk_avtoset1")
device.connect("mqtt.pi40.ru", 1883)

device.on_message = receive_message
device.loop_start()
bot.polling(none_stop=True)
