# Email Slicer
welcome to email - slicer...

## Description
This is a simple yet robust Python script that takes an email address as input and splits it into its two core components: the username and the domain. It includes validation to ensure the input follows standard email formatting rules, making it a great beginner project for practicing string manipulation and conditional logic in Python.

## Features
- **User-Friendly Input**: Prompts the user to enter an email address.
- **Core Slicing Logic**: Separates the username and the domain based on the `@` symbol.
- **Robust Validation**:
  - Checks that exactly one `@` symbol is present.
  - Ensures the `@` symbol is not at the very beginning or end of the address.
  - Verifies that the domain contains a `.` and is not at the beginning or end of the domain part.
- **Clear Output**: Displays the extracted username and domain, or provides a specific error message if the format is invalid.

## How to Use
1.  Make sure you have Python 3 installed on your system.
2.  Save the code as a Python file (e.g., `email_slicer.py`).
3.  Run the script from your terminal:
    ```
    python email_slicer.py
    ```
4.  When prompted, enter an email address and press Enter.

## Author 
[ Abhishek Jha 🧑‍💻 ]
