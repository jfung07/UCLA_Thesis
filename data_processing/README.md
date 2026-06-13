# Julia Fung UCLA MASDS Thesis Repository

insert stuff about project here

## Dependencies
The `requirements.in` script contains the packages used within the project, and `uv pip compile requirements.in -o requirements.txt` compiles the required packages into `requirements.txt`.

## Data
The data lives in the `data` folder within the project root.  The `setters.xlsx` file contains the raw game data as an excel sheet, and the `set_images` folder contains the corresponding images for each row, where each row represents a team's possession.  I grouped the images within game sets, and each image, like row, represents a team's possession. 
I created three scripts in VSCode to process the data, `clean_data.py`, `image_resize.py`, and `xgboost_split.py`.
The `clean_data.py` script cleans the `setters.xlsx` file and outputs the resulting data as `processed.xlsx`.  Data cleaning includes setting data types, removing whitespaces, and engineering features.  I engineered features `receiver_loc_cos`, `receiver_loc_sin`, `pass_loc_cos`, and `pass_loc_sin` to represent the first and second touch locations on the court.  High cosine values represent locations on the left side of the court looking at the team from the team's endline rather than as the opposing team.  Thus, low cosine values represent locations on the right side.  High sine values represent locations closer to the net, while low sine values represent locations closer to the net.  0 values represent locations in the middle of the team's court half verically and horizontally.  The `pro` feature is the `level` feature as a logic feature, and the `men` feature is the logic `game_sex` feature. 
The `image_resize.py` script resizes the images in `set_images` to 1024x512 images.
The `xgboost_split.py` script splits the excel file into training, validation, and testing sets for the xgboost models to use as a 70/15/15 split.  The script saves the data frames as `train.xlsx`, `val.xlsx`, and `test.xlsx` in data/split. 

## LogReg_Rf.qmd
The `LogReg_Rf.qmd` quarto document contains the baseline models' training, selection, and evaluation processes.  The baseline model are logistic regression, and random forest models built in R.

## Models
I train, select, and evaluate the advanced models in the GoogleColab notebooks, to explore other data analyis venues, that live in the `models` folder.  The `cnn` folder contains the scripts for the neural networks that process images, while the `xgboost` folder contains scripts for the spreadsheet data.  
The `cnn` folder contains a script for the three response variables, attack success, set location, and set reciever.  The folder contains two additional scripts that investigate different groupings for the set location and set receiver variables marked as `Grouped`.  Each cnn script contains CNN and VGG construction, training, selection, and evaluation for each response variable.  Thus, the scripts are `CNN_<Orig or Grouped><variable_name>.ipynb`.
The `xgboost` folder contains the script constructing, training, selecting, and evaluating an xgboost model for its corresponding response variable.  I labeled the scripts as XGBoost_<variable_name>.ipynb.


