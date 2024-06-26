from flask import Flask, request, jsonify
from gradio_client import Client
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
# client = Client("ShynBui/Vector_db_v2")
client = Client("ShynBui/Vector_db_v3")

@app.route('/')
def index():
    return 'Welcome to backend botchat2024 Lê Văn Chiến!'
@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    result = client.predict(
		quote = data['quote'],	# str  in 'quote' Textbox component
		history = data['history'],	# str  in 'history' Textbox component
		api_name="/predict"
    )
    if result:
        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

if __name__ == "__main__":
    # Use the PORT environment variable provided by Heroku
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port, host='0.0.0.0')
