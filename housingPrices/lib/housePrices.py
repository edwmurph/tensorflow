#import sys
#print('\nCurrent version of python:\n', sys.version, '\n')

# import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn as skl
import tensorflow as tf

from sklearn.preprocessing import StandardScaler

# adjust imports

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# global variables

NUM_FEATURES=8

# get data

train_data = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_train.csv", sep=",")
test_data = pd.read_csv("https://download.mlcc.google.com/mledu-datasets/california_housing_test.csv", sep=",")
total_data = pd.concat([train_data, test_data])

# split features from labels

train_y = train_data['median_house_value']
train_x = train_data.drop(columns=['median_house_value'])

test_y = test_data['median_house_value']
test_x = test_data.drop(columns=['median_house_value'])

if len(train_x.columns) != NUM_FEATURES or len(test_x.columns) != NUM_FEATURES:
    raise Exception('labels were not removed from features dataframe')

if total_data.isnull().values.any():
    raise Exception('some values in dataframe are missing')

for type in total_data.dtypes:
    if type != 'float64':
        raise Exception('one of the columns is the wrong type')

# we need to normalize the data because the features are on different scales
sc = StandardScaler()
train_x = sc.fit_transform(train_x)
test_x = sc.fit_transform(test_x)

# visualize dataset

#print('\nHead of total dataset:\n', total_data.head().transpose())
#
#print('\nTotal dataset summary:\n', total_data.describe().transpose())
#
#print('\nTraining features shape:\n', train_x.shape)
#
#print('\nTest features shape:\n', test_x.shape)

# the distribution of median house value appears to be slightly skewed
# sns.distplot(total_data['median_house_value']);
# plt.show()

model = tf.keras.Sequential([
    # define input layer
    tf.keras.layers.Dense(64, activation=tf.nn.relu, input_shape=[NUM_FEATURES]),
    # only have single output dense layer
    tf.keras.layers.Dense(1)
])

model.compile(loss='mean_squared_error',
              optimizer=tf.keras.optimizers.RMSprop(0.001),
              metrics=['mean_absolute_error', 'mean_squared_error'])

print('model summary:')
model.summary()

model.fit(train_x, train_y, batch_size = 10, epochs = 10)
