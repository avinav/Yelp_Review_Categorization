import numpy as np
import pandas as pd
from JsonToDF import get_data
import pickle
import os

count = 2
reviews_df = get_data(count)
if os.path.isfile('data.p'):
    data = pickle.load(open('data.p','r'))
