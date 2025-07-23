from functions.get_file_content import verify_file_path
import os


def write_file(working_directory, file_path, content):
    pass



def verify_file_path_w(working_directory, file_path, content):
    

    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    parent_dir = os.path.dirname(abs_file_path)
    common_path = [abs_working_dir, abs_file_path]
   
    in_scope = os.path.commonpath(common_path) == abs_working_dir

    if not in_scope:
        return (False, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    exists = os.path.exists(abs_file_path)
    
    if not exists:
        os.makedirs(parent_dir, exist_ok=True)
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return(True, f"Directory path created and Content has been written to {abs_file_path}")
    
    
    with open(abs_file_path, 'w') as f:
        f.write(content)
    return(True, f"Directory path and file exist content has been overwritten at  {abs_file_path}")    
 
    

    
        
