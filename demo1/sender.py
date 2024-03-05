import pika

QUEUE_NAME = 'scrape'
# credentials = pika.PlainCredentials('user', 'yqN8jqo9x8')
# connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbitmq.cuiqingcai.com', port=5672, credentials=credentials))
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
