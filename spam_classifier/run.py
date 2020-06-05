from application import app
import pickle
from spam_classifier import Filter
import pandas as pd

SPAM = 1
NOT_SPAM = 0
df = pd.read_csv("spam_or_not_spam.csv")
df = df.dropna()
df['label'] = df['label'].apply(lambda s: SPAM if (s == 1) else NOT_SPAM)

data_list = df.values.tolist()

model = Filter()
model.train(data_list)
with open('data.pickle', 'wb') as f:
    pickle.dump(model, f)