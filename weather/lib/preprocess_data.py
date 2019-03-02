from util.noob import *

import sys
validate_match(r'^3.*', sys.version)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
import tensorflow as tf

from sklearn.preprocessing import StandardScaler

from schema_data import *


# GLOBAL VARIABLES / SETTINGS

pd.set_option( 'display.max_columns', 500 )
pd.set_option( 'display.width', 1000 )

NUM_FEATURES=8


# GET DATA

data = pd.read_csv(
    '../data/original_weather_data.csv',
    sep=',',
    dtype=type_columns_dic
)
data = data[rename_columns_dic]; # extract columns for analysis
data = data.rename( index=str, columns=rename_columns_dic ) # rename columns


# FEATURE ENGINEERING

# convert 'date' column to just month
data.date = replace_in_series( data.date, r'\d*-([a-zA-Z]*)-\d*', '\\1' )
expected = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
validate_lists_equal( data.date.unique(), expected )

print(get_first_row(data))
print(data.shape)
print('success!')
