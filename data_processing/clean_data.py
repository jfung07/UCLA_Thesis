# packages
import pandas as pd
import numpy as np
import os

# load in data
base = os.path.abspath(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
path_to_xlsx = os.path.join(base, "data", "setters.xlsx")
df = pd.read_excel(path_to_xlsx)

# remove whitespaces
df = df.replace(r'^\s*$', np.nan, regex=True)

# change numerical vars to numerical[points1, points2, team1_diff, team2_diff, tot_point, set, rotation, receiver_loc, pass_loc, pass_quality, num_block]
num_col = ['points1', 'points2', 'team1_diff', 'team2_diff', 'tot_point', 'set', 'rotation', 'receiver_loc', 'pass_loc', 'pass_quality', 'num_block']
df[num_col] = df[num_col].apply(
    lambda col: pd.to_numeric(col, errors='coerce')
)
df[num_col] = df[num_col].astype('Int64')

# change categorical to categorical variables[game, rotation, set_loc, set_receiver, team, level, game_sex]
# categorical does not carry through excel, so convert when using 

# change kill to logical
df['kill'] = df['kill'].astype('boolean')

# transform pass_loc and receive_loc
angle_map = {
    7: 11*np.pi/8,
    6: np.pi/2,
    5: np.pi/4,
    4: 7*np.pi/4,
    3: 3*np.pi/2,
    2: 5*np.pi/4,
    1: 3*np.pi/4
}
def encode_orientation(v):
    theta = angle_map[int(v)]
    return np.cos(theta), np.sin(theta)
df[['receiver_loc_cos', 'receiver_loc_sin']] = (
    df['receiver_loc'].apply(lambda v: pd.Series(encode_orientation(v)))
)
df[['pass_loc_cos', 'pass_loc_sin']] = (
    df['pass_loc'].apply(lambda v: pd.Series(encode_orientation(v)))
)

df['men'] = df['game_sex'].map({'W': 0, 'M': 1}).astype('int')

df = df.astype({
    'receiver_loc_cos': 'float',
    'receiver_loc_sin': 'float',
    'pass_loc_cos': 'float',
    'pass_loc_sin': 'float',
    'men': 'boolean'
})



# save
data_dir = os.path.join(base, "data")
os.makedirs(data_dir, exist_ok = True)
df.to_excel(os.path.join(data_dir, "processed.xlsx"), index = False)



