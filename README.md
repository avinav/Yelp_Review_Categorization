# Yelp_Review_Categorization
Categorizing Yelp text-reviews into ratings
(This was done in the Google DevFest Buffalo 2015 (24 hours), starting from the idea to deployment in aws)

We try to understand the sentiments and various topics in reviews for Yelp businesses. We propose that this data, a feedback rating in various facets of business, will greatly help them to understand customer response. 

We provide simple ratings, 0 to 5 star for Restaurants in four categories: 'Food', 'Service', 'Value for money' and 'Ambience'. The dataset is made available publicly by Yelp as their [Dataset Challange](http://www.yelp.com/dataset_challenge). 

How we did it? - Natural Language Processing
We extract each sentence from each review and categorize it in one of the categories by doing semantic similarity based on WordNet synsets. We then compute sentiment polarity of the sentence. We have (Category, sentiment polarity) pairs for each sentence in the review, which aggregated (each sentence, each review) to give overall category ratings. 
We also tried to be more precise, extracting phrases in a sentence. For instance - the sentence: "The pizza is was really awesome, but had to wait a lot.", talks about two categories: 'Food' and 'Service' with opposing sentiments). We used Stanford Parser for this extraction, but have currently dropped the idea because of the computation time.
Various optimzations are done to make the system efficient. 

We had an inexhaustible ideas for increasing accuracy and improving results: using the review rating provided by yelp, user profile, different similarity measures,  trying out topic modeling (LDA), Supervised learning... Due to time-constraints of a hackathon we could not explore everything, but this is an ongoing project, with quite a many applications such as summarization. 
