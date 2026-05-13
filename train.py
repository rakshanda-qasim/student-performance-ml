import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# FIX: correct separator
df = pd.read_csv("data/student-mat.csv", sep=";")

print("Dataset Loaded Successfully")
print(df.head())

target_column = "G3"

# select numeric columns
numeric_df = df.select_dtypes(include=["int64", "float64"])

X = numeric_df.drop(columns=[target_column])
y = numeric_df[target_column]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("R2 Score:", r2_score(y_test, pred))