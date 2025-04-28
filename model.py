# this is a simple sentiment analysis model that uses keyword matching to
# predict the sentiment of a given text.
def predict_sentiment(text):
    if not text:
        return "neutral"

    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"

# this is a super commentary for test my workflow
# this is a super commentary for test my workflow