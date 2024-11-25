from confluent_kafka import Consumer, KafkaError

def main():
    consumer_config = {
        'bootstrap.servers': 'kafka:9092',  # Use kafka service name for internal communication
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(consumer_config)
    consumer.subscribe(['user-login'])

    print("Consuming messages from topic 'user-login':\n")

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(f"Error: {msg.error()}")
                    break
            print(f"Received message: {msg.value().decode('utf-8')}")
    except KeyboardInterrupt:
        print("\nExiting consumer...")
    finally:
        consumer.close()

if __name__ == '__main__':
    main()
