
from urllib2 import Request, urlopen
import pandas as pd
import json
from pandas.io.json import json_normalize
from io import StringIO

#with open('/home/zstring/Dropbox/UB/GDG/yelp_dataset_challenge_academic_dataset/smalldataset') as data_file:
#	data = json.load(data_file)


#data_norm= json_normalize(data)

#df = pd.DataFrame(data_norm)


#file = '/home/zstring/Dropbox/UB/GDG/yelp_dataset_challenge_academic_dataset/smalldataset'
file = '/home/zstring/Dropbox/UB/GDG/yelp_dataset_challenge_academic_dataset/yelp_academic_dataset_review.json'
df = None
count = 0
TOTAL_COUNT = 100
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
      		df = pd.DataFrame(data_norm)  
        else:
        	#print "df has something"
        	df = df.append(pd.DataFrame(data_norm))
        #print "Shape, ", df.shape
        count = count + 1
    	if count > 100:
    		break



df.shape