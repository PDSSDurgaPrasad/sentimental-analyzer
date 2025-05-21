from textblob import TextBlob

def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity

    if polarity > 0.5:
        return ("Positive", "High Priority")
    elif 0 < polarity <= 0.5:
        return ("Positive", "Medium Priority")
    elif polarity == 0:
        return ("Neutral", "Low Priority")
    elif -0.5 <= polarity < 0:
        return ("Negative", "Medium Priority")
    else:
        return ("Negative", "High Priority")

