import pytest
from grades import average, letter_grade


def test_average_of_three_scores():
    assert average([80, 90, 100]) == 90


def test_average_of_empty_list_raises_error():
    with pytest.raises(ValueError):
        average([])


def test_exactly_90_is_an_a():
    assert letter_grade(90) == "A"


def test_89_is_a_b():
    assert letter_grade(89) == "B"


def test_score_above_100_raises_error():
    with pytest.raises(ValueError):
        letter_grade(101)