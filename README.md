Password Generator

Users can specify the length of the password, choose character sets (uppercase letters, lowercase letters, digits, special characters, and spaces), and perform actions like generating a new password, copying it to the clipboard, pasting it from the clipboard, or exiting the program.

How to Use:

Password Length:
Enter the minimum and maximum length for the password.
Default values are 8 for the minimum length and 16 for the maximum length.
Positive integer values are expected, and validation ensures correctness.

Character Set Selection:
Users can choose to include or exclude different character sets:
Uppercase letters (default: included)
Lowercase letters (default: included)
Digits (default: included)
Special characters (default: included)
Spaces (default: not included)

Generate Password:
Generates a random password based on the specified length and character sets.

Options Menu:
Users are presented with the following options:
Regenerate Password (1): Generates a new random password.
Copy to Clipboard (2): Copies the generated password to the clipboard.
Paste from Clipboard (3): Pastes the content from the clipboard
Exit (4): Exits the program.

How to Run:
Run the script in a Python environment.
Follow the prompts to customize and manage passwords.
The script uses the pyperclip library for clipboard interaction. Install it using: pip install pyperclip
