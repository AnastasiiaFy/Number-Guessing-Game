# Number-Guessing-Game

## Introduction

Welcome to the Number Guessing game! The goal of this command-line game is to guess the number thought out by the computer. Three levels of difficulty are available to you, which will determine how many chances you have to guess the number:
1. Easy - 10 chances
2. Medium - 5 chances
3. Hard - 3 chances

The number will be in the range of 1 to 100 in the first round, but with each subsequent round, range will rise. After each round, you can either finish the game or choose to play on. When you decide to finish the game, the table showing the top attempts at each difficulty level will be shown.

## How to run
1. Open a terminal or command line.
2. Clone the Repository:
```
git clone https://github.com/AnastasiiaFy/Number-Guessing-Game.git
```
3. Go to the folder with the code:
```
cd Number-Guessing-Game
```
4. Run the code:
```
python3 main.py
```

## Output example
```
	Hi! Welcome to the NUMBER GUESSING GAME
	So, the rules of our game are as follows:
	I guess a number from 1 to 100
	You have to guess it in a limited number of chances.
	Every next round the range of numbers will increase!
		Good luck!

Please select the difficulty level:
 1. Easy level - 10 chances
 2. Medium level - 5 chances
 3. Hard level - 3 chances 

Enter the number of the selected level (1, 2 or 3) - 3
Greate! You have selected hard difficulty level.

	The number is thought of.

Enter your guess (from 1 to 100) - 50
Incorrect! Number is large than 50.

Enter your guess (from 1 to 100) - 75
Incorrect! Number is less than 75.

Enter your guess (from 1 to 100) - 63
Incorrect! Number is large than 63.

Sorry, you've run out of chances. The correct number was 73.

Вo you want to move on to the next round? (yes/no) - no
Thanks for playing. I hope you enjoyed it.

----------------------------------------------------------------------------
|                                HIGH SCORE                                |
----------------------------------------------------------------------------
|    Level     |       Easy        |      Medium       |       Hard        |
----------------------------------------------------------------------------
| Best attempt |        inf        |        inf        |        inf        |
----------------------------------------------------------------------------

```

## Challenge
This project is a task from [roadmap.sh](https://roadmap.sh/projects/number-guessing-game). The objective was to create a game that met specific requirements.

## Feedback

