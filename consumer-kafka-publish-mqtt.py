from kafka import KafkaConsumer
import json
import paho.mqtt.client as paho

# configuração do MQTT
broker = "test.mosquitto.org"
port = 1883


def on_publish(client, userdata, result):
    pass


client = paho.Client("stocksb3-mqtt")
client.on_publish = on_publish
client.connect(broker, port)

# configuração do kafka
brokers = ['localhost:9092']
topic = 'stock.b3.datas'
consumer = KafkaConsumer(topic, group_id='group1', bootstrap_servers=brokers)

for message in consumer:
    text = json.loads(message.value.decode('utf-8'))
    client.publish("stock.b3.datas", str(text))
    print(text)
