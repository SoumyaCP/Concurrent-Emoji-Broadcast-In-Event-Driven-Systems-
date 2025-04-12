from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': 'localhost:9092'  
}
producer = Producer(conf)
input_file_path = '/home/soumya_cp/Downloads/bd_pro/emojis.json'


def send_to_kafka():
    # Open the file and load the data once
    with open(input_file_path, 'r') as f:
        data = json.load(f)
        for entry in data:
            producer.produce('emoji-topic', key=entry['user_id'], value=json.dumps(entry))
            producer.flush()  

    print("Sent batch of 1250 emojis to Kafka.")

if __name__ == "__main__":
    print("Starting to send data to Kafka...")
    send_to_kafka()
    print("Finished sending data to Kafka.")

