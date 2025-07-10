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
            # Refactor repetitive directory path checks into a dedicated function to minimize code duplication 
            # and align with the "Write Once, Run Anywhere" principle.
            # TODO - Write a modular function for checking if somethig is a dir
            print(f"- {item}: {os.path.getsize(os.path.abspath(file_path))}, is_dir={os.path.isdir(file_path)}")
        # print(directory_contents)


    return abs_path

    pass 