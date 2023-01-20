import json

from kafka import KafkaConsumer

#configuração do kafka
brokers = ['localhost:9092']
topic = 'stock.b3.datas'

consumer = KafkaConsumer(topic, group_id='group1', bootstrap_servers=brokers)

for message in consumer:
    text = json.loads(message.value.decode('utf-8'))
    print(text)
