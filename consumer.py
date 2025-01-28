from confluent_kafka import Consumer
import os
import sys

def run_consumer(bootstrap_servers, sasl_username, sasl_password, topic, group_id):
    consumer = Consumer({
        'bootstrap.servers': bootstrap_servers,
        'security.protocol': 'SASL_SSL',
        'sasl.mechanism': 'PLAIN',
        'sasl.username': sasl_username,
        'sasl.password': sasl_password,
        'group.id': group_id,
        'auto.offset.reset': 'earliest'
    })
    consumer.subscribe([topic])
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                print("Waiting ...")
            elif msg.error():
                print("ERROR: %s".format(msg.error()), file=sys.stderr)
            else:
                print("Got quote from Shakespearean classic \"%s\":\n\n%s\n" % (msg.key().decode('utf-8'), msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()

if __name__ == '__main__':
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    sasl_username = os.getenv('SASL_USERNAME')
    sasl_password = os.getenv('SASL_PASSWORD')
    topic = os.getenv('TOPIC', 'poems')
    group_id = os.getenv('GROUP_ID', 'python_kafka101_group_1')
    run_consumer(bootstrap_servers, sasl_username, sasl_password, topic, group_id)
