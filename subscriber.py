from paho.mqtt.client import Client
message = ''
def on_message(client, userdata, msg_payload):
    global message
    message = msg_payload.payload.decode()
    print(message)
hostname = "mqtt.pi40.ru"
port = 1883
username = "client_sasha"
password = "dsr4mn"
clientID = "sahgghshhh7675465a1"
client = Client(clientID)
client.username_pw_set(username, password)
client.connect(hostname, port)
client.subscribe("client_sasha/test")
client.message_callback_add("client_sasha/test", on_message)
client.loop_forever()