import os


def get_files_info(working_directory, directory=None):
    # working_directory is the directory we wannt to search in
    # directory is the content we want to display within the working_directory
    # Example get_files_info(calculator, ".") = Working inside the scope of the calculator directory 
    # List the contents 
    # path = f'{working_directory}/{directory}'

    # NOTE: Return statements will need to be print statements that way the agent can try to determine the error
    # NOTE: Might want to consider not storing err messages multiple times to avoid rewrite the variable
    working_dir = os.path.abspath(working_directory)
    path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(path)

    # Check if a valid dirtory is given
    # This can be its own func - easy testing
    is_directory = os.path.isdir(abs_path)
    if not is_directory:
        err = f'Error: "{directory}" is not a directory'
        return(err, directory)
    
    valid_directory, err = verify_directory_path(abs_path)
    if valid_directory and len(err) == 0:
        inscope, err = restrict_to_working_directory(working_dir, directory)
    # Check if path is in the scope of the working_directory
    # This can be its own func - easy testing
    working_dir_contents = os.listdir(working_dir)
    if directory not in working_dir_contents:
        err = f'Error: "{directory}" is not a directory'
        return(err, working_directory, directory)
    
    # Case of a valid directory
    # Will need to loop over working_dir_contents and use an os function to print details
    directory_contents = os.listdir(abs_path)
    content = []
    if directory in working_dir_contents and is_directory:
        for item in directory_contents:
            file_path = path = os.path.join(abs_path, item)
            item = item.strip('.')
            # Refactor repetitive directory path checks into a dedicated function to minimize code duplication 
            # and align with the "Write Once, Run Anywhere" principle.
            # TODO - Write a modular function for checking if somethig is a dirß
            print(f"- {item}: {os.path.getsize(os.path.abspath(file_path))} bytes, is_dir={os.path.isdir(file_path)}")
        # print(f"{directory_contents}")


    return abs_path

      
    # Check if path is in the scope of the working_directory
    # This can be its own func - easy testing

    
# Check if a valid dirtory is given
def verify_directory_path(path):
    try:
        is_directory = os.path.isdir(path)
    except Exception as e:
       err = f"Invalid path: '{path}'. Ensure the path is a valid string and accessible. Error: {str(e)}"
       return(False, err)
    if not is_directory:
        err = f'Error: "{is_directory}" is not a directory'
        return(False, err)
    return (True, "")

# Verifiy given directory is within working_directory scope
def restrict_to_working_directory(working_directory, directory):
    try:
        working_dir_contents = os.listdir(working_directory)
    except Exception as e:
        err = f"Failed to list contents of '{working_directory}': {str(e)}. Ensure the path is valid and accessible."
        return(False, err)
    
    if directory not in working_dir_contents:
        err = f'Error: "{directory}" is not a directory'
        return(err, working_directory, directory)
    
    return (True, "")

def valid_directory(working_directory, directory):
    working_dir = os.path.abspath(working_directory)
    path = os.path.join(working_directory, directory)
    abs_path = os.path.abspath(path)

    # Check if a valid dirtory is given
    valid_directory, err = verify_directory_path(abs_path)
    if valid_directory and len(err) == 0:
        inscope, err = restrict_to_working_directory(working_dir, directory)

        if inscope and len(err) == 0:
            return (True, "")
        
    return (False, err)