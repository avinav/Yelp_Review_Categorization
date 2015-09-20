import nltk
from textblob import TextBlob

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = './stanfordjars/stanford-parser.jar'
os.environ['STANFORD_MODELS'] = './stanfordjars/stanford-parser-3.5.2-models.jar'

nltk.internals.config_java(options='-xmx2G')

parser = stanford.StanfordParser(model_path="./stanfordjars/englishPCFG.ser.gz")


def single_review_to_sentences(review_text):
    list_iterator = parser.raw_parse(review_text)

    sentence_list = []
    flag = True

    for tree in list_iterator:
        checklist = ['S', 'FRAG', 'SBAR', 'SBARQ']
        sentence_list = [" ".join(i.leaves()) for i in tree.subtrees() if i.label() in checklist]
        if len(sentence_list) > 1:
            del sentence_list[0]

        # for subtree in tree.subtrees():
        #     if subtree.label() == 'S' or subtree.label() == 'FRAG':
        #         if not flag:
        #             current_sentence = " ".join(subtree.flatten().leaves())
        #             sentence_list.append(current_sentence)
        #         flag = False
        #tree.draw()

    return sentence_list


def reviews_to_sentences(reviews):
    all_sentences = []
    for review in reviews:
        review_blob = TextBlob(review)
        review_sentences = review_blob.sentences
        for review_sentence in review_sentences:
            result = review_sentence.raw
            # result = single_review_to_sentences(review_sentence.raw)
            all_sentences.append(result)
    return all_sentences

# print reviews_to_sentences(("I don't know what Dr. Goldberg was like before moving to Arizona , but let me tell you , STAY AWAY from this doctor and this office . I was going to Dr. Johnson before he left and Goldberg took over when Johnson left . He is not a caring doctor . He is only interested in the co-pay and having you come in for medication refills every month . He will not give refills and could less about patients 's financial situations . Trying to get your 90 days mail away pharmacy prescriptions through this guy is a joke . And to make matters even worse , his office staff is incompetent . 90 % of the time when you call the office , they 'll put you through to a voice mail , that NO ONE ever answers or returns your call . Both my adult children and husband have decided to leave this practice after experiencing such frustration . The entire office has an attitude like they are doing you a favor . Give me a break ! Stay away from this doc and the practice . You deserve better and they will not be there when you really need them . I have never felt compelled to write a bad review about anyone until I met this pathetic excuse for a doctor who is all about the money .", "Something else"))
