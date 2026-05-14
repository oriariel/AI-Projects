import pandas as pd
df = pd.read_csv('C:/Users/oriar/Documents/Python/titanic.csv')
df.head()
df.info() #see colums, types, and null values
df.describe() #see stats of numeric columns
df['Survived'].value_counts() #class balance check

import seaborn as sns
sns.heatmap(df.isnull(), cbar=False) #visualise missing data
sns.barplot(x='Pclass', y='Survived', data=df) #survival by class

df['Age'] = df['Age'].fillna(df['Age'].median()) #impute missing ages with median
df['Embarked'] = df['Embarked'].fillna('S') #impute missing embarked with most common value
df.drop(columns=['Cabin', 'Ticket', 'Name', 'PassengerId'], inplace=True) #drop irrelevant columns

#Create useful features
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1 #family size
df['IsAlone'] = (df['FamilySize'] == 1).astype(int) #is alone

#Encode categoricals
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1}) 
df = pd.get_dummies(df, columns=['Embarked'], drop_first=True) #one-hot encode  

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

x = df.drop('Survived', axis=1) #features
y = df['Survived'] #target

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42) #split data

model = RandomForestClassifier(n_estimators=100, random_state=42) #initialize model
model.fit(X_train, y_train) #train model

preds = model.predict(X_test) #make predictions
print(accuracy_score(y_test, preds)) #evaluate accuracy
print(classification_report(y_test, preds)) #detailed classification report

import matplotlib.pyplot as plt

#feature importance - which feautures mattered most?
feat_imp = pd.Series(model.feature_importances_, index = X_train.columns)
feat_imp = feat_imp.sort_values()  #plot feature importance

fig, ax = plt.subplots(figsize=(8,5))
feat_imp.plot(kind = 'barh', ax=ax, color = 'steelblue')
ax.set_title('Feature Importance')
ax.set_xlabel('Importance Score')
plt.tight_layout()
plt.show()

#Confusion matrix - see where model made mistakes
from sklearn.metrics import ConfusionMatrixDisplay
fig, ax = plt.subplots(figsize=(5,4))
ConfusionMatrixDisplay.from_estimator(model, X_test, y_test, ax=ax)
ax.set_title('Confusion Matrix')
plt.tight_layout()
plt.show()

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score

models = {
    'Logistic Regression': LogisticRegression(max_iter=1000),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42),
    'SVM': SVC(kernel='rbf')
}

for name, model in models.items():
    scores = cross_val_score(model, x, y, cv=5, scoring='accuracy')
    print(f"{name}: {scores.mean():.3f} (+/- {scores.std() * 2:.3f})")
