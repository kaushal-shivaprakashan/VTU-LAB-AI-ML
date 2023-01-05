import numpy as np
import pandas as pd
from scipy.stats import entropy
from pprint import pprint

dataset = pd.read_csv("4.csv").iloc[:]
features = dataset.columns[:-1].tolist()
target = 'Target'
def get_weighted_entropy(data, feature):
    uf = data[target].value_counts(normalize = True)
    weighted_entropy = 0
    for i in range(len(uf)):
        table = data.where(data[feature] == uf.index[i]).dropna()
        table_entropy = entropy(table[target].value_counts())

        weighted_entropy += uf.values[i] * table_entropy
    return weighted_entropy
def ID3(data, features, most_freq_target_value):
    
    utv = data[target].value_counts()  
    
    if len(utv) <= 1: return utv.index[0]
    elif len(data) == 0: return d_mftv
    elif len(features) == 0: return most_freq_target_value
    
    else:

        #calculate information gain
        ig = []
        for feature in features:
            total_entropy = entropy(data[feature].value_counts())
            weighted_entropy = get_weighted_entropy(data, feature)
            ig.append(total_entropy - weighted_entropy)
        
        #create tree
        best_feature = features[np.argmax(ig)]
        tree = {best_feature:{}}
        features.remove(best_feature)
        
        #create sub_features_table_and_sub_tree
        sub_features = np.unique(data[best_feature])
        for sf in sub_features:
            sub_table = data.where(data[best_feature] == sf).dropna()
            sub_tree = ID3(sub_table, features, utv.index[0])
            tree[best_feature][sf] = sub_tree
            
        return tree
d_mftv = dataset[target].value_counts().index[0]
pprint(ID3(dataset, features, d_mftv))
