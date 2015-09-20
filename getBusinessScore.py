

def getBusinessScore(reviews):
    sentences = getSentencesFromReviews(reviews)
    final_cat = {'food': 0, 'service': 0}
    cat_count = {'food': 0, 'service': 0}
    for sent in sentences:
        cat = getCategory(sent)
        senti = getSentiment(sent)
        final_cat[cat] = senti + final_cat[cat]
        cat_count[cat] = 1 + cat_count[cat]        
    for key in final_cat.keys():
            final_cat[key] = final_cat[key] / (1.0 * cat_count[key])
    
    return final_cat