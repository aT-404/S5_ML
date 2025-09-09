import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder


# Load dataset and drop Record column
df = pd.read_csv("exp10/Buy_Computer.csv").drop("id", axis=1)

# Encode categorical variables
df_encoded = df.apply(lambda col: pd.factorize(col)[0])

X = df_encoded.drop("Buy_Computer", axis=1)
y = df_encoded["Buy_Computer"]

# Train Decision Tree
clf = DecisionTreeClassifier(criterion="entropy")
clf.fit(X, y)

# Plot the decision tree
plt.figure(figsize=(12,8))
plot_tree(clf,
          feature_names=list(X.columns),
          class_names=["No","Yes"],
          filled=True,
          rounded=True,
          fontsize=10)
plt.show()

print("\nEnter new data for prediction\n")

age = input("Enter Age (Youth/Middle_aged/Senior): ")
income = input("Enter Income (Low/Medium/High): ")
student = input("Student (Yes/No): ")
credit_rating = input("Credit Rating (Fair/Excellent): ")

# Create dataframe for new input
new_data = pd.DataFrame([[age, income, student, credit_rating]],
                        columns=['age', 'income', 'student', 'credit_rating'])

# Apply same encoding
for col in new_data.columns:
    le = LabelEncoder()
    le.fit(df[col])
    new_data[col] = le.transform(new_data[col])

# Predict
prediction = clf.predict(new_data)
print("Predicted class (0=No, 1=Yes):", prediction[0])