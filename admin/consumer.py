import pika

params = pika.URLParameters(
    'amqps://hawybpsh:EFaiLvO0_Wuq0uBGcan5xRHQNTHH2QrN@cougar.rmq.cloudamqp.com/hawybpsh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')


def callback(ch, method, properties, body):
    print('receive in admin')
    print(body)


channel.basic_consume(
    queue="admin", on_message_callback=callback, auto_ack=True)

print('Start Consuming')

channel.start_consuming()

channel.close()
