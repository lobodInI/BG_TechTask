from environs import Env
from pika import ConnectionParameters, BlockingConnection


def get_connection_rabbitmq() -> ConnectionParameters:
    """
    Connection to server RabbitMQ.
    :return: ConnectionParameters
    """
    env = Env()
    env.read_env(".env")

    connection = ConnectionParameters(
        host=env("RABBITMQ_HOST"),
        port=int(env("RABBITMQ_PORT")),
    )

    return connection

def send_message_to_rabbitmq(queue_name: str, message: str) -> None:
    """
    Send message to RabbitMQ about manipulation with strategy.
    :param queue_name: Name of strategy queue
    :param message: Message about manipulation with strategy.
    :return: None
    """
    with BlockingConnection(get_connection_rabbitmq()) as conn:
        with conn.channel() as channel:
            channel.queue_declare(queue=queue_name)
            channel.basic_publish(
                exchange="",
                routing_key=queue_name,
                body=message,
            )
