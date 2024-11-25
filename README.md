Kafka Consumer and Producer Assignment
Questions and Answers
1. What are the key components required to set up the Kafka environment?
To set up the Kafka environment, the following components are required:
- Zookeeper: Manages and coordinates the Kafka brokers.
- Kafka Broker: Responsible for storing and serving messages.
- Topics: Logical storage units in Kafka for publishing and consuming messages.
- Producer: Publishes messages to a Kafka topic.
- Consumer: Subscribes to a topic to read messages.
- Docker Compose: Simplifies the setup process using a predefined YAML configuration.
2. What are the steps to consume and process messages?
Steps to consume and process messages:
1. Configure the Kafka consumer with the appropriate settings (e.g., `bootstrap.servers`, `group.id`).
2. Subscribe to the desired topic (e.g., `user-login`).
3. Use a poll loop to fetch messages from the topic.
4. Process each message (e.g., masking sensitive data, adding metadata).
5. Optionally, publish the processed message to a new topic.
3. How do you handle errors in Kafka message consumption?
Error handling in Kafka message consumption includes:
- Checking for errors in each polled message using `msg.error()`.
- Differentiating between recoverable errors (e.g., `KafkaError._PARTITION_EOF`) and critical errors.
- Logging errors for debugging and monitoring.
- Gracefully shutting down the consumer in case of fatal errors.
4. How do you ensure the processed messages are published to another topic?
To publish processed messages to another topic:
1. Configure a Kafka producer with the appropriate settings (e.g., `bootstrap.servers`).
2. After processing a message, use the `producer.produce()` method to send it to the new topic (e.g., `processed-user-login`).
3. Use `producer.flush()` to ensure all messages are sent before shutting down.
5. How do you validate the processed messages?
To validate the processed messages:
- Consume messages from the `processed-user-login` topic using a Kafka console consumer or another consumer script.
- Verify the message format, schema, and content against the expected output.
- Use logging to confirm successful processing.
6. What changes did you make in the script, and why?
Changes made in the script include:
- Updated `bootstrap.servers` to `localhost:29092` to match the Dockerized Kafka setup.
- Added a `process_message` function to mask IP addresses and add a `processed` flag for message transformation.
- Configured a producer to publish processed messages to the `processed-user-login` topic.
Step-by-Step Execution Process
1. Install Python dependencies:
Command: `pip install confluent-kafka`
Description: Installed the Confluent Kafka library to interact with Kafka in Python.
2. Upgrade pip to the latest version:
Command: `python -m pip install --upgrade pip`
Description: Upgraded pip to avoid compatibility issues with the dependencies.
3. Verify Docker containers:
Command: `docker ps`
Description: Verified that Zookeeper, Kafka, and the producer containers were running.
4. Create the `kafka_consumer.py` script:
Added the script to consume messages from the `user-login` topic, process them by masking IP addresses, and publish them to a new topic `processed-user-login`.
5. Modify bootstrap servers in the script:
Updated `bootstrap.servers` to `localhost:29092` to connect to the Kafka container running on Docker.
6. Run the consumer script:
Command: `python kafka_consumer.py`
Description: Executed the Python consumer script to process and print Kafka messages.
7. Verify processed messages:
Observed transformed messages printed in the console with IP addresses masked and a `processed` flag added.
8. Debug errors during execution:
Resolved issues such as 'No such host is known' by ensuring correct `bootstrap. servers` and that Kafka containers were running.
