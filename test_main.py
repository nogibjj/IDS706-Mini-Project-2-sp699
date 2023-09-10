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
