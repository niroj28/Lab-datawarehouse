#5. Classifiaction: Diabetes Prediction Using Naive Bayes Classifier
import pandas as pd
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB

dataset = pd.read_csv('Diabetes.csv')


split = int(len(dataset)*0.7)
train, test = dataset[:split], dataset[split:]

p = train['Pregnancies'].values
g = train['Glucose'].values
bp= train['BloodPressure'].values
st= train['SkinThickness'].values
ins= train['Insulin'].values
bmi= train['BMI'].values
dfp= train['DiabetesPedigreeFunction'].values
a= train['Age'].values
d= train['Outcome'].values

trainfeatures=zip(p,g,bp,st,ins,bmi,dfp,a)
traininput=list(trainfeatures)
#print(traininput)

model = GaussianNB()
model.fit(traininput,d)

p = test['Pregnancies'].values
g = test['Glucose'].values
bp= test['BloodPressure'].values
st= test['SkinThickness'].values
ins= test['Insulin'].values
bmi= test['BMI'].values
dpf= test['DiabetesPedigreeFunction'].values
a= test['Age'].values
d= test['Outcome'].values

testfeatures=zip(p,g,bp,st,ins,bmi,dpf,a)
testinput=list(testfeatures)

print("0 = Non-diabetic")
print("1 = Diabetic\n")
predicted= model.predict(testinput) 
print("Actual Class\n", *d)
print("\nPredicted Class:\n",*predicted)

print("\nConfusion Matrix")
print(metrics.confusion_matrix(d, predicted))
print("\nClassification Measures:")

print(metrics.classification_report(d, predicted))
print("Accuracy:",metrics.accuracy_score(d,predicted))

#print("Recall:",metrics.recall_score(d,predicted))
#print("Precision:",metrics.precision_score(d,predicted))
#print("F1-Score:",metrics.f1_score(d,predicted))