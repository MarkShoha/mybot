from paho.mqtt.client import Client
import telebot



mqtt_message1 = ''
bot = telebot.TeleBot('5475601416:AAG4DveKGnq1ajhbDOJTi9CPOL_UCFRXHNQ')
#5423912192:AAGJoP0B7lor-9cHkTx1SdXdVYyFtMfYjVE+7 950 192 4621
from telebot import types
import random




mqtt_message1=''
mqtt_message11=''
def gg1(device, userdata, message):
    global mqtt_message1
    mqtt_message1= message.payload.decode()
    print(mqtt_message1)
    bot.send_message(id, 'номер телефона: ' + mqtt_message1)

def gg11(device, userdata, message):
    global mqtt_message11
    mqtt_message11 = message.payload.decode()
    print(mqtt_message11)
    bot.send_message(id, 'услуга: ' + mqtt_message11)

@bot.message_handler(commands=["start"])
def start(m):
    global id
    id = m.chat.id
    bot.send_message(m.chat.id,'iubcwwerre')

device = Client('ywh4783738')

device.username_pw_set("amk_avtoset1", "amk_avtoset1")
device.connect("mqtt.pi40.ru", 1883)
device.subscribe("amk_avtoset1/phones")
device.subscribe("amk_avtoset1/uslugi")
device.message_callback_add("amk_avtoset1/phones",gg1)
device.message_callback_add("amk_avtoset1/uslugi",gg11)
device.on_message = gg11
device.loop_start()
bot.polling()