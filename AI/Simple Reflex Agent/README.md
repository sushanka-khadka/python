# Vacuum Cleaner Simulation

This Python program simulates a simple vacuum cleaner agent moving in a 1D environment (a linear row of rooms).

## **Key Features:**

* **Environment:**
    * Represented as a list, where each element indicates the room's state ("dirty" or "clean").
* **Vacuum Cleaner Agent:**
    * **Initialization:** 
        * Creates a room of specified size with all rooms initially dirty.
        * Starts at the rightmost position of the room.
    * **Actions:**
        * `move(direction)`: Moves the vacuum cleaner left (-1) or right (1).
        * `update_room()`: Cleans the current room if it's dirty.
    * **Sensors:**
        * `get_position()`: Returns the current position of the vacuum cleaner.
        * `get_state(i)`: Returns the state ("dirty" or "clean") of the room at position `i`.

## **Simulation Logic:**

1. **Initialization:** Create a vacuum cleaner for a room of a given size.
2. **Movement and Cleaning:**
    * The vacuum cleaner moves in a back-and-forth motion.
    * At each position, it checks the room's state.
    * If the room is dirty, it cleans it.
3. **Termination:** The simulation ends when all rooms in the environment are clean.

**To Run:**

1. Save the code as `vacuum_cleaner.py`.
2. Execute the script from your terminal: `python vacuum_cleaner.py`

**Note:**

* This is a simplified model. Real-world vacuum cleaner agents would incorporate more complex behaviors, such as:
    * Random movement patterns
    * Memory of previously cleaned locations
    * Obstacle avoidance
    * More sophisticated cleaning algorithms

This README provides a basic overview of the vacuum cleaner simulation. For a deeper understanding, refer to the code itself.

## License
This project is open-source and free to use.

    This `README.md` provides a clear description of how your program works, how to run it, and includes an example.
