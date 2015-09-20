import similarity as sim
import sentiment as senti
from reviewToSentences import reviews_to_sentences
def get_business_score(reviews):
    sentences = reviews_to_sentences(reviews)
    final_cat = {"food":0, "service":0, "hygiene":0, "ambiance":0, "money":0}
    cat_count = {"food":0, "service":0, "hygiene":0, "ambiance":0, "money":0}
    for sent in sentences:
        cat = sim.get_similarity(sent)
        senti = senti.get_sentiment(sent)
        final_cat[cat] = senti + final_cat[cat]
        cat_count[cat] = 1 + cat_count[cat]        
    for key in final_cat.keys():
            final_cat[key] = final_cat[key] / (1.0 * cat_count[key])
    
    return final_cat

#print sim.get_similarity("the pizzas are good")
