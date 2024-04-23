# **GenShell_Backend**

GenShell is a Python project that utilizes generative AI to generate OS commands and database queries based on the input provided. It generates as well as runs the commands to show the desired output.

## Overview

This project aims to assist users in generating OS commands and database queries for various purposes. It utilizes Gemini API and our algorithm uses its result to generate coherent and relevant commands as well as queries based on the provided input.

## Features

- Input-driven Command and Query Generation: Users can input a prompt or context, and the AI generates an OS command or database query relevant to that input.
- Customization: Users can adjust the parameters of the AI model to fine-tune the generated commands and queries.
- Multiple Applications: The generated commands and queries can be used for scripting, database management, system administration, and more.
- Easy-to-Use Interface: Simple command-line interface for generating commands and queries quickly.

## Installation

1. Clone this repository:

    ```
    git clone https://github.com/VarunProhit/genShell_Application.git
    ```

2. Install the required dependencies:

    ```
    pip install -r requirements.txt
    ```

## Usage

1. Run the command generator script:

    ```
    uvicorn server:app
    ```

2. Follow the prompts to input your context or prompt.

3. The AI will generate a Linux command or database queries based on your input.

## Examples

- Linux Command:
  
  ```
  Input: "List all files in the current directory"
  Output: "ls -l"
  ```

- Database Query:

  ```
  Input: "Retrieve all employees from the 'HR' department in MySQL" 
  Output: "SELECT * FROM employees WHERE department = 'HR';"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

