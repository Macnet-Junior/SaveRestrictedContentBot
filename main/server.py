# HTTP Server to keep bot alive on free hosting platforms (Render, Railway, etc)
import threading
from flask import Flask
from decouple import config

app = Flask(__name__)
PORT = config("PORT", default=8080, cast=int)

@app.route('/')
def home():
    return "Bot is running!", 200

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

def run_server():
    """Run Flask server in background"""
    app.run(host='0.0.0.0', port=PORT, debug=False)

def start_server():
    """Start server in daemon thread"""
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    print(f"Server started on port {PORT}")
