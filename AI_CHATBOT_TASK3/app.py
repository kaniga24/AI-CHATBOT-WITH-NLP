from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    msg = request.json["message"].lower()

    if "hello" in msg or "hi" in msg:
        reply = "Hello! How can I help you?"
    elif "name" in msg:
        reply = "I am an AI Chatbot 🤖"
    elif "bye" in msg:
        reply = "Goodbye! Have a nice day 😊"
    else:
        reply = "Sorry, I didn't understand. Please try something else."

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
