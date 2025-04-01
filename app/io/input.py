import pandas as pd
import os

def input_text():
    """
    Function to input text from the console.
    """
    return input("Enter some text: ")

def read_file_builtin(file_path):
    """
    Function to read a file using Python's built-in functions.
    """
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return file.read()
    return "File not found"


def read_file_pandas(file_path):
    """
    Function to read a file using the pandas library.
    """
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df.to_string(index=False).strip()
    return "File not found"