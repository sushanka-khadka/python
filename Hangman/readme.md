# Hangman Game

This is a simple command-line Hangman game implemented in Python. The game randomly selects a word, and the player has to guess the word one letter at a time. If the player guesses incorrectly, they lose a life. The game ends when the player either guesses the word or loses all their lives.

## Features
- Displays the classic Hangman stages as the player loses lives.
- Checks for already guessed letters to prevent repeated guesses.
- Provides feedback on the number of remaining lives.
- Displays the chosen word after the game ends, whether the player wins or loses.

## Requirements

Make sure you have the following dependencies:
- `hangman_art`: This module contains the visual representation for the Hangman stages.
- `hangman_words`: This module contains the list of words used in the game.

## How to Run
1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the Python script:
    ```bash
    python hangman.py

## Game Instructions
  1. The game will show a series of underscores representing the letters in the word.
  2. Enter a letter to guess the word. If the letter is in the word, it will replace the corresponding underscores.
  3. Each incorrect guess will reduce your remaining lives.
  4. The game ends when:
      - You guess the word correctly, and you win!
      - You run out of lives, and you lose.
  5. The number of lives is limited to 6.
    
Good luck, and have fun!

## Example
    ```bash 
    Welcome to Hangman!
    _ _ _ _ _ _ 
    Total lives:  6
    Guess a letter: e
    _ _ e _ _ _
    Lives left: 5
        -----
       |     |
       |     O
       |      
       |     
       |     
       |     
       |     
    ---|---
    
    Guess a letter: a
    a _ e _ _ _
    Lives left: 5
        -----
       |     |
       |     O
       |      
       |     
       |     
       |     
       |     
    ---|---

## License
This project is open-source and can be modified or distributed freely.
```bash	
This README provides an overview of how the program works, the features, and the example usage.
