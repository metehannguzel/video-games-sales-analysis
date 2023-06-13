from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pandas as pd

# load data
df = pd.read_csv("./dataset.csv")

# drop unnecessary columns
df = df.drop(["Name"], axis=1)

# set X axis as all columns but Global_Sales and set Y axis as Global_Sales
X = df.drop(["Global_Sales"], axis=1)
Y = df["Global_Sales"]

# import LabelEncoder to convert string values into numeric values
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()

for i in X:
    if X[i].dtype not in ["float64", "int64"]:
        X[i] = encoder.fit_transform(X[i])
    
    # fill NaN values as mean of the column's all values
    X[i] = X[i].fillna(int(X[i].mean()))

X = X.values
Y = Y.values

# import train_test_split to splite 20% of dataset as a testing set and 80% as a training test
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

# creat a dictionary to keep models
models = {"Nearest Neighbors (k = 5)": KNeighborsRegressor(),
    "Decision Tree": DecisionTreeRegressor(),
    "Linear Regression": LinearRegression()}

best_test = 100000
best_model = ""

# train and evaluate mse for all regression models
for i in models:
    model  = models[i]
    model.fit(x_train, y_train)

    y_pred = model.predict(x_test)
    errors = mean_squared_error(y_test, y_pred)
    
    print(f"\n{i} test error: {errors}")
    
    if best_test > errors:
        best_model = i
        best_test = errors
        
        
# choose best model according to the mse        
print("\nThe best model for this dataset: " + best_model + "\n")

# create model
import pickle
file_name = 'model.sav'
pickle.dump(models[best_model], open(file_name, 'wb'))
