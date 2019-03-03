# https://github.com/MTG/sms-tools/issues/36
from sys import platform as sys_pf
if sys_pf == 'darwin':
    import matplotlib
    matplotlib.use("TkAgg")

from util.noob import *

import sys
validate_match(r'^3.*', sys.version)

import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt

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
              metrics=['mean_squared_error'])

print('model summary:')
model.summary()

#
# TRAIN
#

# train for up to 25 epochs but stop if validation loss isn't improving enough
# early_stop will usually stop at around 15-20 epochs
EPOCHS=25
early_stop = tf.keras.callbacks.EarlyStopping(
    monitor='val_loss',
    min_delta=0.01,
    patience=5
)
training_history = model.fit(
    train_x,
    train_y,
    batch_size = 10,
    epochs = EPOCHS,
    validation_split = 0.3,
    callbacks=[early_stop]
)

ACTUAL_EPOCHS = EPOCHS - (EPOCHS - len(training_history.history['loss']))

# --plot training accuracy over epochs
plot_history(training_history)

#
# PREDICT
#

print('\npredictions:')
loss, mse = model.evaluate(test_x, test_y, verbose=0)
print("Testing set Mean Square Error: {:5.2f} °F".format(mse))


test_predictions = model.predict(test_x).flatten()

plt.scatter(test_y, test_predictions, s=.11)
plt.title("Prediction Accuracy After %s Epochs" % (ACTUAL_EPOCHS))
plt.xlabel('True Values [°F]')
plt.ylabel('Predictions [°F]')
plt.axis('equal')
plt.axis('square')
_ = plt.plot([-100, 100], [-100, 100])
plt.show()

print('success!')
