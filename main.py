
from app.io.input import input_text, read_file_builtin, read_file_pandas
from app.io.output import output_text, write_file_builtin

def main():
    console_input = input_text()
    file_input_builtin = read_file_builtin()
    file_input_pandas = read_file_pandas()

    output_text(console_input)
    output_text(file_input_builtin)
    output_text(file_input_pandas)

    write_file_builtin(console_input)
    write_file_builtin(file_input_builtin)
    write_file_builtin(file_input_pandas)

if __name__ == '__main__':
    main()