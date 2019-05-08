import os
import pandas as pd

def data_reader(data_path):
    # Reading train and test data
    train_df = pd.read_csv(os.path.join(data_path, "train.csv"))
    test_df  = pd.read_csv(os.path.join(data_path, "test.csv"))
    
    # Spliting features and target
    train_target = train_df.target
    train_features = train_df.drop(columns=['ID_code', 'target'])
    test_idcode = test_df.ID_code
    test_features = test_df.drop(columns=['ID_code'])
    
    return train_features, train_target, test_features, test_idcode

def train_test_loader(data_path):
    train_features = pd.read_csv(os.path.join(data_path, "train_features.csv"))
    train_target = pd.read_csv(os.path.join(data_path, "train_target.csv"), header=None)
    test_features = pd.read_csv(os.path.join(data_path, "test_features.csv"))
    test_target = pd.read_csv(os.path.join(data_path, "test_target.csv"), header=None)
    
    return train_features, train_target, test_features, test_target