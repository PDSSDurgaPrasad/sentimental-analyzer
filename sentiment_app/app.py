from flask import Flask, render_template, request
from sentiment import analyze_sentiment

app = Flask(__name__)
history = []

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    priority = None

    if request.method == "POST":
        user_text = request.form["text"]
        sentiment, priority = analyze_sentiment(user_text)
        history.append({
            "text": user_text,
            "sentiment": sentiment,
            "priority": priority
        })

    return render_template("index.html", sentiment=sentiment, priority=priority, history=history[-5:])  # show last 5 entries

if __name__ == "__main__":
    app.run(debug=True)
