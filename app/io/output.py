
def output_text(text):
    """
    Function to output text to the console.
    """
    print(text)

def write_file_builtin(text):
    """
    Function to write text to a file using Python's built-in functions.
    """
    try:
        with open('data/output.txt', 'w') as file:
            file.write(text)
    except Exception as e:
        print(f"An error occurred: {e}")