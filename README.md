# EmoStream: Concurrent Emoji Broadcast over Event-Driven Architecture

## Project Overview

Emojis reflect the dynamic sentiments of fans in real-time. When Virat is batting, everyone’s hoping for boundaries with every ball; when he’s on the field, they’re cheering for wickets. Capturing these user-generated signals as they flow in, distilling them into an emoji swarm that mirrors the crowd’s mood, and displaying these shifting emotions live is a major challenge—especially with billions of emoji reactions anticipated over the tournament.

## Goal

The goal of this project was to design and implement a scalable system that enhances the viewer experience on platforms like Hotstar by capturing and processing billions of user-generated emojis in real-time during live sporting events. This was achieved by creating a horizontally scalable architecture using Kafka for data streaming and Spark for real-time data processing. The system ensures high concurrency and low latency, delivering seamless user interactions.

## Architecture

### Key Components

1. **API Endpoint and Data Collection**
   - A Flask-based **API endpoint** was created to receive **POST** requests from users, containing the emoji data (User ID, Emoji type, Timestamp).
   - Each emoji data entry is **asynchronously** written to a Kafka producer.
   
2. **Kafka Producer and Data Streaming**
   - The emoji data is pushed to Kafka as a message queue, with a **flush interval** of 500 milliseconds to ensure real-time data transmission to the Kafka broker.
   
3. **Real-Time Data Processing with Spark**
   - A **Spark Streaming** job consumes the emoji data from Kafka in **micro-batches**. 
   - The micro-batches are processed in intervals of 2 seconds, with an aggregation algorithm that reduces 1000 or fewer emojis of the same type to a single representative emoji.

4. **Pub-Sub Architecture for Scalability**
   - A **Publisher-Subscriber** model is implemented to handle high concurrency. 
   - Multiple **Kafka clusters** are established, each with its own **publisher** and multiple **subscribers**.
   - The main publisher receives aggregated data from Spark and forwards it to the cluster publishers.
   - Subscribers handle the distribution of messages to clients, ensuring real-time updates to users.

5. **Client Registration and Seamless Connection Management**
   - Clients can register with the subscribers to receive real-time emoji updates.
   - The system supports dynamic client registration and removal, ensuring no interruptions in the live data flow.


- **API Endpoint**: A Flask API that accepts emoji data from users and sends it asynchronously to the Kafka producer.
- **Kafka Producer**: The producer writes emoji data to Kafka with a flush interval of 0.5 seconds.
- **Spark Streaming Job**: A job that processes the emoji data in 2-second intervals, applying the aggregation logic to reduce emojis.
- **Publisher-Subscriber Architecture**: A robust architecture that scales to handle large numbers of clients with multiple clusters, each with a cluster publisher and several subscribers.
- **Real-Time Data Delivery**: The aggregated emoji data is delivered back to clients in real time, with seamless handling of client connections.

## Testing

- **Unit Testing**: Tests were created for the API endpoints to ensure they could handle thousands of emoji requests per second.
- **Load Testing**: The system was stress-tested to ensure it could handle high concurrency with thousands of concurrent clients sending emoji data.
- **Scalability Testing**: The Pub-Sub model was tested to ensure real-time data delivery to users, even under high load.

## Demo

The system was demonstrated with multiple clients sending emoji data to the API endpoint. Kafka producer asynchronously received and wrote emoji data to the Kafka broker, and the Kafka consumer processed and aggregated the data using Spark Streaming. The aggregated data was then distributed to clients through the Pub-Sub architecture, ensuring that all clients received real-time emoji updates.

