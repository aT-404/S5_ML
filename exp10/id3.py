import pandas as pd
import math

# Load dataset
df = pd.read_csv("exp10/Buy_Computer.csv")

# Drop id column (not useful)
df = df.drop(columns=['id'])

# Calculate entropy
def entropy(target_col):
    elements, counts = pd.Series(target_col).value_counts().index, pd.Series(target_col).value_counts().values
    entropy_val = 0
    for i in range(len(elements)):
        p = counts[i] / sum(counts)
        entropy_val += -p * math.log2(p)
    return entropy_val

# Information gain
def info_gain(data, split_attribute, target="Buy_Computer"):
    total_entropy = entropy(data[target])
    vals, counts = data[split_attribute].value_counts().index, data[split_attribute].value_counts().values
    weighted_entropy = 0
    for i in range(len(vals)):
        subset = data[data[split_attribute] == vals[i]]
        weighted_entropy += (counts[i]/sum(counts)) * entropy(subset[target])
    return total_entropy - weighted_entropy

# Build decision tree recursively
def id3(data, original_data, features, target="Buy_Computer", parent_node_class=None):
    # If all target values are the same → return that value
    if len(data[target].unique()) <= 1:
        return data[target].iloc[0]

    # If dataset is empty → return majority from original dataset
    elif len(data) == 0:
        return original_data[target].mode()[0]

    # If no more features → return parent node’s majority class
    elif len(features) == 0:
        return parent_node_class

    # Otherwise → choose feature with max information gain
    else:
        parent_node_class = data[target].mode()[0]
        gains = [info_gain(data, feature, target) for feature in features]
        best_feature = features[gains.index(max(gains))]

        tree = {best_feature: {}}

        # Remove used feature
        remaining_features = [f for f in features if f != best_feature]

        # Grow subtrees for each value of best_feature
        for val in data[best_feature].unique():
            sub_data = data[data[best_feature] == val]
            subtree = id3(sub_data, data, remaining_features, target, parent_node_class)
            tree[best_feature][val] = subtree

        return tree

# Prediction function
def predict(query, tree, default="yes"):
    for feature in query.keys():
        if feature in tree.keys():
            try:
                result = tree[feature][query[feature]]
            except:
                return default
            if isinstance(result, dict):
                return predict(query, result)
            else:
                return result

# ---------------- Main ----------------
features = df.columns.tolist()
features.remove("Buy_Computer")

# Build tree
tree = id3(df, df, features, target="Buy_Computer")

print("\nDecision Tree (as dictionary):")
print(tree)

# ---- User input for prediction ----
print("\nEnter details to predict if user will Buy Computer or Not:\n")

age = input("Enter age (youth/middle_age/senior): ").strip().lower()
income = input("Enter income (low/medium/high): ").strip().lower()
student = input("Is student? (yes/no): ").strip().lower()
credit_rating = input("Enter credit rating (fair/excellent): ").strip().lower()

# Create query dictionary
query = {
    "age": age,
    "income": income,
    "student": student,
    "credit_rating": credit_rating
}

# Prediction
prediction = predict(query, tree)
print("\nPrediction for given input:", query)
print("Predicted class (Buy_Computer):", prediction)
