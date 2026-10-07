#Practical 14
#Demonstrate basic machine learning workflow using Scikitlearn:data loading, splitting, model training and evaluation.


from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import pandas as pd


data = pd.DataFrame({
    "StudyHours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Marks": [40, 45, 50, 55, 60, 65, 72, 80]
})


X = data[["StudyHours"]]
y = data["Marks"]


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)


model = LinearRegression()


model.fit(X_train, y_train)


predictions = model.predict(X_test)

print("Actual Marks:")
print(y_test.values)

print("\nPredicted Marks:")
print(predictions)


error = mean_squared_error(y_test, predictions)

print("\nMean Squared Error:", error)


hours = [[9]]
print("\nPredicted marks for 9 study hours:",
      model.predict(hours)[0])
