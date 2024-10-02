# Caesar Cipher Project
This is a simple Python project that demonstrates the Caesar Cipher encryption and decryption technique. The program allows users to enter any text and either encrypt or decrypt it based on a shift value.

## Table of Contents
* [Description](#description)
* [How to Use](#how-to-use)
* [Example](#example)
* [License](#license)

## Description
The Caesar Cipher is one of the oldest known encryption techniques, where each letter in the plaintext is replaced by a letter found by moving a certain number of places down or up the alphabet. This project implements the cipher in Python with the following features:

- Encrypts text with a positive shift value.
- Decrypts text with a negative shift value.
- Supports both uppercase and lowercase letters.
- Retains non-alphabet characters unchanged (e.g., spaces, punctuation).

## How to Use
1. Clone the repository or download the Python script.
2. Run the program by executing the script.
   ```bash
     python caesar_cipher.py
4. Enter the text you want to encode or decode.
5. Provide the shift position:
    - A positive number will encrypt the text.
    - A negative number will decrypt the text.
6. The program will output the result and ask if you'd like to continue.

## Example
    Enter any text to encode or decode: Hello, World!
    Enter the shift position
        +ve for encryption
        -ve for decryption: 3
    
    Encrypted text: Khoor, Zruog!
    
    type "yes" to continue: yes
    
    Enter any text to encode or decode: Khoor, Zruog!
    Enter the shift position
        +ve for encryption
        -ve for decryption: -3
    
    Decrypted text: Hello, World!
    
    type "yes" to continue: no

## License
This project is open-source and free to use.
      
    This `README.md` provides a clear description of how your program works, how to run it, and includes an example.



