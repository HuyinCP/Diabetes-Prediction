import pandas as pd
from fontTools.unicodedata import script
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from  sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from lazypredict.Supervised import LazyClassifier

# Read data
file_path = 'Datasets/diabetes.csv'
df = pd.read_csv(file_path)

# Data visualization and statistics
# profile = ProfileReport(df, title="Diabetes report", explorative=True)
# profile.to_file("Diabetes.html")

# Data split
target = "Outcome"
x = df.drop([target], axis = 1)
y = df[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Data processing
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train model
# model = RandomForestClassifier(n_estimators=200, random_state=100, criterion="entropy")
# model.fit(x_train, y_train)
# y_prd = model.predict(x_test)
# print(classification_report(y_test, y_prd))

# params = {
#     "n_estimators" : [100, 200, 300, 400],
#     "criterion" : ["gini", "entropy", "log_loss"]
# }
# gird_search = GridSearchCV(estimator=RandomForestClassifier(random_state=42), param_grid=params, cv=5, verbose=2, scoring="recall")
# gird_search.fit(x_train, y_train)
#
# print(gird_search.best_estimator_)
# print(gird_search.best_score_)
# print(gird_search.best_params_)
#
# y_prd = gird_search.predict(x_test)
# print(classification_report(y_test, y_prd))
# print((0.79 + 0.64) / 2)

clf = LazyClassifier(verbose=0, ignore_warnings=True, custom_metric=None)
models, predictions = clf.fit(x_train, x_test, y_train, y_test)
print(models)