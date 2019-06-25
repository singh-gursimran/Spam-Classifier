from wordstem import stem_word
import time
import os
import pickle
from lower import lowstr
from htmlll import remove_html_tags
from url import remove_url
from normemail import nem
from replace import norm_no
from dollar import dollar_rvl

from nonword import nword

from indices import ind
from sklearn import svm
import numpy as np
t1=time.time()
fpathspam="C://Users//Experty//Desktop//mtest//spam"
fpathlegit="C://Users//Experty//Desktop//mtest//legitimate"
fpathtestspam="C://Users//Experty//Desktop//mtest//testdata//spam"
fpathtestlegit="C://Users//Experty//Desktop//mtest//testdata//legit"

ffspam= os.listdir(fpathspam)
fflegit= os.listdir(fpathlegit)
fftestspam= os.listdir(fpathtestspam)
fftestlegit= os.listdir(fpathtestlegit)
x=[]
y1=[]
x_test=[]
y1_test=[]

for line in ffspam:
    tt=open(fpathspam + "//" + line)

    data= tt.readlines()
    data=lowstr(data)
    data=remove_html_tags(data)
    data=remove_url(data)
    data=nem(data)
    data=norm_no(data)
    data=dollar_rvl(data)
    data= stem_word(data)
    data=nword(data)
    data=ind(data)
    x.append(data)
    y1.append(1)

for line in fflegit:
    tt=open(fpathlegit + "//" + line)

    data= tt.readlines()
    data=lowstr(data)
    data=remove_html_tags(data)
    data=remove_url(data)
    data=nem(data)
    data=norm_no(data)
    data=dollar_rvl(data)
    data= stem_word(data)
    data=nword(data)
    data=ind(data)
    x.append(data)
    y1.append(0)

for line in fftestspam:
    tt=open(fpathtestspam + "//" + line)

    data= tt.readlines()
    data=lowstr(data)
    data=remove_html_tags(data)
    data=remove_url(data)
    data=nem(data)
    data=norm_no(data)
    data=dollar_rvl(data)
    data= stem_word(data)
    data=nword(data)
    data=ind(data)
    x_test.append(data)
    y1_test.append(1)

for line in fftestlegit:
    tt=open(fpathtestlegit + "//" + line)

    data= tt.readlines()
    data=lowstr(data)
    data=remove_html_tags(data)
    data=remove_url(data)
    data=nem(data)
    data=norm_no(data)
    data=dollar_rvl(data)
    data= stem_word(data)
    data=nword(data)
    data=ind(data)
    x_test.append(data)
    y1_test.append(0)
t2=time.time()
print(t2-t1)
t1=t2
# X is the data set indices and y is the class of the email
X=np.array(x)
y=np.array(y1)
clf=svm.SVC()
clf.fit(X,y)
X_test=np.array(x_test)
y_test=np.array(y1_test)
print(time.time()-t2)
with open('classifier.pickle','wb') as pickle_out:
    pickle.dump(clf,pickle_out)
    pickle_out.close()
pickle_in=open('classifier.pickle','rb')
clf=pickle.load(pickle_in)

with open('X_test.pickle','wb') as pickle_out:

    pickle.dump(X_test,pickle_out)
    pickle_out.close()
with open('y_test.pickle','wb') as pickle_out:
    pickle.dump(y_test,pickle_out)
    pickle_out.close()
print(clf.score(X_test,y_test))



