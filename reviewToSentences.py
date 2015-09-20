import nltk
from textblob import TextBlob

import os
from nltk.parse import stanford
os.environ['STANFORD_PARSER'] = './stanford-parser.jar'
os.environ['STANFORD_MODELS'] = './stanford-parser-3.5.2-models.jar'

parser = stanford.StanfordParser(model_path="./englishPCFG.ser.gz")


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
        result = single_review_to_sentences(review)
        all_sentences.extend(result)
    return all_sentences

