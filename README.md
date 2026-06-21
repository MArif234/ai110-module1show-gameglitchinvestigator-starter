# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.

The purpose of the game is to guess the number. There are three modes:
- easy mode
- normal mode
- hard mode
- In easy mode, you are guessing a number between the range of 1 to 20.
- For normal mode, you are guessing in the range of 1 to 50.
- In hard mode, you are guessing in the range of 1 to 100.
Basically, how it's supposed to work is that you're supposed to enter a number based on the mode that you're in, and then the system will tell you whether you need to go higher for your gas or lower. You have a certain number of tries to guess the right number, and you will be losing points if your guesses are wrong, and you'll be gaining points if your guesses are right. The purpose of this game is to guess the right number. 
- [ ] Detail which bugs you found.

Problem #1:

When it specifically comes to the three levels of difficulty, it seems a bit confusing. Easy mode of the game: it makes sense that the range is one to twenty because you're guessing between twenty numbers, so that seems correct. However, from the normal mode of the game, the range is 1 to 100. For the hard mode of the game, the ranges went 1 to 50. For this specific game, I do not feel like that is accurate. I believe that for the Normal Mode, the range should be between 1 and 50, and Hard Mode should be 1 to 100. It's harder to guess a number when you have 100 numbers versus 50 numbers, so I believe that part of the game has a bug. 

Problem #2:

Next error is that it just straight up won't let me start a new game. I had run out of my attempts for a game in normal mode, and whenever I click the new game button in any of the modes, it does not work. I have to refresh the page to start a new game. 

Problem #3:

When I was attempting different things in the different modes, when I'm guessing a number that is lower than the actual number, there are errors where it's telling me to actually go higher, which is incorrect. Similarly, when I'm entering numbers that are higher than the number I need to guess, it's actually telling me to go higher when it should be telling me to go lower. It's not reading the numbers correctly, and it's not accurately giving you a hint on whether you should be going higher or lower. 

Problem #4:

Another bug that I noticed is specifically with the instructions. For easy mode, the sidebar is saying that the range is between 1 and 20. However, on the main screen where the game is being played, it's saying that the range is one to 100. That is confusing for the user. For normal mode, that range is fine because they are both consistently saying 1 to 100. Same problem for Hard mode, where the sidebar is saying that the range is 1:50, but the actual game instructions are saying that the range is 1:100. In fact, the instructions, the actual number, also aren't following the rules on the sidebar. All of the numbers, regardless of the mode, are being chosen randomly from 1 to 100 when there should be certain ranges for easy, hard, and normal modes. For example, in hard mode, it is saying that the range is 1 to 50, but the secret number that needs to be guessed is 80. The instructions are quite inconsistent. 

Problem #5:

When it comes to guessing the number, if you are at an even number attempt for guessing the number and you guess too high, the program adds points to your score when you shouldn't be earning any points. Too high a guess is always wrong, so it should always be decreasing the score, not increasing it. This is also an error. Only happens when you're at an even-numbered attempt. If it's your second attempt, your fourth attempt, your sixth attempt, you get the point. 

- [ ] Explain what fixes you applied.

The two specific bugs that I focused on were:
1. The ranges of the different modes
2. The fact that the system was saying "higher" or "lower" incorrectly

I used Claude as my AI tool for this project. So when I fixed the bug of making the number ranges correct for level of difficulty, I changed it so that:
- Easy mode was from 1 to 20 numbers.
- Normal mode was from 1 to 50 numbers.
- Hard mode was from 1 to 100 numbers.

Good suggestion that Claude then made was, after these ranges were fixed, for the instructions to change them so that it displayed the high and low number range. Instead of just statically displaying "Guess a number from 1 to 100", it would display "Guess a number from {low} to {high}". I did listen to that suggestion because it was one of the errors that I had documented previously, and it makes the instructions clear for the user. If we were to statically keep the directions that said "guess the number from one to 100", that would have been inaccurate instructions and would have confused the user when they were trying to guess the number if they were in easy or normal mode. I verified that the results were correct by relaunching the Streamlit app to make sure, and tried with my own guesses and looked at the interface to make sure that everything was working correctly. 

For the second bug that I was solving, with the numbers being incorrect when the system was incorrectly displaying "to go higher or go lower", I had it generate test cases that I could run through my VS Code terminal. I then made sure that those test cases were passing for both of the books that I was solving. Then I ended up opening the Streamlit app so I can manually do a test. I then decided to put a number in for a guess, and I then made sure that it was the "higher or lower" that was being displayed correctly. The number I had to guess was 30. So I made sure to guess 29 to make sure that the system was telling me to go higher. It correctly did that. I then also decided to guess 31 to make sure the system would tell me to go lower, which it also correctly did. 

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 6
2. Game returns "Go Higher"
3. User enters a guess of 9 → "Too High"
4. Score updates correctly after each guess
5. Game ends after the correct guess or if all attempts used

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
# Paste your pytest output here, e.g.:
# pytest tests/
# ========================= X passed in 0.XXs =========================

Pytests for the ranges of different modes: 

tests/test_game_logic.py::test_easy_range PASSED                                                                                        [ 14%]
tests/test_game_logic.py::test_normal_range PASSED                                                                                      [ 28%]
tests/test_game_logic.py::test_hard_range PASSED                                                                                        [ 42%]
tests/test_game_logic.py::test_ranges_increase_with_difficulty PASSED                                                                   [ 57%]
tests/test_game_logic.py::test_winning_guess FAILED                                                                                     [ 71%]
tests/test_game_logic.py::test_guess_too_high FAILED                                                                                    [ 85%]
tests/test_game_logic.py::test_guess_too_low FAILED                                                                                     [100%]

NOTE: The last 3 failed for this specific part because I had not fixed the other bug with the system incorrectly displaying higher or lower for the number guesses. This error was fixed when I fixed the bug of the hints displaying correctly.

Pytests for Fixing High/Low Bugs:

plugins: anyio-4.14.0
collected 4 items                                                                                                                             

test/test_game_logic.py::test_too_high_guess_tells_player_to_go_lower PASSED                                                            [ 25%]
test/test_game_logic.py::test_too_low_guess_tells_player_to_go_higher PASSED                                                            [ 50%]
test/test_game_logic.py::test_correct_guess_wins PASSED                                                                                 [ 75%]
test/test_game_logic.py::test_hint_direction_is_not_swapped PASSED                                                                      [100%]


```

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, describe the Enhanced UI changes here — a screenshot is optional]
