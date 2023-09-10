# Test main.py

import main as count_col, count_row


def test_count_col():
    count_col()
    num_col = count_col()
    assert num_col == 6


def test_count_row():
    count_row()
    num_row = count_row()
    assert num_row == 15723


if __name__ == "__main__":
    test_count_col()
    test_count_row()
