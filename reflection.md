# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

The game looked fine when I first started it. 

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



**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input                                 | Expected Behavior | Actual Behavior | Console Output / Error |
|---------------------------------------|-------------------|-----------------|------------------------|
for normal mode (answer:60), guessed 40  Go higher           Go lower          Need to say go higher for accuracy
for easy mode (answer:71), guessed 97    Go lower            Go higher         Need to say go lower for accuracy
for hard mode (answer:12), guessed 12.5  Go lower            Correct answer    Need to say go lower 

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used Claude as my AI tool for this project. So when I fixed the bug of making the number ranges correct for level of difficulty, I changed it so that:
- Easy mode was from 1 to 20 numbers.
- Normal mode was from 1 to 50 numbers.
- Hard mode was from 1 to 100 numbers.

Good suggestion that Claude then made was, after these ranges were fixed, for the instructions to change them so that it displayed the high and low number range. Instead of just statically displaying "Guess a number from 1 to 100", it would display "Guess a number from {low} to {high}". I did listen to that suggestion because it was one of the errors that I had documented previously, and it makes the instructions clear for the user. If we were to statically keep the directions that said "guess the number from one to 100", that would have been inaccurate instructions and would have confused the user when they were trying to guess the number if they were in easy or normal mode. I verified that the results were correct by relaunching the Streamlit app to make sure, and tried with my own guesses and looked at the interface to make sure that everything was working correctly. 

One misleading thing that claude did was when I was specifically working on the bug for fixing the ranges of the numbers for the different modes.Claude then decided to also run some other tests that were part of the bug about the system incorrectly displaying whether the number should be higher or lower (a bug unrelated to what we were working on). I then basically told Claude to only focus on the test cases that were related to the bug we were trying to solve. I told it to not pay attention to the other bugs of the app currently so we could focus on the problem at hand. Then also took those tests and ran them myself to make sure that they were specific to the bug related to the ranges of the numbers. I made sure to disregard the other tests that Claude was running. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

Specifically, what I did is I first had it generate test cases through PyTest to see if everything was working correctly. For the second bug that I was solving, with the numbers being incorrect when the system was incorrectly displaying "to go higher or go lower", I had it generate test cases that I could run through my VS Code terminal. I then made sure that those test cases were passing for both of the books that I was solving. Then I ended up opening the Streamlit app so I can manually do a test. I then decided to put a number in for a guess, and I then made sure that it was the "higher or lower" that was being displayed correctly. The number I had to guess was 30. So I made sure to guess 29 to make sure that the system was telling me to go higher. It correctly did that. I then also decided to guess 31 to make sure the system would tell me to go lower, which it also correctly did. Claude specifically helped me design the Pytests, and I ran those separately to make sure they were working. I myself did the manual tests, opening Streamlit. I told Claude that I wanted to look to see if the numbers are being displayed correctly for higher or lower. It made those tests, and I read through to make sure that the logic was correct, which it was. I also took those tests separately and ran them in my own VS Code terminal. This was working correctly but I physically opened Streamlit and tested it myself to make sure everything was running right. The same thing for the other bug where it came to the ranges of the modes. Claude helped me design the PyTests, which I then ran on the VS Code terminal to make sure they were working correctly. And also I physically opened up Streamlit to make sure that everything was being displayed correctly. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
