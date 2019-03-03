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
import seaborn as sns
import matplotlib.pyplot as plt

from schema_data import *

#
# GLOBAL VARIABLES / SETTINGS
#

pd.set_option( 'display.max_columns', 500 )
pd.set_option( 'display.width', 1000 )

NUM_FEATURES=8

#
# GET RAW DATA
#

data = pd.read_csv(
    '../data/original_weather_data.csv',
    sep=',',
    dtype=type_columns_dic
)
data = data[rename_columns_dic]; # extract columns for analysis
data = data.rename( index=str, columns=rename_columns_dic ) # rename columns
print('\nshape before feature selection/reduction:', data.shape)

#
# FEATURE ENGINEERING
#

# 'date'
# TODO incorporate with one-hot encoding
# convert 'date' column to just month
data.date = replace_in_series( data.date, r'\d*-([a-zA-Z]*)-\d*', '\\1' )
expected = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
validate_lists_equal( data.date.unique(), expected )
data = data.drop(['date'], 1)

# --weather type
# TODO incorporate with one-hot encoding and fix typos
data = data.drop('predominate_weather', 1);

# --sunrise/sunset
# TODO incorporate this somehow
data = data.drop(['sunrise', 'sunset'], 1)

# --remove features without enough (arbitrarily picked 90%) valid data
data = data.drop(['snowfall_metar', 'sunshine_observed', 'snowfall_day', 'snowfall_nws', 'snowfall_rtp', 'precip_hours'], 1)

# --somewhat arbitrarily reduce tuplets of features that are highly correlated
data = data.drop(['avg_feels_like', 'avg_temp_2', 'avg_solar_radiance_2', 'avg_heat_index', 'avg_heat_index_2', 'avg_dew_point_2', 'avg_wind_chill_temp', 'sunshine_percent', 'avg_daily_pressure_mb', 'lowest_pressure_mb', 'highest_pressure_mb', 'lowest_pressure_in', 'sunshine_calculated', 'max_wind_gust', 'highest_sustained_wind_speed', 'highest_pressure_in', 'avg_solar_radiance'], 1);

#print(data['snowfall_nws'].describe())
if not len(get_top_abs_correlations(data)) == 0:
    raise Exception('features are too correlated to continue')

# --remove rows with invalid data
data = data.dropna()

#
# EXPORT ENGINEERED DATASET
#

print('\nshape after feature selection/reduction:', data.shape)

# print correlation stats
# print(data.describe().transpose())

# print correlation matrix
#sns.heatmap(data.corr())
#plt.show()

data.to_csv(path_or_buf='../data/processed_weather_data.csv', index=False)

print('success!')
