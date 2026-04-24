import pandas as pd
from sklearn.linear_model import LogisticRegression

# Train on your split data
train = pd.read_csv('data/train.csv')
X = train.drop('Outcome', axis=1)
y = train['Outcome']

model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Predict on test features
test_features = pd.read_csv('data/test_features.csv')
preds = model.predict(test_features)

# Save the submission file
pd.DataFrame({'Outcome': preds}).to_csv('submissions/baseline_sub.csv', index=False)
print("Baseline created in submissions/baseline_sub.csv")