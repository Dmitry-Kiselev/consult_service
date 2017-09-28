import pika


class ConsumerException(Exception):
    pass


class Consumer:
    def __init__(self, queue_name=None):
        self.connection = pika.BlockingConnection()
        self.channel = self.connection.channel()
        self.queue_name = queue_name

    def consume(self):
        if self.queue_name is None:
            raise ConsumerException('queue_name is required')
        self.create_queue()  # create if not exists
        self.channel.basic_consume(self.return_message, self.queue_name)
        try:
            self.channel.start_consuming()
        except KeyboardInterrupt:
            self.stop_consuming()

    def create_queue(self):
        self.channel.queue_declare(queue=self.queue_name)

    def stop_consuming(self):
        self.channel.stop_consuming()
        self.connection.close()

    def return_message(self, _channel, _method_frame, _header_frame, body):
        self.stop_consuming()
        return body
