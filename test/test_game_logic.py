"""Tests for game logic, targeting the high/low hint bug in check_guess.

The original bug: when a guess was too high, the game told the player to
"Go HIGHER!", and when too low it said "Go LOWER!" — the hints were swapped.
"""

import os
import sys

# Allow importing logic_utils.py from the parent directory.
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from logic_utils import check_guess


def test_too_high_guess_tells_player_to_go_lower():
    """A guess above the secret must hint LOWER, not higher."""
    outcome, message = check_guess(97, 71)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_too_low_guess_tells_player_to_go_higher():
    """A guess below the secret must hint HIGHER, not lower."""
    outcome, message = check_guess(40, 60)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_correct_guess_wins():
    """An exact match should be a win regardless of the hint logic."""
    outcome, message = check_guess(12, 12)
    assert outcome == "Win"


def test_hint_direction_is_not_swapped():
    """Explicit guard against the regression: hints must match direction."""
    _, too_high_msg = check_guess(80, 50)
    _, too_low_msg = check_guess(20, 50)
    # The "too high" message should never tell the player to go higher.
    assert "HIGHER" not in too_high_msg
    # The "too low" message should never tell the player to go lower.
    assert "LOWER" not in too_low_msg
