# Rock-Paper-Scissors Game

This is a simple Rock-Paper-Scissors game implemented in Python where the user plays against the computer. The game follows the traditional rules, and the user can make a selection from the available choices of **rock**, **paper**, **scissors**, or choose to **exit** the game.

## How to Run the Game

1. Make sure you have Python installed.
2. Save the Python script as `rock_paper_scissors.py`.
3. Run the script using Python:
    ```bash
    python rock_paper_scissors.py

## Game Instructions
  After running the script, you will see a menu with the following options:    
  
    1. rock 
    2. paper 
    3. scissors
    4. exit
  * The user can input a number to choose rock, paper, or scissors.
  * Enter 4 to exit the game.

The computer randomly selects one of the three options, and the game compares the user's choice with the computer's choice to determine the winner.

## Game Rules:
  1. Rock beats Scissors
  2. Scissors beat Paper
  3. Paper beats Rock
The game will display a graphical representation of your choice and the computer's choice.

## Example Output:
    1. rock 
    2. paper 
    3. scissors
    4. exit
    
    RULES:
    1.rock beats scissors
    2. scissors beats paper
    3. paper beats rock
    
    Enter your choice: 1
    You chose: 
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    
    Computer chose:
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    
    You win!

## How the Game Works
  1. User Input: The player enters a number (1 for rock, 2 for paper, 3 for scissors, or 4 to exit).
  2. Random Computer Choice: The computer randomly selects rock, paper, or scissors.
  3. Comparison and Result:       
      * The user's choice is compared to the computer's.
      * The result is displayed: win, lose, or draw.
  5. Exit Option: The player can enter 4 to exit the game.

## Code Explanation
  * Images: ASCII art images represent the choices for rock, paper, and scissors.
  * Random Choice: The computer's choice is generated using random.randint(1, 3).
  * Game Loop: The game runs in a continuous while loop, and the user can keep playing until they choose to exit.
  
## License
This project is open-source and free to use.
  ```css
  This `README.md` explains the basic usage of the Rock-Paper-Scissors game, how to run it, what the rules are, and how the game mechanics work.
