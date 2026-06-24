import os
import sys

# Make the project root importable so we can test the real functions in app.py.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import check_guess, update_score, get_range_for_difficulty


# --- Basic check_guess behavior -------------------------------------------
# app.py's check_guess returns a (outcome, message) tuple, so we unpack it.

def test_winning_guess():
    # Secret 50, guess 50 -> Win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # Secret 50, guess 60 -> Too High
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    # Secret 50, guess 40 -> Too Low
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug: lexicographic comparison ----------------------------------------
# The old code stringified the secret on even-numbered attempts, so check_guess
# compared strings. As strings, "12" < "9" is True, so a guess of 12 against a
# secret of 9 was wrongly reported as "Too Low". The fix compares numerically.

def test_check_guess_is_numeric_not_lexicographic():
    outcome, _ = check_guess(12, 9)
    assert outcome == "Too High"


# --- Bug: wrong guess could increase the score ----------------------------
# "Too High" on an even-numbered attempt used to ADD 5 points. A wrong guess
# should always cost points, matching the "Too Low" branch.

def test_too_high_never_increases_score():
    assert update_score(100, "Too High", 2) == 95


def test_too_low_decreases_score():
    assert update_score(100, "Too Low", 2) == 95


# --- Bug: win scoring off-by-one ------------------------------------------
# Winning on the first attempt should be a perfect score, not penalized.

def test_first_guess_win_is_perfect_score():
    assert update_score(0, "Win", 1) == 100


# --- Bug: difficulty was inverted -----------------------------------------
# Hard's range was narrower (1-50) than Normal's (1-100), making Hard easier.
# After the fix, Hard's range must be at least as wide as Normal's.

def test_hard_range_is_not_easier_than_normal():
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high >= normal_high
