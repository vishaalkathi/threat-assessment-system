import pandas as pd
import pickle
from sklearn.ensemble import RandomForestClassifier

# load dataset
df = pd.read_csv("ml/dataset.csv")

# convert direction to numbers
df['direction'] = df['direction'].map({
    'approaching': 1,
    'hovering': 2,
    'leaving': 3
})

X = df[['speed','altitude','distance','direction']]
y = df['object_type']

# train model
model = RandomForestClassifier()
model.fit(X, y)

# save model
with open("ml/model.pkl","wb") as f:
    pickle.dump(model, f)

print("Model trained!")