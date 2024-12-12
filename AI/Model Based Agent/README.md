# Grid Pathfinding Simulation

This project simulates a grid-based environment where an agent moves towards a goal position using the shortest possible path. The program is implemented in Python and demonstrates the use of classes, grid-based navigation, and heuristic decision-making.

## Features

- **Grid Representation**: A grid of customizable size (`row` x `col`) is created, with specific start and goal positions.
- **Pathfinding**: The agent calculates the shortest path to the goal using Manhattan distance heuristics.
- **Visualization**: The program prints each step taken by the agent towards the goal.

## Code Structure

### 1. **Class: `Grid`**
The `Grid` class represents the grid environment and encapsulates the pathfinding logic.

#### Attributes:
- `row`, `col`: Dimensions of the grid.
- `goal_row`, `goal_col`: Target coordinates.
- `row_no`, `col_no`: Current position of the agent.
- `grid`: 2D list representing the grid and visited cells.

#### Methods:
- `__init__(self, row, col, start_row, start_col, goal_row, goal_col)`: Initializes the grid and agent's start and goal positions.
- `up()`, `down()`, `right()`, `left()`: Returns directional movements.
- `update_model()`: Marks the current cell as visited.
- `make_goal()`: Determines the next optimal move based on Manhattan distance.
- `way_to_goal()`: Executes the pathfinding process, printing each step.

### 2. **Function: `main()`**
The `main` function initializes the grid with random start and goal positions and starts the pathfinding process.

#### Workflow:
1. Define the grid size.
2. Randomly select start and goal positions.
3. Initialize the `Grid` object.
4. Print the start and goal positions.
5. Call the `way_to_goal()` method to find the path.

## Usage

1. Ensure Python is installed on your system.
2. Copy the code into a `.py` file, e.g., `grid_pathfinding.py`.
3. Run the script:

```bash
python grid_pathfinding.py
```

4. The program will output the agent's movement and confirm when the goal is reached.

### Example Output:

```
start row:2 start col:3
goal row:4 goal col:1

move to position (3,3)
move to position (4,2)
move to position (4,1)

Reached the goal position!
```

## Customization

- **Grid Size**: Change the `grid_size` variable in the `main()` function to modify the grid dimensions.
- **Start and Goal Positions**: Replace the random positions with specific values if desired.


## Author
This project was developed as a basic simulation of grid-based pathfinding logic.

