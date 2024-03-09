from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)
client = Client("ShynBui/Vector_db")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    # client = Client("ShynBui/Vector_db")
    # result = client.predict(
	# 	data,	# str  in 'quote' Textbox component
	# 	api_name="/predict"
    # )
    result = data 
    if result:

        return jsonify(result), 200
    else:
        return jsonify({"error": "Failed to connect to database"}), 500

if __name__ == "__main__":
    app.run(debug=True)
