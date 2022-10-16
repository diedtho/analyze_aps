# Import the linear regression model:
from sklearn import linear_model

linreg = linear_model.LinearRegression()

# Use the linear regression model to fit data:
linreg.fit ([[0, 0], [2, 2], [4, 4]], [0, 2, 4])

# Run the model and return a  point fitted to the data
# and projected on the same line:
print(linreg.coef_)