import pandas as pd
from sklearn.datasets import load_iris

data = load_iris()
print(data.target[[10, 25, 50]])
print(list(data.target_names))
print(list(data.items()))

df_data = pd.DataFrame(data.data, columns=['sepal-length', 'sepal-width', 'petal-length', 'petal-width'])
print(df_data)
df_targets = pd.DataFrame(data.target, columns=['Class'])
print(df_targets)
df_full = pd.concat([df_data, df_targets], axis=1)
df_full.to_csv('iris.csv', encoding='utf8', sep=';', index=False)


