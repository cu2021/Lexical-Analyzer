# Lexical Analyzer
**Date:** December 6th, 2023
## Description
This Python script serves as a lexical analyzer for source code, designed to read and process a given source code file while identifying and categorizing various elements within the code, such as keywords, operators, constants, identifiers, and special characters. The script uses regular expressions and a predefined set of rules to tokenize the code and provide extended tokens with additional information about each matched element.

## Prerequisites
Before using this script, make sure you have Python installed on your system.

## How to Use

1. Clone or download this repository to your local machine.

2. Place your source code in a file (e.g., `sourceCode.txt`) within the same directory as this script.

3. Open a terminal or command prompt and navigate to the directory containing the script.

4. Run the script using the following command:
	```
	python main.py
	```
5. The script will process the source code and display the resulting tokens in the console.

## Code Explanation

The script performs the following tasks:

* Reads the source code from the specified file and removes comments.
* Defines regular expressions to identify keywords, operators, constants, identifiers, and special characters within the code.
* Replaces matched elements with extended tokens containing additional information about each element.
* Displays the extended tokens in the console.

## Example
Here are some example tokens that the script may generate:

* `<IF>`: Keyword "if" identified.
* `<mop, 'ADD'>`: Mathematical operator "+" identified as addition.
* `<const, 123.45>`: Constant value "123.45" identified.
* `<id, variable_name>`: Identifier "variable_name" identified.
* `<(>`: Special character "(" identified.
* `<lop, 'GE'>`: Greater than or equal `>=` identified.

## Sample Usage
```
# Specify the input file path
input_file_path = 'sourceCode.txt'

# Read and process the code
code_text = read_code(input_file_path)
modified_code = process_code(code_text)

# Printing the streams of lexemes
for token in tokens:
    if token == " <spch, '}'> " or token == " <spch, '{'> " or token == " <spch, ';'> ":
        print(token)
    else:
        print(token, end='')
```
Please ensure that you have the sourceCode.txt file containing your source code in the same directory as the script.
