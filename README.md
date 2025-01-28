# apache-kafka-101

Sample Python producer and consumer based on the Confluent Developer [Apache Kafka 101](https://developer.confluent.io/courses/apache-kafka/events/) course

## The producer

The producer `producer.py` produces a stream of quotes from Shakespearean classics to the Kafka topic `poems` or another Kafka topic of your choice.

### Environment variables

| Name | Required | Example or default |
| --- | --- | --- |
| `BOOTSTRAP_SERVERS` | Y | `kafka:9092` |
| `SASL_USERNAME` | Y | Confluent API key |
| `SASL_PASSWORD` | Y | Confluent API secret |
| `TOPIC` | - | `poems` |

### Usage

The Kafka cluster must support SASL authentication. The most convenient method to stand up Kafka with SASL authentication enabled is via [Confluent Cloud](https://confluent.cloud/) - sign up for an account and get USD$400 in free credits.

```bash
python producer.py
```

Press `Ctrl+C` to stop the producer.

## License

[Apache 2.0](./LICENSE)
