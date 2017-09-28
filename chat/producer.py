import pika


class Producer:
    def __init__(self, queue_name=None):
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        self.queue_name = queue_name

    def create_queue(self):
        self.channel.queue_declare(queue=self.queue_name)

    def send(self, message):
        message = str(message)
        self.create_queue()
        self.channel.publish(exchange='',
                             routing_key=self.queue_name,
                             body=message)
