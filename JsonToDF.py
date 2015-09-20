import pandas as pd
import json
from pandas.io.json import json_normalize

#with open('/home/zstring/Dropbox/UB/GDG/yelp_dataset_challenge_academic_dataset/smalldataset') as data_file:
#	data = json.load(data_file)


#data_norm= json_normalize(data)

#df = pd.DataFrame(data_norm)


#file = '/home/zstring/Dropbox/UB/GDG/yelp_dataset_challenge_academic_dataset/smalldataset'
def get_data(count):

    #path = '/home/avinav/Dropbox/git/Yelp/yelp_dataset_challenge_academic_dataset'
    path = "/home/castamere/Downloads/yelp_dataset_challenge_academic_dataset"

    file = path + "/yelp_academic_dataset_business.json"
    df = None
    count = 0
    TOTAL_COUNT = count
    with open(file) as f:
        for line in f:
            while True:
                try:
                	#print "%%%% lines",  line
                    jfile = json.loads(line)
                    break
                except ValueError:
                    # Not yet a complete JSON value
                    line += next(f)
                    #print "@#@@@@@@ after, ", line
            data_norm = json_normalize(jfile)
            #print "converting to df", data_norm
            if df is None:
                #print "df is None"
                df = pd.DataFrame(data_norm[['business_id','categories', 'name']])  
            else:
                #print "df has something"
                df = df.append(pd.DataFrame(data_norm[['business_id','categories', 'name']]))
            #print "Shape, ", df.shape
            count = count + 1
            if count > 100:
                break
    df['restaurant'] = ['Restaurants' in category for category in df.categories]
    
    file = path + "/yelp_academic_dataset_review.json"
    df_review = None
    count = 0
    with open(file) as f:
        for line in f:
            while True:
                try:
                    #print "%%%% lines",  line
                    jfile = json.loads(line)
                    break
                except ValueError:
                    # Not yet a complete JSON value
                    line += next(f)
                    #print "@#@@@@@@ after, ", line
            data_norm = json_normalize(jfile)
            #print "converting to df", data_norm
            if df_review is None:
                  #print "df is None"
                  df_review = pd.DataFrame(data_norm)  
            else:
                #print "df has something"
                df_review = df_review.append(pd.DataFrame(data_norm))
            #print "Shape, ", df.shape
            count = count + 1
            if count > 100:
                break
    
    df = pd.merge(df_review, df, on='business_id', how='outer')
    
    return df