from functions.get_file_content import verify_file_path
import os


def write_file(working_directory, file_path, content):
    pass



def verify_file_path_w(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    # abs_file = os.path.abspath(file_path)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    common_path = [abs_working_dir, abs_file_path]
   
    print(f'Abs file path = {abs_file_path}')
    in_scope = os.path.commonpath(common_path) == abs_working_dir
    print(f"Common Path = {common_path}")
    print(f'In Scope - {in_scope}')
    if not in_scope:
        return (False, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    exists = os.path.exists(abs_file_path)
    print(f'Exists - {exists}')
    if not exists:
        os.makedirs(abs_file_path)

    # if 
    # if base_file_path not in working_dir_contents:
    #     return(False, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory') 
    
    # if not (os.path.exists(os.path.join(working_dir_path, file_path))):
    #     os.makedirs(os.join(working_dir_path, file_path))
    
        
