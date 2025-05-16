# required import `re` library stands for Regular Expression,
# you can find its documentation here: https://docs.python.org/3/library/re.html
import re

# Define the list of keywords, logical operators, and mathematical operators
KEYWORDS = ["if", "else", "int", "real", "begin", "end", "float", "return"]
LOP = {'<=': 'LE', '>=': 'GE', '>': 'GT', '<': 'LT', '==': 'EQ', '<>': 'NE'}
MOP = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV', '%': 'MOD', '**': 'POW', '=': 'ASSIGN'}
spch = ['(', ')', '$', '?', '::', ',', ';', '{', '}']

# Define a regular expression pattern that combines all the elements to match
combined_pattern = r'("(?:\\"|[^"])*"|\b(?:' + '|'.join(map(re.escape, KEYWORDS)) + r')\b|[()\$?\?\,;\{\}]|\:\:|' \
                                                                                    r'(<=|>=|<>|<|>|==)|[0-9\^\\]+[a-zA-Z][a-zA-z0-9]*|[|\.@`~\'><&\\:]+|' \
                                                                                    r'((?<![0-9]|\w)[-]?\d+(\.\d+)?(?:[eE][-+]?\d+)?)|(\+|-|\*\*|\*|/|%|=)|\b[a-zA-Z_][a-zA-Z0-9_]*\b)'

tokens = []

# Define a function to read and remove comments from the input source code
def read_code(file_path):
    """
    Reads and removes comments from a given source code file and returns the code without comments.

    Args:
        file_path (str): The path to the source code file containing comments.

    Returns:
        str: The source code without comments.

    Raises:
        FileNotFoundError: If the specified file does not exist.

    Example:
        input_file_path = 'sourceCode.txt'
        code_without_comments = read_code(input_file_path)
        print(code_without_comments)
    """

    # Specify the regular expression pattern for single-line and multi-line comments
    comment_pattern = r'(\/\/[^\n]*|/\*.*?\*/|#[^\n]*)'

    try:
        # Read code from the specified file
        with open(file_path, 'r') as file:
            code_text = file.read()

        # Remove all comments from the code
        code_without_comments = re.sub(comment_pattern, '', code_text, flags=re.DOTALL)

        return code_without_comments

    except FileNotFoundError:
        raise FileNotFoundError(f"The specified file '{file_path}' does not exist.")




# Define a function to add extra information to a matched element
def replace_with_extra_info(match):
    """
    Replace a matched element with an extended token containing additional information.

    This function is used in a regex substitution operation to replace matched elements
    with extended tokens that provide extra information about the matched element.

    Args:
        match (re.Match): A regex match object representing the matched element.

    Returns:
        str: An extended token with additional information based on the type of the matched element.

    Examples:
        When used in a regex substitution operation, this function can replace various types of elements
        (e.g., keywords, operators, constants, identifiers, special characters) with tokens containing
        additional information.

    Note:
        The function relies on external data structures like `KEYWORDS`, `LOP`, `MOP`, `spch`, and `tokens`
        for determining the type and additional information of the matched element.

    See Also:
        This function is typically used in the context of lexical analysis or tokenization of source code.
    """
    element = match.group()
    if element in KEYWORDS:
        token = f"<{element.upper()}>"
        tokens.append(token)
        return token
    elif element in LOP:
        token = f" <lop, '{LOP[element]}'> "
        tokens.append(token)
        return token
    elif element in MOP:
        token = f" <mop, '{MOP[element]}'> "
        tokens.append(token)
        return token
    elif re.match(r'^"[^"]*"$', element):
        token = f" <const, {element}> "
        tokens.append(token)
        return token
    elif re.match(r'^(-|\+)?\d+(\.\d+)?(?:[eE][-+]?\d+)?$', element):
        token = f" <const, {element}> "
        tokens.append(token)
        return token
    elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', element):
        token = f" <id, {element}> "
        tokens.append(token)
        return token
    elif element in spch:
        token = f" <{element}> "
        tokens.append(token)
        return token
    else:
        token = f" <unknown, '{element}'> "  # Unrecognized element, return as is
        tokens.append(token)
        return token


# Process the code and add extra information to elements
def process_code(code):
    """
    Process source code by replacing matched elements with extended tokens.

    This function takes a source code string and processes it by replacing matched elements
    with extended tokens that contain additional information. It uses the `re.sub` function
    with a specified `combined_pattern` and the `replace_with_extra_info` function for the replacement.

    Args:
        code (str): The source code to be processed.

    Returns:
        str: The processed source code with matched elements replaced by extended tokens.

    Examples:
        This function is typically used in the context of lexical analysis or tokenization of source code.
        It replaces elements like keywords, operators, constants, identifiers, and special characters with tokens
        containing additional information based on their type.

    See Also:
        - `combined_pattern`: The regular expression pattern used for identifying elements to replace.
        - `replace_with_extra_info`: The function responsible for generating extended tokens.
    """
    return re.sub(combined_pattern, replace_with_extra_info, code)


if __name__ == '__main__':
    # Specify the input file path
    input_file_path = 'sourceCode.txt'

    # Read and process the code
    code_text = read_code(input_file_path)
    modified_code = process_code(code_text)

    # Printing the streams of lexemes
    for token in tokens:
        if token == " <}> " or token == " <{> " or token == " <;> ":
            print(token)
        else:
            print(token, end='')
