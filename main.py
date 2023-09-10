# Main.py using pandas and matplotlib to set data and see some plot

import pandas as pd
import matplotlib as plt

stat_df = pd.read_csv("Statistics_Test.csv")


# Mean, Median, Standard Deviation
def people(data):
    age = stat_df["Age"]
    age_mean = age.mean()
    age_median = age.median()
    age_std = age.std()
    return


# Make a plot to Histogram of Age column
def create_hist(data):
    plt.hist(stat_df["AGE"], bins=10, color="blue", edgecolor="white")
    plt.xlabel("AGE")
    plt.ylabel("Frequency")
    plt.title("Age Histogram")
    plt.show()
    plt.savefig("age_hist.png")
    return
