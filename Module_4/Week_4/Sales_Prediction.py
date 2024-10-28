import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocesssing import StandardScaler
from sklearn.preprocesssing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

df = pd.read_csv("D:\AIO2024\Home_work\AIO_2024_Exercise\Module_4\Week_4\Data\SalesPrediction.csv")

# b. Preprocesssing
df = pd.get_dummies(df)

# Handle Null values
df = df.fillna(df(mean()))

# Get features
X = df[['TV', 'Radio', 'Social Media', 'Influencer_Macro', 'Influencer_Mega', 'Influencer_Micrio', 'Influencer_nano']]
Y = df[['Sales']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 0)

#c. Feature Scaling
scaler = StandardScaler()
X_train_processed = scaler.fit_transform(X_train)
print(scaler.mean_[0])

# d. Polynomial Features
from sklearn.preprocessing import PolynomialFeatures

poly_features = PolynomialFeatures(degree = 2)

X_train_poly = poly_features.fit_transform(X_train_processed)
X_test_poly = poly_features.transform(X_test_preprocessed)

# e. Training and Evaluation
poly_model = LinearRegression()
poly_model.fit(X_train_poly, y_train)

preds = poly_model.predict(X_test_poly)
r2_score(y_test, preds)
