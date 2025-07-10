import unittest
from functions.get_files_info import get_files_info
import os
from dotenv import load_dotenv

class TestGetFiles(unittest.TestCase):
    # Load abs path from env to project abs path details   
    load_dotenv()
    def test_valid_case_print_content(self):
        path = get_files_info("calculator", "pkg")
        # correct = os.environ.get("TEST_PATH")
        # print(f"result is {path}")
        # self.assertEqual(path, correct)


    def test_path_creation(self):
        path = get_files_info("calculator", "pkg")
        correct = os.environ.get("TEST_PATH")
        # print(f"result is {path}")
        self.assertEqual(path, correct)

    def test_list_dir_contents(self):
        path = get_files_info("calculator", "pkg")
        contain_contents = len(os.listdir(path)) > 0
        # print(f"result is {result}")
        # print(f"Contents are - {os.listdir(result)}")
        self.assertEqual(contain_contents, True)

    def test_is_dir(self):
        result = get_files_info("calculator", "pkg")
        is_dir = os.path.isdir(result)
        # print(f"result is {result}")
        # print(f"This is a dur {is_dir}")
        self.assertEqual(is_dir, True)

    def test_is_not_dir(self):
        result, dir = get_files_info("calculator", "pkgf")
        correct = f'Error: "{dir}" is not a directory'
        # print(f"result is {result}")
        # print(f"This is a dur {is_dir}")
        self.assertEqual(result, correct)

    def test_if_dir_is_within_working_directory(self):
        err,working_dir,dir = get_files_info("calculator", "/bin")
        correct = f'Error: "{dir}" is not a directory'
        # if err == correct:
        #     print("Correct!")
        # else:
        #     print("Fail")
        self.assertEqual(err, correct)

if __name__ == "__main__":
    unittest.main()