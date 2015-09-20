import numpy as np
import pandas as pd
from JsonToDF import get_data
from review import reviews_df
from review.review_score import get_reviews
from business import get_business_score
import pickle

count = 2
df = get_data(count)
id_list = np.unique(reviews_df.business_id)
data = []
for _id in id_list:
    _dict = {}
    _dict['id'] = _id
    _dict['name'] = np.unique(reviews_df[reviews_df.business_id == _id].name)[0]
    print _id
    reviews = get_reviews(_id)
    try:
        cat_score = get_business_score(reviews)
        _dict['cat_score'] = cat_score
        data.append(_dict)
    except:
        pass
pickle.dump(data,open('data.p','w'))

