import pandas as pd

def input_text():
    """
    Function to input text from the console.
    """
    return input("Enter some text: ")

def read_file_builtin():
    """
    Function to read a file using Python's built-in functions.
    """
    try:
        with open('data/input.txt', 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"

def read_file_pandas():
    """
    Function to read a file using the pandas library.
    """
    try:
        df = pd.read_csv('data/input.csv')
        return df.to_string()
    except FileNotFoundError:
        return "File not found"