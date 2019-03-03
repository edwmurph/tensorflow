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

def print_frequencies(df, column):
    print("\n%s distribution:" % column)
    print(df[column].value_counts(dropna=False))
    print()

def print_range(df, column):
    print("\n%s range:" % column)
    print(df[column].describe())
    print()


#
# External
#

def get_redundant_pairs(df):
    '''Get diagonal and lower triangular pairs of correlation matrix'''
    pairs_to_drop = set()
    cols = df.columns
    for i in range(0, df.shape[1]):
        for j in range(0, i+1):
            pairs_to_drop.add((cols[i], cols[j]))
    return pairs_to_drop

def get_top_abs_correlations(df, threshold = 0.8):
    au_corr = df.corr().abs().unstack()
    labels_to_drop = get_redundant_pairs(df)
    au_corr = au_corr.drop(labels=labels_to_drop).sort_values(ascending=False)
    return au_corr[au_corr>threshold]
