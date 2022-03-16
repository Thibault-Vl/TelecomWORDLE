#  Copyright (c) 2022/3/16.

# Import personal package
from app.core.checkWinCondition import checkWinCondition


def test_first_checkWinCondition():
    # First set of tests
    requiredWord = "test"
    userWord = "tete"
    currentTries = 7

    data = checkWinCondition(userWord, requiredWord, currentTries, 5)

    assert type(data) == dict
    assert data['statement'] == False
    assert data['winStatement'] == False
    assert data['css'][0] == "good-place"
    assert data['css'][1] == "good-place"
    assert data['css'][2] == "bad-place"
    assert data['css'][3] == "not-found"


def test_second_checkWinCondition():
    # Second set of tests
    requiredWord = "test"
    userWord = "test"
    currentTries = 5

    data = checkWinCondition(userWord, requiredWord, currentTries, 5)

    assert type(data) == dict
    assert data['statement'] == False
    assert data['winStatement'] == True
    assert data['css'][0] == "good-place"
    assert data['css'][1] == "good-place"
    assert data['css'][2] == "good-place"
    assert data['css'][3] == "good-place"


def test_third_checkWinCondition():
    # Third set of tests
    requiredWord = "test"
    userWord = "tire"
    currentTries = 5

    data = checkWinCondition(userWord, requiredWord, currentTries, 5)

    assert type(data) == dict
    assert data['statement'] == True
    assert data['winStatement'] == False
    assert data['css'][0] == "good-place"
    assert data['css'][1] == "not-found"
    assert data['css'][2] == "not-found"
    assert data['css'][3] == "bad-place"


def test_fourth_checkWinCondition():
    # Fourth set of tests
    requiredWord = "test"
    userWord = "timer"
    currentTries = 5

    with pytest.raises(AssertionError):
        checkWinCondition(userWord, requiredWord, currentTry=currentTries, maxTries=5)
