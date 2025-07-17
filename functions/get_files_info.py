import os


def get_files_info(working_directory, directory=None):
    # working_directory is the directory we wannt to search in
    # directory is the content we want to display within the working_directory
    # Example get_files_info(calculator, ".") = Working inside the scope of the calculator directory 
    # List the contents 
    # path = f'{working_directory}/{directory}'

    # NOTE: Return statements will need to be print statements that way the agent can try to determine the error
    # NOTE: Might want to consider not storing err messages multiple times to avoid rewrite the variable
    # working_dir = os.path.abspath(working_directory)
    # path = os.path.join(working_directory, directory)
    # abs_path = os.path.abspath(path)

    
    results  = valid_directory(working_directory, directory)
    # print(results)
    if results[0] and len(results[1]) == 0:
        print_directory_content(results[2])
    else:
        print(results[1])



def print_directory_content(path):
    try:
        directory_contents = os.listdir(path)
    except Exception as e:
       print(f"Error accessing directory '{path}': {str(e)}")
    print("Result for current directory:")
    for item in directory_contents:
        file_path = os.path.join(path, item)
        item = item.strip('.')
        # Refactor repetitive directory path checks into a dedicated function to minimize code duplication 
        # and align with the "Write Once, Run Anywhere" principle.
        # TODO - Write a modular function for checking if somethig is a dirß
        print(f"- {item}: {os.path.getsize(os.path.abspath(file_path))} bytes, is_dir={os.path.isdir(file_path)}")

    
# Check if a valid dirtory is given
def verify_directory_path(path):
    if not isinstance(path, str):
        return (False, f"Error: Invalid path: '{path}'. Path must be a string.") 
    
    try:
        if not os.path.exists(path):
            # print(f"verify_directory_path - {path}")
            return (False, f"Path does not exist: '{path}'.")
        if not os.path.isdir(path):
            return (False, f"Path is not a directory: '{path}'.")
        return (True, "")
    # Catch odd edge cases - permission error
    except Exception as e:
        return (False, f"Invalid path: '{path}'. Error: {str(e)}")

# Verifiy given directory is within working_directory scope
def restrict_to_working_directory(working_directory, directory):
    try:
        working_dir_contents = os.listdir(working_directory)
    except Exception as e:
        err = f"Error: Failed to list contents of '{working_directory}': {str(e)}. Ensure the path is valid and accessible."
        return(False, err)
    
    if directory not in working_dir_contents and directory != ".":
        err = f'Error: Cannot list "{directory}" as it is outside the permitted working directoryy'
        # return(False,err, working_directory, directory)
        return(False,err)
    
    return (True, "")

def valid_directory(working_directory, directory):
    working_dir = os.path.abspath(working_directory)
    path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(path)

    # print(f"valid_directory - {abs_path}")
    # Check if a valid dirtory is given
    valid_directory, err = verify_directory_path(abs_path)
    if valid_directory and len(err) == 0:
        inscope, err = restrict_to_working_directory(working_dir, directory)

        if inscope and len(err) == 0:
            return (True, "", abs_path)
        
    return (False, err, abs_path)