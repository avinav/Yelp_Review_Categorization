import nltk
from textblob import TextBlob


def get_sentiment(text):
    normalization_constant = 1;
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    normalized_polarity = (polarity + 1.0)/(2.0) * normalization_constant
    print 'polarity', normalized_polarity
    return normalized_polarity

example = "I'm fucking happy"
print get_sentiment(example)
