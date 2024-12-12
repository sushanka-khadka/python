# Follower Comparison Game

This is a command-line game where players have to guess which social media account has more followers. The game presents two accounts at a time, and the player tries to select the one with the higher follower count. For every correct guess, the player’s score increases. The game continues until the player makes an incorrect guess.

## Features

- Randomly selects and displays two social media accounts.
- Players choose between two options, guessing which account has more followers.
- Keeps track of the player’s score and displays it after each round.
- Ends the game and displays the final score when the player makes a wrong guess.

## Requirements

Ensure the following dependencies are available in the `game_data` module:

- `accounts`: A dictionary or list of social media accounts.
- `data`: A list of dictionaries, where each dictionary represents an account with fields like `account`, `description`, and `followers`.
- `icon`: A text or ASCII logo to display at the start of each round.

## How to Play

1. Clone or download this repository to your local machine.
2. Make sure you have Python 3.x installed.
3. Run the game with the following command:

   ```bash
   python game.py
4. Follow the on-screen instructions:
    * You’ll see two accounts displayed with a description of each.
    * Type a if you think account A has more followers, or b if you think account B has more followers.
    * If you guess correctly, your score increases, and a new comparison round begins.
    * If you guess incorrectly, the game ends, and your final score is displayed.

## Example Gameplay
    Welcome to the Follower Comparison Game!
    Your current score: 3
    Choice A: Instagram, Social Media Platform
    Choice B: Cristiano Ronaldo, Professional Footballer
    Who has got more followers? Type "a" or "b": b
    You are right!
    Your score: 4
    
    Choice A: Cristiano Ronaldo, Professional Footballer
    Choice B: National Geographic, Media Organization
    Who has got more followers? Type "a" or "b": a
    You are wrong!
    Your final score: 4


## Code Structure
* format_data(account): Formats and returns a string with the account name and description.
* Main game loop:
  - Displays current score and follower comparison options.
  - Takes input from the player and checks if their guess is correct.
  - Updates the score and account options accordingly.
  - Ends the game when the player guesses incorrectly.

 ## License
This project is open-source and available for use, distribution, and modification.


### Explanation

- **Game Description**: Explains the purpose and rules of the game.
- **Dependencies**: Lists the required data structures (`accounts`, `data`, `icon`) that need to be available in the `game_data` module.
- **How to Play**: Provides steps on how to run and play the game.
- **Example Gameplay**: Gives players a sample of what gameplay looks like.
- **Code Structure**: Briefly describes the code structure for clarity.
