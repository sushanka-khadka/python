# Goal-Based Agent Program

## Overview
This program demonstrates a simple goal-based agent system where an agent tries to achieve a set of predefined goals using available actions. Each goal is described by its description, and each action specifies a task to perform and the goal it helps to achieve.

## Key Components

### 1. **Goal**
Represents a goal the agent aims to achieve.
- **Attributes:**
  - `description`: A string describing the goal.
- **Methods:**
  - `get_description()`: Returns the description of the goal.

### 2. **Action**
Represents an action the agent can perform to achieve a specific goal.
- **Attributes:**
  - `task_perform`: A string describing the task.
  - `goal_description`: A string describing the goal this action supports.
- **Methods:**
  - `get_task_perform()`: Returns the task to be performed.
  - `get_goal_description()`: Returns the goal description this action addresses.
  - `execute_task()`: Executes the task by printing a message to the console.

### 3. **Agent**
Represents the agent that manages goals and actions.
- **Attributes:**
  - `action`: A list of available actions.
  - `goal`: A list of goals to achieve.
- **Methods:**
  - `add_action(action)`: Adds an action to the agent's list of actions.
  - `add_goal(goal)`: Adds a goal to the agent's list of goals.
  - `achieve_goal()`: Attempts to achieve each goal in the list. If a matching action is found, the action is executed. Otherwise, it indicates that the agent does not know what to do.

## Execution Flow
1. **Define Goals:** Create `Goal` objects representing the agent's objectives.
2. **Define Actions:** Create `Action` objects specifying tasks and their corresponding goals.
3. **Add Goals and Actions to Agent:** Use the `add_goal()` and `add_action()` methods to populate the agent's goal and action lists.
4. **Achieve Goals:** Call the `achieve_goal()` method to let the agent attempt to fulfill its goals by matching actions to goals.

## Example Usage
The main function illustrates the usage of the program:
- **Goals:**
  - Score a header
  - Score a banger
  - Win the ball
  - Win a foul
  - Keep possession
  - Win the match

- **Actions:**
  - Dive to win a foul
  - Shoot from outside the box to score a banger
  - Jump to score a header
  - Pass the ball to keep possession
  - Tackle the opponent to win the ball

- The agent attempts to achieve these goals using the defined actions. If no action matches a goal, the agent indicates that it doesn't know what to do.

## Running the Program
To run the program:
1. Save the script to a file, e.g., `goal_based_agent.py`.
2. Execute the script using Python:
   ```
   python goal_based_agent.py
   ```
3. The output will display the agent's attempts to achieve each goal and the corresponding actions performed.

## Sample Output
```
achieving goal: score a header
executing task: jump

achieving goal: score a banger
executing task: shoot from outside the box

achieving goal: win the ball
executing task: tackle the opponent

achieving goal: win a foul
executing task: dive

achieving goal: keep possession
executing task: pass the ball

achieving goal: win the match
	 don't know what to do....
```

## Customization
- **Adding Goals:** Create additional `Goal` objects and add them to the agent using `add_goal()`.
- **Adding Actions:** Create new `Action` objects and add them to the agent using `add_action()`.
- **Modify Behavior:** Extend the `Agent`, `Goal`, or `Action` classes to introduce new features or decision-making capabilities.

## License
This project is open-source and can be freely used and modified.

