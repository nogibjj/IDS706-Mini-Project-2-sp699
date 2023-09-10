# Test main.py

from main import people, count_col


def test_people():
    people()
    num_col = count_col()

    assert num_col == 2562


if __name__ == "__main__":
    test_people()
