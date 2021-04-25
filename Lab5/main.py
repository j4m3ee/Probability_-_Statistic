import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

plt.style.use('bmh')
df = pd.read_csv('moviesfilter.csv')

# budget gross company name
x = df['budget']
y = df['gross']
z = df['company']

budget = x.to_list()
gross = y.to_list()
company = z.to_list()

# format data to million dollar
for i in range(0, len(budget)):
    budget[i] = budget[i]/1000000
for i in range(0, len(gross)):
    gross[i] = gross[i]/1000000

def regression_line():
    # W is regression coefficients
    X = np.vstack((budget,np.ones(len(budget)))).T
    W = np.linalg.inv(X.T @ X) @ X.T @ gross

    plt.xlabel('Budget (million us dollar)')
    plt.ylabel('Gross (million us dollar)')
    plt.title('Movie profits')
    plt.scatter(budget, gross)

    # z is Predicted vector
    z = X @ W

    plt.plot(budget, z, color='r')

    print('Estimated coefficients = {:.4f} + {:.4f}X'.format(W[1],W[0]))
    plt.show()

if __name__ == "__main__":
    regression_line()
