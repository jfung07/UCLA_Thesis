# packages
import pandas as pd
import numpy as np
import os

# load df
base = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
path_to_xlsx = os.path.join(base, "data", "processed.xlsx")
df = pd.read_excel(path_to_xlsx)

# split data
n = len(df)
idx = np.arange(n)
np.random.seed(256)
np.random.shuffle(idx)
train_end = int(0.7*n)
val_end = int(0.85*n)

# populate
train_idx = idx[:train_end]
train_df = df.iloc[train_idx]
val_idx = idx[train_end:val_end]
val_df = df.iloc[val_idx]
test_idx = idx[val_end:]
test_df = df.iloc[test_idx]

# save
split_dir = os.path.join(base, "data", "split")
os.makedirs(split_dir, exist_ok = True)
train_df.to_excel(os.path.join(split_dir, "train.xlsx"), index = False)
val_df.to_excel(os.path.join(split_dir, "val.xlsx"), index = False)
test_df.to_excel(os.path.join(split_dir, "test.xlsx"), index = False)
