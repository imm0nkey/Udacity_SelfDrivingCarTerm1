import numpy as np
import pandas as pd

admissions = pd.read_csv('binary.csv')
print(admissions)

# Make dummy variables for rank
data = pd.concat([admissions, pd.get_dummies(admissions['rank'], prefix='rank')], axis=1)
print(data)
data = data.drop('rank', axis=1)
print(data)

# Standardize features
for field in ['gre', 'gpa']:
    mean, std = data[field].mean(), data[field].std()
    data.loc[:, field] = (data[field]-mean)/std
print(data)

# Split off random 10% of the data for testing
np.random.seed(42)
sample = np.random.choice(data.index, size=int(len(data)*0.9), replace=False)
print(sample)
data, test_data = data.iloc[sample], data.drop(sample)
print('data')
print(data)
print('test_data')
print(test_data)

# Split into features and targets
features, targets = data.drop('admit', axis=1), data['admit']
print('features')
print(features)
print('targets')
print(targets)
features_test, targets_test = test_data.drop('admit', axis=1), test_data['admit']
print('features_test')
print(features_test)
print('targets_test')
print(targets_test)
