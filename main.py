import argparse
import pandas as pd
from ecg import *
from sklearn import metrics
from sklearn import linear_model
from xgboost import XGBClassifier
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, ExtraTreesClassifier
from sklearn.metrics import confusion_matrix, classification_report

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--detector', nargs='?', type=str, default='hamilton', help='R-peak detector name')
parser.add_argument('-clf', '--classifier', nargs='?', type=str, default='logreg', help='Classification algorithm name')
parser.add_argument("-V", "--version", help="show program version", action="store_true")
args = parser.parse_args()

classifiers = { 
    'logreg': linear_model.LogisticRegression(max_iter=2000), 
    'decisiontree': DecisionTreeClassifier(criterion='entropy'),
    'xgboost': XGBClassifier(), 
    'randomforest': RandomForestClassifier(criterion='entropy'), 
    'extratrees': ExtraTreesClassifier(criterion='entropy'), 
    'bagging': BaggingClassifier(DecisionTreeClassifier(), max_samples=0.5, max_features=0.5) 
    }

ecg_preprocessor(args.detector)
df = pd.read_csv("ecg_processed.csv")
X = df[['mean_hr', 'std','NFD', 'NSD', 'HRV', 'avNN', 'sdNN', 'RMSSD', 'NN50', 'pNN50', 'pNN20']]
y = df["anxiety"]

estimator = RandomForestClassifier(criterion='entropy')
featureSelector = RFE(estimator) 
featureSelector = featureSelector.fit(X, y)

featuresRanked = list(featureSelector.ranking_) 
selectedFeatures = [] 
for i in range(len(featuresRanked)): 
    if(featuresRanked[i] == 1): 
        selectedFeatures.append(X.columns[i])


X = X[selectedFeatures]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

clf = classifiers[args.classifier]
clf = clf.fit(X_train, y_train)
print(f'Training accuracy: {clf.score(X_train, y_train)}')
print(f'Testing accuracy: {metrics.accuracy_score(y_test, clf.predict(X_test))}')
print(f'Confusion Matrix: {confusion_matrix(y_test, clf.predict(X_test))}')
print(f'Classification Report: {classification_report(y_test, clf.predict(X_test))}')
