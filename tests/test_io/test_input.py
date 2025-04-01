import unittest
import os
import shutil
import pandas as pd
from app.io.input import read_file_builtin, read_file_pandas


class TestInputFunctions(unittest.TestCase):

    def setUp(self):
        """Create necessary directories and files for testing."""
        self.data_dir = os.path.join(os.path.dirname(__file__), '../../data')
        os.makedirs(self.data_dir, exist_ok=True)

        self.input_txt = os.path.join(self.data_dir, 'input.txt')
        self.input_csv = os.path.join(self.data_dir, 'input.csv')

        with open(self.input_txt, 'w') as file:
            file.write("Hello, World!")

        data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
        df = pd.DataFrame(data)
        df.to_csv(self.input_csv, index=False)

    def test_read_file_builtin(self):
        """Test that the file is read correctly using built-in functions."""
        result = read_file_builtin(self.input_txt)
        self.assertEqual(result, "Hello, World!")

    def test_read_file_builtin_file_not_found(self):
        """Test the case when the file is not found."""
        os.remove(self.input_txt)
        result = read_file_builtin(self.input_txt)
        self.assertEqual(result, "File not found")

    def test_read_file_pandas(self):
        """Test that the file is read correctly using pandas."""
        expected_output = " Name  Age\nAlice   25\n  Bob   30"
        result = read_file_pandas(self.input_csv)
        self.assertEqual(result.replace("  ", " ").strip(), expected_output.replace("  ", " ").strip())

    def test_read_file_pandas_file_not_found(self):
        """Test the case when the pandas file is not found."""
        os.remove(self.input_csv)
        result = read_file_pandas(self.input_csv)
        self.assertEqual(result, "File not found")

    def tearDown(self):
        """Remove the test files after tests are done."""
        if os.path.exists(self.data_dir):
            shutil.rmtree(self.data_dir)


if __name__ == '__main__':
    unittest.main()