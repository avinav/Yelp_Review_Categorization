from app import app
from flask import render_template, flash, redirect
from review.review_score import get_reviews

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
    bus_id = "vcNAWiLM4dR7D2nwwJ7nCA"
    res = get_reviews(bus_id)
    print res
    return render_template("index.html",
                           title = "Yelp Review Categorization",
                           res = res)

