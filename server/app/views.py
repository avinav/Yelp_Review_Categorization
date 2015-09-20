from app import app
from flask import render_template, flash, redirect
from review.review_score import get_reviews
from review import reviews_df
from business import get_business_score
import numpy as np

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    #bus_id = "vcNAWiLM4dR7D2nwwJ7nCA"
    bus_id = "mVHrayjG3uZ_RLHkLj-AMg"
    res = get_reviews(bus_id)
    cat_score  = get_business_score(res)
    name = np.unique(reviews_df[reviews_df.business_id == bus_id].name)[0]
    print res
    return render_template("index.html",
                           title = "Yelp Review Categorization",
                           cat_score = cat_score,
                           res = res,
                           name = name)
i
@app.route('/all',method = ['GET', 'POST'])
def all_restaurants():
    id_list = np.unique(reviews_df.id)
    data = []
    for _id in id_list:
        _dict = {}
        _dict['id'] = _id
        _dict['name'] = np.unique(reviews_df[reviews_df.business_id == _id])[0].name
        reviews = get_reviews(_id)
        cat_score = get_business_score(reviews)
        _dict['cat_score'] = cat_score
        data.append(_dict)
    return render_template("all_retaurants",
                            title = "Yelp Review Categorization",
                            data = data)

