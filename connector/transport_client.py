import os
from kafka import KafkaProducer, KafkaConsumer

from topics import connector_topics
from message_distributor import message_distributor

KAFKA_BROKER_ADRESS = os.environ.get('KAFKA_BROKER_ADRESS')

def main():
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='connector_producer',
    )

    consumer = KafkaConsumer(
        bootstrap_servers=KAFKA_BROKER_ADRESS,
        client_id='connector_consumer',
    )
    consumer.subscribe(connector_topics)

    for message in consumer:
        topic, message = message_distributor(message)
        producer.send(topic, value=message.encode())