import os
import json
from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER_ADRES = os.environ.get('KAFKA_BROKER_ADRES')

def main():
    consumer = KafkaConsumer(
        'test_topic',
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_deserializer=lambda value: json.loads(value.decode())
    )

    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_ADRES,
        value_serializer=lambda value: json.dumps(value).encode()
    )

    for message in consumer:
        producer.send('test_topic2', value=message.value)
        print(message.value)

if __name__ == '__main__':
    main()