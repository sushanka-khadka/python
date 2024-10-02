# Python Calculator Project
This project is a simple calculator program implemented in Python. It allows users to perform continuous calculations with various mathematical operations until they choose to stop or start a new calculation.

## Table of Contents
* [Description](#description)
* [How to Use](#how-to-use)
* [Features](#features)
* [Example](#example)
* [License](#license)

## Description
This Python calculator project offers basic arithmetic operations such as addition, subtraction, multiplication, and division. Users can:
  * Input two numbers.
  * Choose an operation to perform.
  * Continue calculating using the result from the last calculation, start a new calculation, or exit.
The project is built using a custom library (calculator_lib) that contains the functions and operations for the calculator.

## How to Use
1. Clone or download the project to your local machine.
2. Make sure the calculator_lib is correctly imported or present in the working directory.
3. Run the program by executing the script.
    ```bash
    python calculator.py  
4. Enter the first number and then continuously enter the next number for calculations.
5. Choose an operation (+, -, *, /) when prompted.
7. After each calculation, you can:
    * Press y to continue using the result in further operations.
    * Press n to start a new calculation.
    * Press e to exit the program.

## Features
* Basic arithmetic operations (addition, subtraction, multiplication, division).
* Ability to continue calculations using the result of the previous calculation.
* Option to start a new calculation or exit the program.
* Clear screen functionality for starting new calculations.

## Example
    enter first number: 10
    enter next number: 5
    +   -   *   /
    enter operation: +
    10 + 5 = 15
    
    press "y" to continue, "n" to start new calculation or "e" to exit: y
    enter next number: 2
    +   -   *   /
    enter operation: *
    15 * 2 = 30
    
    press "y" to continue, "n" to start new calculation or "e" to exit: n

## License
This project is open-source and free to use.
