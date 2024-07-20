from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import pandas as pd
from sklearn import *
import numpy as np
import pandas as pd
from sklearn import *
from sklearn.metrics import accuracy_score
df = pd.read_csv('eduset.csv')
df["AddnlCourses?"] = df["AddnlCourses?"].map({'NoCourses':-1,'LessThan3':0,'ThreeOrmore':1})
df["StudyBlogs?"] = df["StudyBlogs?"].map({'StudyBlogs':1,'DoNotStudy':0})
df["WriteRsrchPapers?"] = df["WriteRsrchPapers?"].map({'WriteRsrchPapers':1,'NoRsrchPapers':0})
df["ListenTechVideos?"] = df["ListenTechVideos?"].map({'ListenTechVideos':1,'DoNotListen':0})
df["CourseCertifications?"] = df["CourseCertifications?"].map({'CourseCertifications':1,'NoCourseCertifications':0})
df["IntnlConfattended?"] = df["IntnlConfattended?"].map({'AttendedIntnlConf':1,'NoIntnlConfs':0})
df["PublishedRsrchPapers?"] = df["PublishedRsrchPapers?"].map({'NoRsrchPapers':-1,'National':0,'International':1})
df["PresentedInConferences?"] = df["PresentedInConferences?"].map({'PresentedInConferences':1,'NotPresentedInConferences':0})
df["WroteTechBlogs?"] = df["WroteTechBlogs?"].map({'WroteTechBlogs':1,'NoTechBlogs':0})
df["DevelopedTechVideos?"] = df["DevelopedTechVideos?"].map({'DevelopedTechVideos':1,'NoTechVideos':0})
df["Employability?"] = df["Employability?"].map({'Good':2,'Reasonable':1,'Low':0})
data = df[["AddnlCourses?","StudyBlogs?","WriteRsrchPapers?","ListenTechVideos?","CourseCertifications?","IntnlConfattended?","PublishedRsrchPapers?","PresentedInConferences?","WroteTechBlogs?","DevelopedTechVideos?","Employability?"]].to_numpy()
inputs = data[:,:-1]
outputs = data[:, -1]
training_inputs = inputs[:1000]
training_outputs = outputs[:1000]
testing_inputs = inputs[1000:]
testing_outputs = outputs[1000:]
classifier = KNeighborsClassifier()
classifier.fit(training_inputs, training_outputs)
predictions = classifier.predict(testing_inputs)
accuracy = 100.0 * accuracy_score(testing_outputs, predictions)
print ("The accuracy of KNN Classifier on testing data is: " + str(accuracy))
testSet = [[0,0,1,0,0,0,0,0,0,0]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the first test set is:',predictions)
testSet = [[0,0,1,0,1,1,1,0,0,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the second test set is:',predictions)
testSet = [[1,1,1,0,1,1,0,1,1,1]]
test = pd.DataFrame(testSet)
predictions = classifier.predict(test)
print('KNN prediction on the third test set is:',predictions)