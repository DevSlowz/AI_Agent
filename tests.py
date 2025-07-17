import unittest
from functions.get_files_info import get_files_info, verify_directory_path, restrict_to_working_directory, valid_directory
import os
# from dotenv import load_dotenv

class TestGetFiles(unittest.TestCase):
    # Load abs path from env to project abs path details   
    # load_dotenv()

    # working_dir = os.path.abspath("calculator")

    def test_valid_verify_directory_path(self):
        path = os.path.join('calculator', "pkg")
        abs_path = os.path.abspath(path)
        result = verify_directory_path(abs_path)

        self.assertEqual((True, ''), result)

    def test_invalid_verify_directory_path(self):
        path = os.path.join('calculator', 'pkg')
        abs_path = os.path.abspath(path) + "F"
        result = verify_directory_path(abs_path)
        self.assertEqual((False, f"Path does not exist: '{abs_path}'."), result)

        # TODO need to add test case for invalid directory ^ 

    def test_restrict_to_working_directory(self):
        path = os.path.join('calculator', 'pkg')
        abs_path = os.path.abspath('calculator')
        result = restrict_to_working_directory(abs_path, 'pkg')
        self.assertEqual((True, ""), result)

    def test_invalid_restrict_to_working_directory(self):
        path = os.path.join('calculator', 'pkg')
        abs_path = os.path.abspath(path)
        result = restrict_to_working_directory(abs_path, 'pkg')
        self.assertEqual(False, result[0])

    def test_valid_directoryy(self):
        result = valid_directory('calculator', 'pkg')
        self.assertEqual((True, ""), (result[0], result[1]))
 
    def test_invalid_valid_directoryy(self):
        working_dir = os.path.abspath('calculator')
        path = os.path.join(working_dir, 'pkgg')
        abs_path = os.path.abspath(path)

        result = valid_directory('calculator', 'pkgg')
        # print(result)
        expected = (False, f"Path does not exist: '{abs_path}'.")
        self.assertEqual(result[:2], expected, f"Expected {expected}, but got {result}")

    def test_thing(self):
        get_files_info("calculator", "pkg")
        

    # TODO : Need to modify get_files_info to handle this case
    # def test_directory_is_current_directory(self):
    #     path = get_files_info("calculator", ".")
        # correct = os.environ.get("TEST_PATH")
        # print(f"result is {path}")
        # self.assertEqual(path, correct)

    # def test_path_creation(self):
    #     path = get_files_info("calculator", "pkg")
    #     correct = os.environ.get("TEST_PATH")
    #     # print(f"result is {path}")
    #     self.assertEqual(path, correct)


    # def test_list_dir_contents(self):
    #     path = get_files_info("calculator", "pkg")
    #     contain_contents = len(os.listdir(path)) > 0
    #     # print(f"result is {result}")
    #     # print(f"Contents are - {os.listdir(result)}")
    #     self.assertEqual(contain_contents, True)


    # def test_is_dir(self):
    #     result = get_files_info("calculator", "pkg")
    #     is_dir = os.path.isdir(result)
    #     # print(f"result is {result}")
    #     # print(f"This is a dur {is_dir}")
    #     self.assertEqual(is_dir, True)


    # def test_is_not_dir(self):
    #     result, dir = get_files_info("calculator", "pkgf")
    #     correct = f'Error: "{dir}" is not a directory'
    #     # print(f"result is {result}")
    #     # print(f"This is a dur {is_dir}")
    #     self.assertEqual(result, correct)
   

    # def test_if_dir_is_within_working_directory(self):
    #     err,working_dir,dir = get_files_info("calculator", "/bin")
    #     correct = f'Error: "{dir}" is not a directory'
    #     # if err == correct:
    #     #     print("Correct!")
    #     # else:
    #     #     print("Fail")
    #     self.assertEqual(err, correct)
     

if __name__ == "__main__":
    unittest.main(verbosity=0)