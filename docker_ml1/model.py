from sklearn import svm, datasets
import pickle
import numpy as np

iris = datasets.load_iris()

X = iris.data
y = iris.target

model = svm.SVC(kernel='poly', degree=3, C=1.0).fit(X, y)

models_folder = 'models/'
model_file_name = 'svm'
with open(models_folder+model_file_name+'.pckl', 'wb') as model_file:
    pickle.dump(model, model_file)
