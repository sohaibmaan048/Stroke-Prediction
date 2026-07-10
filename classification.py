import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ---------------------------------------
# 1. Load Data
# ---------------------------------------
df = pd.read_csv("stroke_data.csv")

print(df.head())
print(df.info())

# ---------------------------------------
# 2. Visualization
# ---------------------------------------
plt.figure(figsize=(8, 5))
plt.hist(df["age"], bins=10, edgecolor="black")
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(True, alpha=0.3)
plt.show()

sns.countplot(x=df.columns[-1], data=df)
plt.title("Target Distribution")
plt.show()

# ---------------------------------------
# 3. Handle Missing Values
# ---------------------------------------
df = df.drop("id", axis=1)

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")

# ---------------------------------------
# 4. Encoding
# ---------------------------------------
text_cols = df.select_dtypes(include=["object", "category"]).columns
df_encoded = pd.get_dummies(df, columns=text_cols, drop_first=True)

# ---------------------------------------
# 5. Features & Target
# ---------------------------------------
X = df_encoded.drop("stroke", axis=1)
y = df_encoded["stroke"]

# ---------------------------------------
# 6. Train Test Split
# ---------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ---------------------------------------
# 7. Train Model (Random Forest)
# ---------------------------------------
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# ---------------------------------------
# 8. Evaluation
# ---------------------------------------
y_pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d")
plt.title("Confusion Matrix")
plt.show()

# ---------------------------------------
# 9. Save Model
# ---------------------------------------
joblib.dump(model, "random_forest_model.pkl")