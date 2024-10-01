 # Number Guessing Game

## Introduction

Welcome to the Number Guessing Game! This interactive game allows players to guess a randomly generated number between 1 and 100. Players can choose between two difficulty levels: easy and hard, affecting the number of attempts available. The game provides hints about whether the guessed number is too high or too low, and additional information about the generated number.

## Features

- Randomly generates a number between 1 and 100.
- Difficulty levels:
  - **Easy**: 10 attempts
  - **Hard**: 5 attempts
- Provides hints about the number:
  - Whether it is even or odd.
  - Whether it is divisible by 5.
- Option to exit the game at any time.

## How It Works

1. The player selects the difficulty level.
2. The program generates a random number.
3. The player has a limited number of attempts to guess the number.
4. After each guess, the program indicates whether the guess is too high or too low.
5. The game provides information about the generated number.
6. The player can choose to continue or exit the game.

## Example Output
    ***** Welcome to number guessing game *****
    I am thinking of a number between 1 and 100
    choose difficulty: "easy" or "hard": easy
    you have 10 attempts left
    
    about number:
        is_even: True
        is_divisible_by_5: yes
    
    make a guess: 50
    too high
    you have 9 attempts left
    
    make a guess: 30 
    You got it! The answer was 30    
    type "e" to exit else continue:

   
## How to Run

1. Clone or download the repository.
2. Make sure you have Python installed on your machine.
3. Run the script in your terminal:
   ```bash
   python guess_the_number.py
4. Follow the on-screen instructions to play the game.

## License
This project is open-source and can be modified or distributed freely.


