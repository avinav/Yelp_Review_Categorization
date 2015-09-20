import similarity as sim
import sentiment as senti
from reviewToSentences import reviews_to_sentences
import collections
import operator
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def get_business_score(reviews, id):
    sentences = reviews_to_sentences(reviews)
    final_cat = {"food":0, "service":0,"ambiance":0, "money":0}
    cat_count = {"food":1, "service":1, "ambiance":1, "money":1}
    items_food = {}
    items_service = {}
    items_amb = {}
    items_money = {}
    for sent in sentences:
        sentr = senti.get_sentiment(sent)
        if sentr != 0.5:
            cat = sim.get_similarity(sent)
            final_cat[cat] = sentr + final_cat[cat]
            cat_count[cat] = 1 + cat_count[cat]        
            if cat == 'food':
                items_food[sent] = sentr
            elif cat == 'service':
                items_service[sent] = sentr
            elif cat == 'ambiance':
                items_amb[sent] = sentr
            elif cat == 'money':
                items_money[sent] = sentr
            
    for key in final_cat.keys():
            final_cat[key] = final_cat[key] / (1.0 * cat_count[key])
    
    total_sen = 5
    new_f = dict(sorted(items_food.iteritems(), key=operator.itemgetter(1), reverse=True)[:total_sen])
    new_s = dict(sorted(items_service.iteritems(), key=operator.itemgetter(1), reverse=True)[:total_sen])
    new_a = dict(sorted(items_amb.iteritems(), key=operator.itemgetter(1), reverse=True)[:total_sen])
    new_m = dict(sorted(items_money.iteritems(), key=operator.itemgetter(1), reverse=True)[:total_sen])
    
    f = " ".join(new_f.keys())
    s = " ".join(new_s.keys())
    a = " ".join(new_a.keys())
    m = " ".join(new_m.keys())
    write_image(f, s, a, m, id)

    return final_cat


def write_image(new_f, new_s, new_a, new_m, id):
    
    
    w_image(new_f,'app/static/'+ id+'_f.png')
    w_image(new_s,'app/static/'+ id+'_s.png')
    w_image(new_a,'app/static/'+  id+'_a.png')
    w_image(new_m,'app/static/'+  id+'_m.png')

def w_image(text, name):

        
    plt.axis("off")

    # take relative word frequencies into account, lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.imshow(wordcloud)
    plt.savefig(name)
    

