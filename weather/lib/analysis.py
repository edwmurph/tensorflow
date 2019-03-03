from util.noob import *

import sys
validate_match(r'^3.*', sys.version)

import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.preprocessing import StandardScaler

from schema_data import *

#
# GLOBAL VARIABLES / SETTINGS
#

pd.set_option( 'display.max_columns', 500 )
pd.set_option( 'display.width', 1000 )
NUM_FEATURES = 11

#
# GET PROCESSED DATA
#

try:
    data = pd.read_csv(
        '../data/processed_weather_data.csv',
        sep=',',
        dtype=type_columns_dic
    )
except:
    raise Exception('\nproblem importing processed data\n')

if data.isnull().values.any():
    raise Exception('some values in dataframe are missing')

for type in data.dtypes:
    if type != 'float64':
        raise Exception('one of the columns is the wrong type')

#
# CREATE TEST AND TRAIN SUBSETS AND SPLIT LABELS
#

msk = np.random.rand(len(data)) < 0.8
train_data = data[msk]
test_data = data[~msk]

train_y = train_data['avg_temp']
train_x = train_data.drop(columns=['avg_temp'])

test_y = test_data['avg_temp']
test_x = test_data.drop(columns=['avg_temp'])

if len(train_x.columns) != NUM_FEATURES or len(test_x.columns) != NUM_FEATURES:
    raise Exception('labels were not removed from features dataframe')

#
# NORMALIZE
#

# we need to normalize the data because the features are on different scales
sc = StandardScaler()
train_x = sc.fit_transform(train_x)
test_x = sc.fit_transform(test_x)

#
# BUILD MODEL
#

model = tf.keras.Sequential([
    # define input layer
    tf.keras.layers.Dense(NUM_FEATURES, activation=tf.nn.relu, input_shape=[NUM_FEATURES]),
    # only have single output dense layer
    tf.keras.layers.Dense(1)
])

model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.RMSprop(0.001),
              metrics=['mean_absolute_error', 'mean_squared_error'])

print('model summary:')
model.summary()

#
# TRAIN
#

model.fit(train_x, train_y, batch_size = 10, epochs = 10)

print('success!')
