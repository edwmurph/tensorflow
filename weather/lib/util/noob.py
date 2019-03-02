import re
import numpy as np

# input: dataframe
# output: first row of dataframe
def get_first_row(df):
    return df.iloc[0,:]

# input: series
# output: new series
# e.g. replace_in_series(df.column, r'\d*-([a-zA-Z]*)-\d*', '\\1')
def replace_in_series(series, regex, replacement):
    return series.apply(
        lambda x: re.sub(regex, replacement, x)
    )

# input: python list or numpy array
# output: throws error if sorted lists are not equal
def validate_lists_equal(list1, list2):
    arr1 = np.sort( np.array(list1) )
    arr2 = np.sort( np.array(list2) )
    if not np.array_equal( arr1, arr2 ):
        print('\nDEBUG:')
        print(arr1)
        print(arr2)
        print('')
        raise Exception('lists are not equal:')

# input: dictionary
# output: new dictionary
def map_dic(dic, valFn, keyFn = lambda x,y: x):
    newDic = {}
    for key, value in dic.items():
        newKey = keyFn(key, value)
        newValue = valFn(key, value)
        newDic[ newKey ] = newValue
    return newDic

def validate_match(regex, string):
    if not re.match(regex, string):
        print('\nDEBUG:')
        print(regex)
        print(string)
        print('')
        raise Exception('regex did not match')
