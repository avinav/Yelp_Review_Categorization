from app import app
from flask import render_template, flash, redirect
from review.review_score import get_reviews
from review import reviews_df
from business import get_business_score
import numpy as np

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    bus_id = "vcNAWiLM4dR7D2nwwJ7nCA"
    res = get_reviews(bus_id)
    cat_score  = get_business_score(res)
    name = np.unique(reviews_df[reviews_df.business_id == bus_id].name)[0]
    print res
    return render_template("index.html",
                           title = "Yelp Review Categorization",
                           cat_score = cat_score,
                           res = res,
                           name = name)

