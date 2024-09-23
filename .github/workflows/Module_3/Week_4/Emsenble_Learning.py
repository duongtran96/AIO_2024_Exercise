###########################
# 1. Import libralies
###########################

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error

###########################
# 2. Load data
###########################
""


###########################
# 3. Read data
###########################

dataset_path = ''
df = pd.read_csv(dataset_path)


###########################
# 4. Processing categorical
###########################

categorical_cols = df.select_dtypes(include = ['object']).columns.to_list()
print(categorical_cols)

# Convert to number by using OrdinalEncoder()
ordinal_encoder = OrdinalEncoder()
encoded_categorical_cols = ordinal_encoder.fit_transform(
                            df[categorical_cols])

print(encoded_categorical_cols)

encoded_categorical_df = pd.DataFrame(encoded_categorical_cols, 
                                    columns = categorical_cols)

print(encoded_categorical_df)

numerical_df = df.drop(categorical_cols, axis = 1)
encoded_df = pd.concat([numerical_df, 
                        encoded_categorical_df], axis = 1)


###########################
# 5. Normalize the data set
###########################

normalizer = StandardScaler()
dataset_arr = normalizer.fit_transform(encoded_df)


###########################
# 6. Slit data X, y
###########################

test_size = 0.3
random_state = 1
is_shuffle = True
X_train, X_val, y_train, y_val = train_test_split(X, y, 
                                    test_size = test_size, 
                                    random_state = random_state, 
                                    shuffle = is_shuffle
)

###########################
# 7. Train model
###########################

def train_val_model(model, X_train, X_val, y_train, y_val):
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_val)

    # Calculate MAE and MSE
    mae = mean_absolute_error(y_val, y_pred)
    mse = mean_squared_error(y_val, y_pred)

    print(f"Model : {model}")
    print('Evaluation results on validation set:')
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")

if __name__ == "__main__":

    # Random Forest
    regressor_RF = RandomForestRegressor(random_state = random_state)
    train_val_model(regressor_RF, X_train, X_val, y_train, y_val)

    # AdaBoost
    regressor_Ada = AdaBoostRegressor(random_state = random_state)
    train_val_model(regressor_Ada, X_train, X_val, y_train, y_val)

    # Gradient
    regressor_Gra = GradientBoostingRegressor(random_state = random_state)
    train_val_model(regressor_Gra, X_train, X_val, y_train, y_val)
