# Test main.py

from main import people


def test_people():
    result = people()

    plt.hist(stat_df["AGE"])
    plt.show()

    max_value = max(result["GDP rate"])
    assert max_value == 3.1


if __name__ == "__main__":
    test_GDP()
