import random
import uuid  # Import the uuid module
import json
from confluent_kafka import Producer

def generate_message():
    """
    Generate a random message to simulate user login data.
    """
    user_id = str(uuid.uuid4())  # Use uuid4() from the uuid module
    app_version = "2.3.0"
    ip = f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}"
    locale = random.choice(["US", "IN", "CA", "UK", "AU"])
    device_id = str(uuid.uuid4())  # Use uuid4() for device ID
    timestamp = random.randint(1609459200, 1700000000)  # Random timestamp
    device_type = random.choice(["android", "iOS"])

    message = {
        "user_id": user_id,
        "app_version": app_version,
        "ip": ip,
        "locale": locale,
        "device_id": device_id,
        "timestamp": timestamp,
        "device_type": device_type
    }
    return json.dumps(message)

def on_delivery(err, msg):
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

def main():
    producer_config = {
        'bootstrap.servers': 'localhost:9092'
    }

    producer = Producer(producer_config)

    while True:
        message = generate_message()  # Generate a new message
        producer.produce('user-login', message, callback=on_delivery)  # Produce message to Kafka
        producer.poll(0)  # Poll the producer to handle delivery reports
        print(f"Produced message: {message}")

if __name__ == '__main__':
    main()
