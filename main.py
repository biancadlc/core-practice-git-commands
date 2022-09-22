import pytest


def always_returns_true():
<<<<<<< HEAD
    print("Always returns True!")
    return True
=======
    return None
>>>>>>> c55355964ef3a782a2e1276d8ee22bf7528fa22b


def test_always_returns_true():
    assert always_returns_true()
