from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):
    # Get sentiment score
    sentiment_score = analyzer.polarity_scores(text)
    # Return compound score
    return sentiment_score["compound"]


def send_message1(message):
    sentiment_score = analyze_sentiment(message)
    depression_flag = sentiment_score < -0.5
    return depression_flag


print(send_message1("I lost my friend in car accident tragedy"))
