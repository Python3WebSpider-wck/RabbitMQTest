import pika

QUEUE_NAME = 'scrape'
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.cuiqingcai.com', port=5672, credentials=credentials))
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello')


def callback(ch, method, properties, body):
    # print(" [x] Received %r" % body)
    print(f" [x] Received {body}")

channel.basic_consume(queue=QUEUE_NAME,
                      auto_ack=True,
                      on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
