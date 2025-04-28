"""Model module for sentiment predictione r."""


def predict_sentiment(text):
    """Predict the sentiment of a given text as positive,
    negative, or neutral."""
    if not text:
        return "neutral"

    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"

    return "neutral"

