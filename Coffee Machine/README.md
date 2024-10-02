# Coffee Machine Program

This is a Python-based coffee machine simulation that allows users to place orders for different coffee drinks, checks if enough resources are available, and handles payments. The program keeps track of the profit earned and displays a report of resources.

## Features
- **Available Drinks**: The coffee machine offers the following drinks:
  - Espresso
  - Americano
  - Latte
  - Cappuccino
- **Resource Management**: The machine checks if enough resources (water, milk, coffee, foam) are available before processing an order.
- **Payment Handling**: Users can pay using quarters, dimes, nickels, and pennies. The machine will calculate the total inserted amount, check if it is sufficient, and refund any excess.
- **Reporting**: A `report` command shows the current status of the machine's resources and the total profit earned.
- **Turn Off the Machine**: The `off` command allows the user to turn off the machine and exit the program.


## How to Run the Program
1. Clone or download this repository.
2. Ensure you have Python installed on your system.
3. Run the program:
    ```bash
    python main.py
4. Follow the prompts to select a drink, enter payment, and view reports.


## Program Flow
1. Startup: The machine will display available products and options (off, report).
2. Order: The user selects a drink or other options.
3. Resource Check: The machine checks if there are enough resources for the selected drink.
4. Payment: The user enters payment in coins (quarters, dimes, nickels, pennies).
5. Completion: If payment is successful, the drink is made, and resources are reduced accordingly.
6. Reporting: Use the report option to view available resources and total profit.

## License
This project is open source, feel free to use.

    You can customize the content according to your project structure and additional features.
