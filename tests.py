import unittest
from functions.get_files_info import get_files_info, verify_directory_path, restrict_to_working_directory, valid_directory
from functions.get_file_content import get_file_content, verify_file_path
from functions.write_file import write_file
from functions.run_python import run_python_file
import os
# from dotenv import load_dotenv

class TestGetFiles(unittest.TestCase):
    # Load abs path from env to project abs path details   
    # load_dotenv()

    # working_dir = os.path.abspath("calculator")

    # def test_valid_verify_directory_path(self):
    #     path = os.path.join('calculator', "pkg")
    #     abs_path = os.path.abspath(path)
    #     result = verify_directory_path(abs_path)

    #     self.assertEqual((True, ''), result)

    # def test_invalid_verify_directory_path(self):
    #     path = os.path.join('calculator', 'pkg')
    #     abs_path = os.path.abspath(path) + "F"
    #     result = verify_directory_path(abs_path)
    #     self.assertEqual((False, f"Path does not exist: '{abs_path}'."), result)

    #     # TODO need to add test case for invalid directory ^ 

    # def test_restrict_to_working_directory(self):
    #     path = os.path.join('calculator', 'pkg')
    #     abs_path = os.path.abspath('calculator')
    #     result = restrict_to_working_directory(abs_path, 'pkg')
    #     self.assertEqual((True, ""), result)

    # def test_invalid_restrict_to_working_directory(self):
    #     path = os.path.join('calculator', 'pkg')
    #     abs_path = os.path.abspath(path)
    #     result = restrict_to_working_directory(abs_path, 'pkg')
    #     self.assertEqual(False, result[0])

    # def test_valid_directoryy(self):
    #     result = valid_directory('calculator', 'pkg')
    #     self.assertEqual((True, ""), (result[0], result[1]))
 
    # def test_invalid_valid_directoryy(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = valid_directory('calculator', 'pkgg')
    #     # print(result)
    #     expected = (False, f"Path does not exist: '{abs_path}'.")
    #     self.assertEqual(result[:2], expected, f"Expected {expected}, but got {result}")

    # def test__valid_directoryy(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = verify_file_path("calculator", "main.py")
    #     print(result)

    # def test__valid_txt_file(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = get_file_content("calculator", "lorem.txt")
    #     # print(result)

    # def test__valid_file(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = get_file_content("calculator", "main.py")
    #     print(result)


    # def test__valid_path_to_file(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = get_file_content("calculator", "pkg/calculator.py")
    #     print(result)

    # def test__invalid_path_to_file(self):
    #     working_dir = os.path.abspath('calculator')
    #     path = os.path.join(working_dir, 'pkgg')
    #     abs_path = os.path.abspath(path)

    #     result = get_file_content("calculator", "pkg/does_not_exist.py")
    #     # print(result)
    

    # def test_write_file_file_exist(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    #     print(result) 
   
    # def test_write_file_file_not_exist(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    #     print(result) 
    # def test_write_file_file_not_allowed(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    #     print(result)
    # 
    #  


    # def test_write_file_file_exist(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = run_python_file("calculator", "main.py") 
    #     print(result) 
   
    # def test_write_file_file_not_exist(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = run_python_file("calculator", "main.py", ["3 + 5"])
    #     print(result) 
    # def test_write_file_file_not_allowed(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = run_python_file("calculator", "tests.py")
    #     print(result)
        
    # def test_write_file_file_not_allowed2(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = get_files_info({'directory': '.'})
    #     print(result) 

    # def test_write_file_file_not_allowed3(self):
    #     abs_file_path = os.path.abspath(os.path.join("calculator", "lorem.txt"))
    #     result = get_files_info({'directory': 'pkg'})
    #     print(result)  
    # def test_get_files_info_calculator(self):
    #     get_files_info("calculator", ".")

    # def test_get_files_info_calculator_pkg(self):
    #     get_files_info("calculator", "pkg")
        
    # def test_get_files_info_calculator_bin(self):
    #     get_files_info("calculator", "/bin")

    # def test_get_files_info_calculator_outside_directroy(self):
    #     get_files_info("calculator", "../")

    # def test_get_file_content(self):
    #     get_file_content("calculator", "pkg/calculator.py")
    #     result = verify_file_path("calculator", "pkfg/calculator.py")
    #     print(result)
     

if __name__ == "__main__":
    unittest.main(verbosity=0)