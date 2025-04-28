from model import predict_sentiment


# test the predict_sentiment function with a positive text
def test_predict_positive(): 
    assert predict_sentiment("I am happy today") == "positive" 


# test the predict_sentiment function with a negative text
def test_predict_negative():
    assert predict_sentiment("I feel sad") == "negative" 


# test the predict_sentiment function with a neutral text
def test_predict_neutral(): 
    assert predict_sentiment("The sky is blue") == "neutral" 