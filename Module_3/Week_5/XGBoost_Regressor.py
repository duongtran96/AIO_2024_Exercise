import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split

# Load Data
data_path = './Problem3.csv'
data_df = pd.read_csv(data_path)
print(data_df.head(3))


categorical_cols = data_df.select_dtypes(include = ['object', 'bool']).columns.to_list()

for col_name in categorical_cols:
    n_categories = data_df[col_name].nunique()
    print(f"Number of categories in {col_name}: {n_categories}")

ordinal_encoder = OrdinalEncoder()
encoded_categorical_cols = ordinal_encoder.fit_transform(
                                    data_df[categorical_cols])

encoded_categorical_df = pd.DataFrame(encoded_categorical_cols, 
                                    columns = categorical_cols)

numerical_df = data_df.drop(categorical_cols, axis = 1)

encoded_df = pd.concat([numerical_df, encoded_categorical_df], axis = 1)

# Split X, y
X = encoded_df.drop(columns = ['area'])
y = encoded_df['area']

# split 7:3
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 7)

# Model XGBppst for Regression with parameters seed = 7, learning_rate = 0.01, n_estimators = 102, max_depth = 3
xg_reg = xgb.XGBRegressor(seed = 7, 
                    learning_rate = 0.01, 
                    n_estimators = 102, 
                    max_depth = 3)

def train_test_model(model, X_train, X_test, y_train, y_test):
    model.fit(X_train, y_train)

    # Predict 
    preds = xg_reg.predict(X_test)

    # Calculate MAE, MSE 
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)

    # Print results
    print(f"Model : {model}")
    print('Evaluation results on test set:')
    print(f"Mean Absolute Error: {mae}")
    print(f"Mean Squared Error: {mse}")


if __name__ == "__main__":
    xg_reg = xgb.XGBRegressor(seed = 7, learning_rate = 0.01, n_estimators = 102, max_depth = 3)
    train_test_model(xg_reg, X_train, X_test, y_train, y_test)
