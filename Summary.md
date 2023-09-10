### < Summary of Statistics_Test.csv >

#### Python Code
* `main.py`
```# Main.py using pandas and matplotlib to set data and see some plot

import pandas as pd
import matplotlib.pyplot as plt

stat_df = pd.read_csv("Statistics_Test.csv")


# Mean, Median, Standard Deviation
def people():
    age = stat_df["AGE"]
    age_mean = age.mean()
    age_median = age.median()
    age_std = age.std()
    print(f"Mean = {age_mean}, Median = {age_median}, Standard Deviation = {age_std}")
    return


# Count columns for test
def count_col():
    num_col = len(stat_df.columns)
    return num_col


# Count rows for test
def count_row():
    num_row = len(stat_df)
    return num_row


# Make a plot to Histogram of Age column
def create_hist():
    plt.hist(stat_df["AGE"], bins=10, color="blue", edgecolor="white")
    plt.xlabel("AGE")
    plt.ylabel("Frequency")
    plt.title("Age Histogram")
    plt.savefig("age_hist.png")
    plt.show()
    return


people()
create_hist()
```

* `test_main.py`
```
# Test main.py

import main


def test_count_col():
    num_col = main.count_col()
    assert num_col == 6


def test_count_row():
    num_row = main.count_row()
    assert num_row == 15723


if __name__ == "__main__":
    test_count_col()
    test_count_row()
```


#### Statistics of Age
The following are the statistical values of the ages of all individuals in the given data.</br>
- `Mean` = 44.6958</br>
- `Medain` = 46.0</br>
- `Standard Deviation` = 12.8772</br>

</br>

#### Histogram of Age
The following histogram was created to visualize the distribution of ages.</br>

![age_hist](https://github.com/suim-park/Mini-Project-2/assets/143478016/91afeb26-d8f4-4bfb-bbf5-259425e8dee0)
