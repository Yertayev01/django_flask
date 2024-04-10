import pika, json

params = pika.URLParameters('amqps://glgsjouo:zfKMulkWKcOksY5iM1DjWI0d3R08WwhT@cougar.rmq.cloudamqp.com/glgsjouo')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)