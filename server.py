import os
from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# فایل ذخیره پیام‌ها
FILE_PATH = "messages.txt"

@app.route("/")
def index():
    return "Server is running ✅"

@app.route("/save", methods=["POST"])
def save_message():
    data = request.get_json(silent=True)
    
    if not data or "text" not in data:
        return jsonify({"error": "فیلد text ارسال نشد"}), 400
    
    text = data["text"]
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # نوشتن در فایل (حالت append یعنی اضافه شدن به انتهای فایل)
    with open(FILE_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")
    
    return jsonify({"status": "saved", "text": text})

@app.route("/messages", methods=["GET"])
def get_messages():
    """برای دیدن همه پیام‌های ذخیره‌شده"""
    if not os.path.exists(FILE_PATH):
        return jsonify({"messages": []})
    
    with open(FILE_PATH, "r", encoding="utf-8") as f:
        content = f.read()
    
    return jsonify({"messages": content})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)