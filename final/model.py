import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

# Load the JSON data
df = pd.read_json("admission_data.json")

# Check column names
print("Columns:", df.columns)

# Drop rows with missing percentile
df = df.dropna(subset=["percentile"])

# Convert string columns to categorical
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].astype("category")

# Define features and target
X = df.drop(columns=["percentile"])
y = df["percentile"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model using XGBRegressor with categorical support
model = XGBRegressor(
    enable_categorical=True,
    tree_method="hist",
    objective="reg:squarederror",
    n_estimators=100,
    max_depth=6,
    learning_rate=0.1
)

# Fit model
model.fit(X_train, y_train)

# Evaluate
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)
print(f"Mean Absolute Error on test set: {mae:.2f}")

# Predict one example
print("\nExample prediction:")
print("Input:", X_test.iloc[0])
print("Predicted Percentile:", model.predict(X_test.iloc[0:1])[0])
