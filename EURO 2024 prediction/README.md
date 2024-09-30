# Euro Cup Winner Prediction: Spain vs England

## Introduction

This program simulates and predicts the winner of a Euro Cup match between Spain and England, including possible extra time and penalty shootouts. It also selects a random player as the "Man of the Match."

## How It Works

1. **Random Score Generation**: 
   - The program generates random scores for England and Spain within regular time using the `random.randint()` function.
   - If scores are tied after regular time, extra time is simulated with additional random score generation.
   - If scores are still tied after extra time, the game proceeds to a penalty shootout, with random penalties generated.

2. **Man of the Match**:
   - A player is randomly selected from the combined list of players from both teams as the "Man of the Match."

## Features

- Predicts the winner based on random scores.
- Simulates extra time and penalty shootouts if needed.
- Randomly selects a "Man of the Match" from both teams.

## Program Flow

1. **Regular Time**: 
   - Random scores are assigned to both teams.
   - If one team has a higher score, they are declared the winner.

2. **Extra Time**: 
   - If the scores are tied in regular time, extra time is simulated, and more scores are generated.
   - If one team scores higher during extra time, they win.

3. **Penalty Shootout**: 
   - If scores are still tied after extra time, a penalty shootout occurs.
   - Random penalties are generated, and the team with the higher penalty score wins.

4. **Man of the Match**:
   - A random player from either team is declared the "Man of the Match."

## Example Output
     Spains Wins with score 1-0
     Man of the Match: Yamal

## How to Run

1. Clone or download the program file.
2. Run the script in Python:
   ```bash
   python euro_final2024.py
   
 ## License
This project is open-source and can be modified or distributed freely.
```bash	
This README provides an overview of how the program works, the features, and the example usage.

