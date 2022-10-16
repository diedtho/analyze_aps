import json
import re
import docx2txt
import textract as textract
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
with open('sample_text.txt', 'r', encoding='utf8') as fr:
    doc1 = fr.read()
doc2 = docx2txt.process('Gliederung_der_Projektdokumentation_Stichpunkte.docx', 'tmp')

#
# Lists of docs
#
l_doc1 = re.sub(r"[^a-zA-Z0-9]", " ", doc1.lower()).split()
l_doc2 = re.sub(r"[^a-zA-Z0-9]", " ", doc2.lower()).split()


wordset = list(set(l_doc1 + l_doc2))

bow1 = calculateBOW(wordset, l_doc1)
bow2 = calculateBOW(wordset, l_doc2)
df_bow = pd.DataFrame([bow1, bow2])
print(f'df_bow.head():\n{df_bow.head()}')

#
# Use Vectorizer with stopwords-filter
#
with open('german_stopwords.txt', 'r', encoding='utf8') as fr:
    stopwords_loaded = fr.readlines()
vectorizer = CountVectorizer(stop_words=stopwords_loaded)
X = vectorizer.fit_transform([doc1, doc2])
df_bow_sklearn = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df_bow_sklearn.to_csv('df_bow_sklearn.csv', encoding='utf8', sep=';')
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
vectorizer = CountVectorizer(stop_words=stopwords_loaded, ngram_range=(2, 2))
X = vectorizer.fit_transform([doc1, doc2])
df_bow_sklearn = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
df_bow_sklearn.to_csv('df_bow_sklearn_2grams.csv', encoding='utf8', sep=';')
print(f'df_bow.sklearn.head()\n: {df_bow_sklearn.head()}')

#
#
#

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn import metrics

X = df_bow_sklearn[:, [0, 2]]
print(f'X: {X}')
y = np.array([1, 2, 0])

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