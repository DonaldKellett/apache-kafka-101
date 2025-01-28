from confluent_kafka import Producer
import os
import random
import sys

def random_shakespearean_quote():
    SHAKESPEAREAN_QUOTES = [
        ('Hamlet', [
            "O, that this too, too solid flesh would melt,\nThaw and resolve itself into a dew!",
            "Neither a borrower nor a lender be,\nFor loan oft loses both itself and friend,\nAnd borrowing dulls the edge of husbandry.",
            "Something is rotten in the state of Denmark."
        ]),
        ('Romeo and Juliet', [
            "A pair of star-crossed lovers take their life.",
            "Abraham: Do you bite your thumb at us, sir?\nSampson: I do bite my thumb, sir.",
            "O Romeo, Romeo, wherefore art thou Romeo?"
        ]),
        ('The Merchant of Venice', [
            "The devil can cite Scripture for his purpose.",
            "I like not fair terms and a villain's mind.",
            "It is a wise father that knows his own child."
        ]),
        ('A Midsummer Night\'s Dream', [
            "The course of true love never did run smooth.",
            "Ill met by moonlight, proud Titania.",
            "What angel wakes me from my flow'ry bed?"
        ]),
        ('Twelfth Night', [
            "If music be the food of love, play on.",
            "I'll do my best\nTo woo your lady. - Yet, a barful strife!\nWhoe'er I woo, myself would be his wife.",
            "Better a witty fool than a foolish wit."
        ]),
        ('Sonnet 18', [
            "Shall I compare theee to a summer's day?\nThou art more lovely and more temperate:\nRough winds do shake the darling buds of May,\nAnd summer's lease hath all to short a date:",
            "Sometime too hot the eye of heaven shines,\nAnd often is his gold complexion dimm'd;\nAnd every fair from fair sometime declines,\nBy chance, or nature's changing course, untrimm'd;",
            "So long as men can breathe, or eyes can see,\nSo long lives this, and this gives life to thee."
        ])
    ]
    work_quotes = random.choice(SHAKESPEAREAN_QUOTES)
    work = work_quotes[0]
    quote = random.choice(work_quotes[1])
    return (work, quote)

def run_producer(bootstrap_servers, sasl_username, sasl_password, topic):
    producer = Producer({
        'bootstrap.servers': bootstrap_servers,
        'sasl.username': sasl_username,
        'sasl.password': sasl_password,
        'security.protocol': 'SASL_SSL',
        'sasl.mechanisms': 'PLAIN',
        'acks': 'all'
    })
    def delivery_report(err, msg):
        if err is not None:
            print('Message delivery failed: {}'.format(err), file=sys.stderr)
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))
    while True:
        producer.poll(0)
        (work, quote) = random_shakespearean_quote()
        producer.produce(topic, value=quote, key=work, callback=delivery_report)
        producer.flush()

if __name__ == '__main__':
    bootstrap_servers = os.getenv('BOOTSTRAP_SERVERS')
    sasl_username = os.getenv('SASL_USERNAME')
    sasl_password = os.getenv('SASL_PASSWORD')
    topic = os.getenv('TOPIC', 'poems')
    run_producer(bootstrap_servers, sasl_username, sasl_password, topic)
