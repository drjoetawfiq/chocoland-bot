
from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def verify():
    # عملية التحقق من Webhook - تطلبها Meta
    VERIFY_TOKEN = "chocoland_token"
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.verify_token") == VERIFY_TOKEN:
        return request.args.get("hub.challenge"), 200
    return "Verification token mismatch", 403

@app.route('/', methods=['POST'])
def webhook():
    data = request.json
    print("📥 تم استقبال تعليق جديد:", data)
    return "تم الاستلام", 200

if __name__ == '__main__':
    app.run(debug=True)
