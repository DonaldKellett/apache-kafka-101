# apache-kafka-101

Sample Python producer and consumer based on the Confluent Developer [Apache Kafka 101](https://developer.confluent.io/courses/apache-kafka/events/) course

## Prerequisites

You'll need:

1. Python and Pip installed - we recommend [pyenv](https://github.com/pyenv/pyenv) for managing your Python installations
1. A Kafka cluster with SASL authentication enabled - get started with Kafka in no time with [Confluent Cloud](https://confluent.cloud/) and receive USD$400 in free credit

## Getting started

Fork and clone this repository and make it your working directory.

Now install the Pip dependencies:

```bash
pip install -r requirements.txt
```

### The producer

The producer `producer.py` produces a stream of quotes from Shakespearean classics to the Kafka topic `poems` or another Kafka topic of your choice.

#### Environment variables

| Name | Required | Example or default |
| --- | --- | --- |
| `BOOTSTRAP_SERVERS` | Y | `kafka:9092` |
| `SASL_USERNAME` | Y | Confluent API key |
| `SASL_PASSWORD` | Y | Confluent API secret |
| `TOPIC` | - | `poems` |

#### Usage

```bash
python producer.py
```

Press `Ctrl+C` to stop the producer.

### The consumer

The consumer consumes messages from the Kafka topic `poems` or another Kafka topic of your choice.

#### Environment variables

| Name | Required | Example or default |
| --- | --- | --- |
| `BOOTSTRAP_SERVERS` | Y | `kafka:9092` |
| `SASL_USERNAME` | Y | Confluent API key |
| `SASL_PASSWORD` | Y | Confluent API secret |
| `TOPIC` | - | `poems` |
| `GROUP_ID` | - | `python_kafka101_group_1` |

#### Usage

```bash
python consumer.py
```

Press `Ctrl+C` to stop the consumer.

## License

[Apache 2.0](./LICENSE)
