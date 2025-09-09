import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

#single linear regression
print("Single Linear Regression (TV vs Sales)")
advertising_df = pd.read_csv("exp7/advertising.csv")
X_single = advertising_df[['TV']]
y_single = advertising_df['Sales']


X_train_s, X_test_s, y_train_s, y_test_s = train_test_split(X_single, y_single, test_size=0.2, random_state=42)


model_single = LinearRegression()
model_single.fit(X_train_s, y_train_s)
y_pred_s = model_single.predict(X_test_s)


r2_single = r2_score(y_test_s, y_pred_s)
mse_single = mean_squared_error(y_test_s, y_pred_s)


print("R² Score (Single Linear):", r2_single)
print("Mean Squared Error (Single Linear):", mse_single)

#multiple linear regression
print("\nMultiple Linear Regression (Boston Housing) ")
boston_df = pd.read_csv("exp7/Boston.csv")

X_multi = boston_df.drop(columns=['medv'])
y_multi = boston_df['medv']


X_train_m, X_test_m, y_train_m, y_test_m = train_test_split(X_multi, y_multi, test_size=0.2, random_state=42)


model_multi = LinearRegression()
model_multi.fit(X_train_m, y_train_m)
y_pred_m = model_multi.predict(X_test_m)


r2_multi = r2_score(y_test_m, y_pred_m)
mse_multi = mean_squared_error(y_test_m, y_pred_m)


print("R² Score (Multiple Linear):", r2_multi)
print("Mean Squared Error (Multiple Linear):", mse_multi)




#polynomial regression
print("\nPolynomial Regression (Month vs Sales)")
ice_df = pd.read_csv("exp7/icecream.csv")
X_poly = ice_df[['month']]
y_poly = ice_df['sales']

poly = PolynomialFeatures(degree=2)
X_poly_transformed = poly.fit_transform(X_poly)

X_train_p, X_test_p, y_train_p, y_test_p = train_test_split(X_poly_transformed, y_poly, test_size=0.2, random_state=42)

model_poly = LinearRegression()
model_poly.fit(X_train_p, y_train_p)
y_pred_p = model_poly.predict(X_test_p)

r2_poly = r2_score(y_test_p, y_pred_p)
mse_poly = mean_squared_error(y_test_p, y_pred_p)

print("R² Score (Polynomial Regression):", r2_poly)
print("Mean Squared Error (Polynomial Regression):", mse_poly)
