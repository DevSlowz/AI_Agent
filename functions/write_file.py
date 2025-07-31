from functions.get_file_content import verify_file_path
import os
from google.genai import types


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    parent_dir = os.path.dirname(abs_file_path)
    common_path = [abs_working_dir, abs_file_path]
   
    in_scope = os.path.commonpath(common_path) == abs_working_dir

    if not in_scope:
        return(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')

    exists = os.path.exists(abs_file_path)
    
    if not exists:
        os.makedirs(parent_dir, exist_ok=True)
        with open(abs_file_path, 'w') as f:
            f.write(content)
        return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    
    with open(abs_file_path, 'w') as f:
        f.write(content)
    return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')    

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to the file specified by file path provided and constrained within the working directory. Use the content to write to the file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="This is the content that will be written to the python file provided"
            ),
        },
    ),
)

    


 
    

    
        
