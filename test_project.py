from project import decide, get_stats, check_winner




def test_decide():
    # Ties
    assert decide("Rock", "Rock") == "Tie"
    assert decide("Paper", "Paper") == "Tie"
    assert decide("Scissors", "Scissors") == "Tie"


    # Wins
    assert decide("Rock", "Scissors") == "Win"
    assert decide("Paper", "Rock") == "Win"
    assert decide("Scissors", "Paper") == "Win"


    # Losses
    assert decide("Rock", "Paper") == "Lose"
    assert decide("Paper", "Scissors") == "Lose"
    assert decide("Scissors", "Rock") == "Lose"




def test_get_stats():
    assert get_stats([]) == (0, 0)


    hist = [
        "Rock vs Scissors = Win",
        "Paper vs Rock = Win",
        "Scissors vs Rock = Lose",
        "Rock vs Rock = Tie",
    ]
    assert get_stats(hist) == (2, 1)


    all_ties = ["Rock vs Rock = Tie", "Paper vs Paper = Tie"]
    assert get_stats(all_ties) == (0, 0)




def test_check_winner():
    assert check_winner([0, 0]) is None
    assert check_winner([3, 4]) is None
    assert check_winner([5, 2]) == "You"
    assert check_winner([2, 5]) == "Computer"


