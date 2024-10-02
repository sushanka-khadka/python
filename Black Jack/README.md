# Black Jack Game

This is a simple terminal-based implementation of the classic card game **Black Jack**. The objective of the game is to beat the computer by having a hand with a value closer to 21 without exceeding it.

## How to Play

1. You and the computer are each dealt two cards.
2. The value of cards 2-10 is their face value, J/Q/K are worth 10, and Ace is worth 11 unless it causes the score to exceed 21, in which case it's worth 1.
3. You can choose to draw additional cards to improve your score, but if your score exceeds 21, you lose.
4. The computer will draw cards until it has a score of at least 17.

### Game Flow

- Initially, two cards are dealt to both the player and the computer.
- You can see the value of one of the computer's cards.
- You then choose whether to draw more cards or hold.
- The computer will automatically draw cards if its total score is below 17.
- The game ends when either you or the computer have a score of 21 (Black Jack), or someone exceeds 21.

### Win Conditions

- If your score is exactly 21, you win (Black Jack).
- If the computer’s score exceeds 21, you win.
- If your score exceeds 21, you lose.
- The highest score without going over 21 wins the game.

## Example Run
    Your cards: [7, 10], current_score: 17
    Computer first card: 8 
    
    Do you want to draw another card?
    Type "y" or "n"

## Installation
1. Clone this repository or download the script.
2. Ensure you have Python installed on your system.
3. Run the script.
    ```bash
    python black_jack.py

## Dependencies
This project uses the following external Python libraries:
  * os (for clearing the screen)
  * random (for drawing random cards)
Ensure you have these libraries installed. These should be pre-installed in standard Python distributions.

## License
This project is open-source and free to use.
   ```css   
   This `README.md` provides a clear description of how your program works, how to run it, and includes an example.
