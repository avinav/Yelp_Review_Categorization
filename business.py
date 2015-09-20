import similarity as sim
import sentiment as senti
from reviewToSentences import reviews_to_sentences
def get_business_score(reviews):
    sentences = reviews_to_sentences(reviews)
    final_cat = {"food":0, "service":0, "hygiene":0, "ambiance":0, "money":0}
    cat_count = {"food":1, "service":1, "hygiene":1, "ambiance":1, "money":1}
    for sent in sentences:
        cat = sim.get_similarity(sent)
        sent = senti.get_sentiment(sent)
        if sent != 0.5:
		final_cat[cat] = sent + final_cat[cat]
        	cat_count[cat] = 1 + cat_count[cat]        
    for key in final_cat.keys():
            final_cat[key] = final_cat[key] / (1.0 * cat_count[key])
    
    return final_cat
print "e"
#print sim.get_similarity("the pizzas are good")
