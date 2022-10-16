# importing libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.metrics import pairwise_distances
from sklearn.metrics.pairwise import euclidean_distances
from scipy.spatial import distance
import pandas as pd
import numpy as np


## Converting 3D array of array into 1D array
def arr_convert_1d(arr):
    arr = np.array(arr)
    arr = np.concatenate(arr, axis=0)
    arr = np.concatenate(arr, axis=0)
    return arr


## Cosine Similarity
cos = []


def cosine(trans):
    cos.append(cosine_similarity(trans[0], trans[1]))


## Manhattan Distance
manhatten = []


def manhatten_distance(trans):
    manhatten.append(pairwise_distances(trans[0], trans[1],
                                        metric='manhattan'))


## Euclidean Distance
euclidean = []


def euclidean_function(vectors):
    euc = euclidean_distances(vectors[0], vectors[1])
    euclidean.append(euc)


# This Function finds the similarity between two
# sentences by using above functions.

## TF - IDF
def tfidf(str1, str2):
    ques = []
    # You have to provide the dataset. Link of the dataset
    # is given in the end of this article.
    # and if you are using a different dataset then adjust
    # it according to your dataset's columns and rows
    dataset = pd.read_csv('quora_duplicate_questions.tsv',
                          delimiter='\t', encoding='utf-8')
    print(f'dataset.head(11):\n{dataset.head(11)}')
    x = dataset.iloc[:, 1:5]
    x = x.dropna(how='any')

    for k in range(len(x)):
        for j in [2, 3]:
            ques.append(x.iloc[k, j])
    vect = TfidfVectorizer()
    # Fit the your whole dataset. After all, this'll
    # produce the vectors which is based on words in corpus/dataset
    vect.fit(ques)

    corpus = [str1, str2]
    trans = vect.transform(corpus)

    euclidean_function(trans)
    cosine(trans)
    manhatten_distance(trans)
    return convert()


def convert():
    dataf = pd.DataFrame()
    lis2 = arr_convert_1d(manhatten)
    dataf['manhatten'] = lis2
    lis2 = arr_convert_1d(cos)
    dataf['cos_sim'] = lis2
    lis2 = arr_convert_1d(euclidean)
    dataf['euclidean'] = lis2
    return dataf


newData = pd.DataFrame();
str1 = "hello i am pulkit"
str2 = "your name is akshit"
newData = tfidf(str1, str2)
print(newData)
