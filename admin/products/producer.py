import pika

params = pika.URLParameters(
    'amqps://hawybpsh:EFaiLvO0_Wuq0uBGcan5xRHQNTHH2QrN@cougar.rmq.cloudamqp.com/hawybpsh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')
