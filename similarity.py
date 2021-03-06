from nltk.corpus import wordnet as wn
from textblob import Word


def get_similarity(sentence):
	sentence_words = sentence.split(" ")
	#sentence_words = ["this", "restaurant", "has", "cheap"]
	categories = ["food", "service","ambiance", "money"]
	categories_score = [0, 0, 0, 0]

	for i in range (0, 4):
		category_synset = wn.synset(categories[i] + '.n.01')
		for word in sentence_words:
			try:
				syn = Word(word)
				word_synset = syn.synsets[0]
				categories_score[i] += category_synset.path_similarity(word_synset)
			except Exception, e:
				pass
		
	print categories_score
	return categories[categories_score.index(max(categories_score))]
