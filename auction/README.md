# Messi's Jersey Auction Program

## Introduction

This program allows users to bid for Messi's jersey in an auction. Users can input their name and the bid amount in thousands (k). The program keeps track of the highest bid, and once bidding is over, it announces the winner with the highest bid. The auction starts with a minimum price of 150k.

## How It Works

- The auction starts with a minimum bid of 150k.
- Users can place a bid by entering their name and bid amount.
- If the bid is higher than the current highest bid, it is accepted and stored.
- If the bid is lower than or equal to the highest bid, the user is informed, and the bid is rejected.
- The program keeps asking for new bids until the user decides to stop.
- Once the bidding is complete, the highest bidder is announced as the winner.

## Program Flow

1. The auction dictionary is initialized with a minimum bid of 150k.
2. The program enters a loop, asking users if they want to place a bid.
3. Users provide their name and bid.
4. If the bid is higher than the current highest bid, it is accepted.
5. The program continues asking for more bids until the user types `no`.
6. The program then announces the winner and their bid amount.

## Example Run  
    what is your name: John
    what is your bid (in k)? रु200
    do you want to bid again? yes or no: yes
    what is your name: Alice
    what is your bid (in k)? रु250
    do you want to bid again? yes or no: no   
    Jersey sold to Alice for 250k   
    {'lowest': 150, 'John': 200, 'Alice': 250}

## How to Run

1. Clone the repository or download the Python script.
2. Run the script in your terminal or Python IDE.
3. Follow the prompts to enter your name and bid.
4. Once all bids are entered, the program will announce the winner.

## Code Explanation

- The `auction` dictionary stores the names and bid amounts.
- The `while` loop keeps running until the user inputs 'no' when asked if they want to bid again.
- The program checks if the current bid is higher than the highest bid so far using `max()`.
- The winner is determined based on the highest bid in the dictionary.

## License

This project is open-source and available for use, distribution, and modification.
