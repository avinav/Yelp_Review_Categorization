from app import app
from flask import render_template, flash, redirect
from review.review_score import get_reviews
from review import reviews_df
from business import get_business_score
import numpy as np
import math
import pickle

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    #bus_id = "vcNAWiLM4dR7D2nwwJ7nCA"
    #bus_id = "mVHrayjG3uZ_RLHkLj-AMg"
    #bus_id = "1qCuOcks5HRv67OHovAVpg"
    bus_id =  "wJr6kSA5dchdgOdwH6dZ2w"
    res = get_reviews(bus_id)
    try:
        cat_score  = get_business_score(res)
        name = np.unique(reviews_df[reviews_df.business_id == bus_id].name)[0]
        print res
        return render_template("index.html",
                               title = "Yelp Review Categorization",
                               cat_score = cat_score,
                               res = res,
                               name = name)
    except :
        print "nan",res
        return render_template("index.html",
        title = "Yelp Review Categorization",
        cat_score = {},
        res = [],
        name = " ")


@app.route('/all_live', methods = ['GET', 'POST'])
def all_restaurants():
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
    return render_template("all_restaurants.html",
                            title = "Yelp Review Categorization",
                            data = data)

@app.route('/all', methods = ['GET', 'POST'])
def all_business():
    data = pickle.load(open('data.p','r'))
    return render_template("all_restaurants.html",
                            title = "Yelp Review Categorization",
                            data = data)

