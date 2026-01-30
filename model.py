import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from data import df

X = df.drop('Country', axis=1).values
y = df['Country'].values

le = LabelEncoder()
y_encoded = le.fit_transform(y)

tree = DecisionTreeClassifier(criterion='entropy', max_depth=6, random_state=0)
tree.fit(X, y_encoded)

features = list(df.columns[1:])
