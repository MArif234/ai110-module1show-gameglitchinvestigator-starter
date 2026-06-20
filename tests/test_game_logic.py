import pytest

from logic_utils import check_guess, get_range_for_difficulty


# --- get_range_for_difficulty: ranges must grow with difficulty ---
# The original bug: Easy=1-20, Normal=1-100, Hard=1-50, so Hard's range
# was SMALLER than Normal's. After the fix the upper bound should increase
# monotonically: Easy < Normal < Hard.

def test_easy_range():
    assert get_range_for_difficulty("Easy") == (1, 20)

def test_normal_range():
    assert get_range_for_difficulty("Normal") == (1, 50)

def test_hard_range():
    assert get_range_for_difficulty("Hard") == (1, 100)

def test_ranges_increase_with_difficulty():
    # This is the assertion the original buggy code FAILED.
    _, easy_high = get_range_for_difficulty("Easy")
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert easy_high < normal_high < hard_high


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"
