import unittest
from functions.get_files_info import get_files_info
import os

class TestGetFiles(unittest.TestCase):
    def test_one(self):
        result = get_files_info("calculator", "pkg")
        print(f"result is {result}")
        # self.assertEqual(result, 8)

    def test_list_dir_contents(self):
        result = get_files_info("calculator", "pkg")
        print(f"result is {result}")
        print(f"Contents are - {os.listdir(result)}")

    def test_is_dir(self):
        result = get_files_info("calculator", "pkg")
        is_dir = os.path.isdir(result)
        # print(f"result is {result}")
        print(f"This is a dur {is_dir}")

    def test_if_dir_is_within_working_directory(self):
        err,working_dir,dir = get_files_info("calculator", "/bin")
        correct = f'Error: "{dir}" is not a directory'
        if err == correct:
            print("Correct!")
        else:
            print("Fail")

if __name__ == "__main__":
    unittest.main()