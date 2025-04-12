from flask import Flask, jsonify
import random
import threading
import json
import time
from datetime import datetime

app = Flask(__name__)
emojis = ['🏏', '🏆', '🎉', '🔥', '👏', '🙌', '❤️', '😢', '🤯', '😤']


output_file_path = 'emojis.json'


def generate_emojis():
    user_ids = [f"user_{i}" for i in range(1, 6)] 
    
    while True:
        emoji_data = []
        
        for user_id in user_ids:
            # Generate exactly 250 emoji entries per user
            user_emoji_count = 250
            for _ in range(user_emoji_count):
                random_emoji = random.choice(emojis)
                timestamp = datetime.now().isoformat()
                emoji_data.append({
                    "user_id": user_id,
                    "emoji_type": random_emoji,
                    "timestamp": timestamp
                })
        
        with open(output_file_path, 'w') as f:
            json.dump(emoji_data, f, ensure_ascii=False, indent=2)

        print("Generated and saved 1250 emojis for 5 users.")
        time.sleep(5) 

@app.route('/start', methods=['POST'])
def start_generating():
    thread = threading.Thread(target=generate_emojis)
    thread.start()
    return jsonify({"message": "Started generating emojis for 5 users."}), 200

if __name__ == '__main__':
    app.run(port=5002)

