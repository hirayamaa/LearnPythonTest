import pytest
import cards


def test_no_path_fail():
    # TypeErrorが発生する
    cards.CardsDB()
