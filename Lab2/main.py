import statistics as stc
import matplotlib.pyplot as plt
import pandas as pd
import stemgraphic
import seaborn as sns
import numpy as np

plt.style.use('bmh')
df = pd.read_csv('moviesfilter.csv')

# budget gross company name
x = df['budget']
y = df['gross']
z = df['company']

budget = x.to_list()
gross = y.to_list()
company = z.to_list()

#format data to million dollar
for i in range(0, len(budget)):
    budget[i] = budget[i]/1000000
for i in range(0, len(gross)):
    gross[i] = gross[i]/1000000

#Print all detail
def detail():
    print("Mean      Budget : {:.4f}".format(stc.mean(budget)))
    print("          Gross  : {:.4f}".format(stc.mean(gross)))
    print("Mode      Budget : {:.4f}".format(stc.mode(budget)))
    print("          Gross  : {:.4f}".format(stc.mode(gross)))
    print("Median    Budget : {:.4f}".format(stc.median(budget)))
    print("          Gross  : {:.4f}".format(stc.median(gross)))
    print("Deviation Budget : {:.4f}".format(stc.stdev(budget)))
    print("          Gross  : {:.4f}".format(stc.stdev(gross)))
    print("Minimum   Budget : {:.4f}".format(min(budget)))
    print("          Gross  : {:.4f}".format(min(gross)))
    print("Maximum   Budget : {:.4f}".format(max(budget)))
    print("          Gross  : {:.4f}".format(max(gross)))

def histogram():
    fig, ax = plt.subplots(1, 2, sharey=True)

    ax[0].set_xlabel('Budget (million us dollar)')
    ax[0].set_ylabel('Quantity')
    ax[0].set_title('Budget')
    ax[0].hist(budget, bins=30)

    ax[1].set_title('Gross')
    ax[1].hist(gross, bins=30)
    ax[1].set_xlabel('Gross (million us dollar)')

    plt.show()


def boxplot():
    fig, ax = plt.subplots(1, 2, sharey=True)
    ax[0].set_title('Budget')
    ax[0].boxplot(budget, vert=False)
    ax[0].set_xlabel('Budget (million us dollar)')
    ax[1].set_title('Gross')
    ax[1].boxplot(gross, vert=False)
    ax[1].set_xlabel('Gross (million us dollar)')
    plt.show()


def stem():
    stemgraphic.stem_graphic(df['budget'])
    plt.title('Budget')
    plt.show()
    stemgraphic.stem_graphic(df['gross'])
    plt.title('Gross')
    plt.show()

def scatter():
    plt.xlabel('Budget (million us dollar)')
    plt.ylabel('Gross (million us dollar)')
    plt.title('Movie industry')
    plt.scatter(budget,gross)
    plt.show()

def densityplot():
    sns.distplot(budget, hist = False, kde = True, rug = True,color = 'darkblue', kde_kws={'linewidth': 3},rug_kws={'color': 'black'})

    # Plot formatting
    plt.title('Probability Density Function')
    plt.xlabel('Budget (million us dollar)')
    plt.ylabel('Density')
    plt.show()

    sns.distplot(gross, hist = False, kde = True, rug = True,color = 'darkblue', kde_kws={'linewidth': 3},rug_kws={'color': 'black'})

    # Plot formatting
    plt.title('Probability Density Function')
    plt.xlabel('Gross (million us dollar)')
    plt.ylabel('Density')
    plt.show()

def cumulative():
    budgetData = sorted(np.array(budget))
    grossData = sorted(np.array(gross))
    budgetProb = 1. * np.arange(len(budgetData)) / (len(budgetData)-1)
    grossProb = 1. * np.arange(len(grossData)) / (len(grossData)-1)
    fig, ax = plt.subplots(1, 2)
    fig.suptitle('Cumulative Probability Function')
    ax[0].set_title('Budget')
    ax[0].plot(budgetData, budgetProb)
    ax[0].set_xlabel('Budget (million us dollar)')
    ax[0].set_ylabel('Probability')
    ax[1].set_title('Gross')
    ax[1].plot(grossData, grossProb)
    ax[1].set_xlabel('Gross (million us dollar)')
    ax[1].set_ylabel('Probability')
    plt.show()

if __name__ == "__main__":
    detail()
    # histogram()
    # boxplot()
    # stem()
    scatter()
    # densityplot()
    # cumulative()
