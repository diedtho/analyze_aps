import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier

clf1 = LogisticRegression(max_iter=1000, random_state=123)
clf2 = RandomForestClassifier(n_estimators=100, random_state=123)
clf3 = GaussianNB()
X = np.array([[-1.0, -1.0], [-1.2, -1.3], [-1.4, -2.2], [2.1, 2.2]])
y = np.array([1, 1, 2, 2])

eclf = VotingClassifier(estimators=[('lr', clf1), ('rf', clf2), ('gnb', clf3)],
                        voting='soft',
                       weights=[1, 2, 3])

# Predict the class probabilities for all classifiers:
probas = [c.fit(X, y).predict_proba(X) for c in (clf1, clf2, clf3, eclf)]

# Get the class probabilities for the sample dataset:
class1_1 = [pr[0, 0] for pr in probas]
class2_1 = [pr[0, 1] for pr in probas]

# Plot the probabilities:
N = 4 # Number of groups in the array
ind = np.arange(N) # Group positions
width = 0.275 # Bar graph width

# Create a matplotlib subplots for each bar graph:
fig, ax = plt.subplots()

# Create a bar graph for each classifier:
p1 = ax.bar(ind, np.hstack(([class1_1[:-1], [0]])), width,
            color='red', edgecolor='k')
p2 = ax.bar(ind + width, np.hstack(([class2_1[:-1], [0]])), width,
            color='blue', edgecolor='k')

# Create a bar graph for the VotingClassifier estimated average:
p3 = ax.bar(ind, [0, 0, 0, class1_1[-1]], width,
            color='red', edgecolor='k')
p4 = ax.bar(ind + width, [0, 0, 0, class2_1[-1]], width,
            color='blue', edgecolor='k')

# Create plot annotations to add descriptive text:
plt.axvline(2.8, color='k', linestyle='dashed')
ax.set_xticks(ind + width)
ax.set_xticklabels(['LogisticRegression\nweight 1',
                    'GaussianNB\nweight 2',
                    'RandomForestClassifier\nweight 3',
                    'VotingClassifier\n(average probabilities)'],
                   rotation=40,
                   ha='right')
plt.ylim([0, 1])
plt.title('Class Probabilities for a Sample, Predicted by Different Classifiers')
plt.legend([p1[0], p2[0]], ['class 1', 'class 2'], loc='upper left')
plt.tight_layout()
plt.show()