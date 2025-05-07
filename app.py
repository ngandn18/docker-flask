from flask import Flask
import os

PORT = int(os.environ.get("PORT", 5000))  # Use Render's assigned PORT

app = Flask(__name__)

@app.route("/")
def home():
    return "Docker is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT, debug=True)

