import re
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import collections



def calculateBOW(wordset,l_doc):
    tf_diz = dict.fromkeys(wordset, 0)
    for word in l_doc:
        tf_diz[word] = l_doc.count(word)
    return tf_diz


#
# Create sample set of documents
#
doc1 = 'Game of Thrones is an amazing tv series!'
doc2 = 'Game of Thrones is the best tv series!'
doc3 = 'Game of Thrones is so great'
doc4 = 'Mirabai has won a silver medal in weight lifting in Tokyo olympics 2021' \
       ' Sindhu has won a bronze medal in badminton in Tokyo olympics' \
       ' Indian hockey team is in top four team in Tokyo olympics 2021 after 40 years'
#
# Lists of docs
#
l_doc1 = re.sub(r"[^a-zA-Z0-9]", " ", doc1.lower()).split()
l_doc2 = re.sub(r"[^a-zA-Z0-9]", " ", doc2.lower()).split()
l_doc3 = re.sub(r"[^a-zA-Z0-9]", " ", doc3.lower()).split()
l_doc4 = re.sub(r"[^a-zA-Z0-9]", " ", doc4.lower()).split()

wordset = list(set(l_doc1 + l_doc2 + l_doc3 + l_doc4))

bow1 = calculateBOW(wordset, l_doc1)
bow2 = calculateBOW(wordset, l_doc2)
bow3 = calculateBOW(wordset, l_doc3)
bow4 = calculateBOW(wordset, l_doc4)
df_bow = pd.DataFrame([bow1, bow2, bow3, bow4])
print(f'df_bow.head():\n{df_bow.head()}')

#
# Use Vectorizer with stopwords-filter
#
vectorizer = CountVectorizer(stop_words='english')
X = vectorizer.fit_transform([doc1, doc2, doc3, doc4])
df_bow_sklearn = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
print(f'df_bow.sklearn.head()\n: {df_bow_sklearn.head()}')

#
# Get unique words / tokens found in all the documents. The unique words / tokens represents
# the features
#
print(vectorizer.get_feature_names_out())
#
# Associate the indices with each unique word
#
print(vectorizer.vocabulary_)
#
# Print the numerical feature vector
#
print(bag.toarray())
#
# Creating training data set from bag-of-words  and dummy label
#
X = bag.toarray()
y = np.array([1, 1, 0, 0, 1, 1])

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

#
# Create training and test split
#
X_train, X_test, y_train, y_test = train_test_split(X, y)
#
# Create an instance of LogisticRegression classifier
#
lr = LogisticRegression(C=100.0, random_state=1, solver='lbfgs', multi_class='ovr')
#
# Fit the model
#
lr.fit(X_train, y_train)
#
# Create the predictions
#
y_predict = lr.predict(X_test)

# Use metrics.accuracy_score to measure the score
print("LogisticRegression Accuracy %.3f" % metrics.accuracy_score(y_test, y_predict))