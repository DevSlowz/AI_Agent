import os 
import subprocess
def run_python_file(working_directory, file_path, args=[]):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    parent_dir = os.path.dirname(abs_file_path)
    common_path = [abs_working_dir, abs_file_path]
   
    in_scope = os.path.commonpath(common_path) == abs_working_dir

    if not in_scope:
        return(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    

    exists = os.path.exists(abs_file_path)
    
    if not exists:
        return(f'Error: File "{file_path}" not found.')
    
    if not abs_file_path.endswith('.py'):
        return(f'Error: "{file_path}" is not a Python file.')
    
    try:  
        msg_output = ""
        result = subprocess.run(args=['python3', abs_file_path] + args, timeout=30, capture_output=True, cwd = working_directory)
        msg_output += (f'STDOUT: {result.stdout.decode()}') + '\n'
        msg_output += (f'STDERR: {result.stderr.decode()}') + '\n'

        if result.returncode != 0:
            msg_output += (f'Process exited with code {result.returncode}') + '\n'
        if not result.stdout and not result.stderr:
            msg_output += ('No output produced') + '\n'
    except Exception as e:
        msg_output += (f"Error: executing Python file: {e}") + '\n'

    return msg_output