Rock Paper Scissors
Video Demo: https://youtu.be/2zgu6au7cU0
Description:


Rock Paper Scissors is a graphical desktop game built in Python that lets a user play the classic hand game against the computer. Instead of running purely in the terminal like most of the CS50P problem sets, this project uses Python's built-in tkinter library to create a real windowed application: the player clicks buttons labeled "Rock," "Paper," and "Scissors" to make a move, the computer responds with a random choice of its own, and the outcome of each round is displayed on screen along with a running score and a scrollable history of recent rounds. The first player to reach five points wins the match, at which point the game locks the move buttons and enables a "Restart" button so a new match can begin.


I built this project because I wanted my final project to go beyond a terminal-based script and actually produce something with a real interface — something that felt like a finished, usable application rather than just a program you run once and read the output of. Rock Paper Scissors was a good fit for that goal: the rules are simple enough that I could focus my effort on the interface and the software design, rather than spending most of my time puzzling out game logic.


How It Works


The game keeps track of three pieces of state while it runs: the running score (a two-item list holding the player's and computer's points), a list of the last several rounds played (used to build the on-screen history and to calculate win/loss stats), and whatever move the player most recently clicked. Every time the player clicks a move button, the program picks a random move for the computer, compares the two moves to determine a winner, updates the score and history accordingly, and refreshes every label and text box on screen to reflect the new state. Once either score reaches five, the game disables further moves and declares a winner.


Project Structure


This project consists of three files in its root directory:


project.py — Contains the main function, which launches the game window, along with three additional functions that were deliberately written as pure functions with no dependency on tkinter:
decide(plyr, cpu) determines the outcome ("Win," "Lose," or "Tie") of a single round given the player's and computer's moves.
get_stats(hist) takes the list of round-history strings and returns a tuple of (wins, losses), which is displayed alongside the score.
check_winner(sc) checks the current score and returns "You" or "Computer" once one side reaches five points, or None if the match is still in progress.
All of the tkinter window setup, button callbacks, and label updates live inside a build_gui() helper function, which main() calls. Keeping the GUI code separate from the three functions above was a deliberate design choice, explained further below.
test_project.py — Contains pytest tests for each of the three functions above: test_decide, test_get_stats, and test_check_winner. Each test checks multiple cases, including edge cases like an empty history list and a tied round.
README.md — This file.


This project has no external dependencies beyond the Python standard library (tkinter for the interface and random for the computer's moves), so no requirements.txt file was necessary.


Design Decisions


The most important design decision in this project was separating the game's core logic from its graphical interface. My first working version of this game had all of its logic embedded directly inside the tkinter callback functions — for example, the code that decided who won a round lived inside the same function that updated the on-screen labels. That version worked perfectly well as a game, but it created a real problem for this assignment: CS50P requires that project functions be testable with pytest, and functions that directly reference tkinter widgets are difficult to test in isolation, since doing so would require spinning up an actual graphical window during testing.


To resolve this, I refactored the project so that all of the decision-making logic — who wins a round, how to tally wins and losses, and whether someone has reached the winning score — lives in small, pure functions that take plain Python values as input (strings, lists) and return plain Python values as output. The tkinter code then simply calls these functions and uses their return values to update the display. This separation made the project both easier to test and, I found, easier to reason about generally: when I wanted to change a rule (for example, experimenting with a different winning score during development), I only had to change one small function rather than hunt through GUI callback code.


I also chose to cap the visible round history at ten entries rather than letting it grow indefinitely, since an unbounded scrolling list felt less useful than a short, readable recent history once a match ran long.


Challenges and What I Learned


The biggest challenge in this project was learning to think about my code in terms of what could and couldn't be unit tested, and restructuring around that constraint rather than around what was easiest to write first. It would have been simpler to leave all my logic embedded in the GUI callbacks, but doing so would have left me with nothing meaningfully testable. Pulling the game rules out into standalone functions took some upfront refactoring, but it left me with a cleaner, more maintainable codebase — a lesson I expect to carry into future projects.


I also spent time working through tkinter specifics I hadn't used before this course, including managing widget state (enabling and disabling buttons based on game state) and formatting a scrolling text widget to display a running history.


How to Run It


This project requires no external libraries — only a standard installation of Python 3, which includes tkinter. To play:


python project.py


To run the test suite:


pytest test_project.py


