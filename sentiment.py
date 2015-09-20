import nltk
from textblob import TextBlob


def get_sentiment(text):
    normalization_constant = 10;
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    normalized_polarity = (polarity + 1)/2 * normalization_constant
    print polarity
    return normalized_polarity

example = "I'm fucking happy"
print get_sentiment(example)

# print nltk.pos_tag_sents(blob.sentences)
