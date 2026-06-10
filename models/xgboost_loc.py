# packages
import os
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from xgboost import XGBClassifier

# load full df
base = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
data_path = os.path.join(base, "data")
full_path = os.path.join(data_path, "setters.xlsx")
df = pd.read_excel(full_path)

# load split data
split_path = os.path.join(data_path, "split")
train_df = pd.read_excel(os.path.join(split_path, "train.xlsx"))
val_df = pd.read_excel(os.path.join(split_path, "val.xlsx"))
test_df = pd.read_excel(os.path.join(split_path, "test.xlsx"))
























