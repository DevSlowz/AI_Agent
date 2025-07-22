from functions.get_file_content import verify_file_path
import os


def write_file(working_directory, file_path, content):
    pass



def verify_file_path_w(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    # abs_file_path = os.path.abspath(file_path)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    paths = [abs_working_dir, abs_file_path]
    result = os.path.commonpath(paths) 
    print(result)
    print(f'abs working dir - {abs_working_dir}')
    thing = abs_file_path.startswith(result)
    print(f'Thing is - {thing}')
    # working_dir_contents = os.listdir(working_dir_path)
    # print(result)    
    # print(abs_working_dir)
    # print(abs_file_path)
    print(f"Current working directory: {os.getcwd()}")
    print(f"Working directory parameter: {working_directory}")
    print(f"Joining the abs path: {abs_file_path}")
    print(f"File path parameter: {os.path.abspath(file_path)}")
    print(f"Does the file actually exist at the resolved path? {os.path.exists(abs_file_path)}")

    # if 
    # if base_file_path not in working_dir_contents:
    #     return(False, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory') 
    
    # if not (os.path.exists(os.path.join(working_dir_path, file_path))):
    #     os.makedirs(os.join(working_dir_path, file_path))
    
        
