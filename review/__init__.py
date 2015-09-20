import numpy as np
import pandas as pd
from JsonToDF import get_data
import pickle
import os

count = 1000
reviews_df = get_data(count)
