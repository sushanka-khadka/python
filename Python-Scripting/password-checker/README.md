# Password Pwned Checker

## Overview
The Password Pwned Checker is a Python program that helps you determine if your password has been exposed in known data breaches. It uses the **Have I Been Pwned API** to check the password's SHA-1 hash against a secure database of compromised passwords. This tool is essential for improving online security and encouraging the use of strong, uncompromised passwords.
- haveibeenpwned API: https://haveibeenpwned.com/API/v3
- API(searching by range) : https://api.pwnedpasswords.com/range/{first 5 hash chars}
---

## Features
- **Secure Password Verification**: Utilizes the k-anonymity model to securely check password hashes without exposing full hashes.
- **Breach Count**: Reports how many times a password has appeared in breached datasets.
- **Simple Interface**: Command-line-based program for quick checks.

---

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `requests` library (install using `pip install requests`)

---

## Usage
1. Clone or download the script to your local machine.
2. Open a terminal in the script's directory.
3. Run the program with the passwords you want to check:

```bash
python password_pwned_checker.py [password1] [password2] ...
```

### Example:
```bash
python3 main.py mypassword123 qwerty clone_it_gItHub
```
**Output:**
```bash
"mypassword123" has been pwned 2315 times. Time to change your password.
"qwerty" has been pwned 10716300 times. Time to change your password.
clone_it_gItHub has not found. Carry on!
done!!!
```
---

## How It Works
1. **Hashing the Password**: The program converts your password into a SHA-1 hash.
2. **K-Anonymity Model**: Sends only the first five characters of the hash to the Have I Been Pwned API.
3. **Checking Breach Count**: Compares the remaining part of the hash against the API's response to determine if the password has been compromised.
4. **Reporting**: Displays the result, including the breach count, if applicable.

---

## Limitations
- Only checks passwords using the Have I Been Pwned database.
- Requires an active internet connection.

---

## Security Note
- The program never sends your full password or complete hash to the API, ensuring your passwords remain secure.

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute the program as needed.

---

## Contributing
If you encounter issues or have suggestions for improvements, please submit a pull request or create an issue in the repository.
