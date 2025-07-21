import os

# Need to ensure the provided file_path is withing the bounds of the working_directory
# pkg/calculator.py is a valid path and we must structure the path to accomodate this

def get_file_content(working_directory, file_path):
    dir_content = os.listdir(working_directory)
    path = os.path.join(working_directory,file_path)
    is_file = os.path.isfile(path)
    # print(dir_content)
    # print(f"PATH = {path}")
    # print(is_file)

    is_valid = verify_file_path(working_directory, file_path)

    # It len > 2 it contains a error 
    if len(is_valid[1]) > 0:
        print(is_valid[1])
        # print(is_valid)
    else:
       test = read_file(path)
       print(test) 

    

def verify_file_path(working_directory, file_path):
    # dir_content = os.listdir(working_directory)
    file = ""
    if len(file_path.split('/')) > 0:
        file = file_path.split('/')[-1:]
        # print(f'file - {file}')
        # dir_contents = os.listdir()
        file_parent_dir = "/".join(file_path.split('/')[:-1])
        # print(f'file_path - {file_path}')
        # print(file)
    try:
        path = os.path.abspath(os.path.join(working_directory,file_parent_dir))
        # print(f'PATH - {path}')
        path_exists = os.path.exists(path)
        if path_exists:
            try:
                file_path = path + '/' + file[0]
                # print(f'FINAL FILE PATH - {file_path}')
                is_file = os.path.isfile(file_path)
                if not is_file:
                    return(False, f'Error: File not found or is not a regular file: "{file_path}"')
            except Exception as e:
                return(False, f'Error: {e}')
        else:
            return(False, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory eeee')
    except Exception as e:
        return(False, f'Error: {e}')
    
    
    return(True, "")


def read_file(file_path):
    MAX_CHARS = 10000
    
    with open(file_path, "r") as f:
        file_content_string = f.read(MAX_CHARS)

        if f.read(1):
            return(f"{(file_content_string)}{f'[...File "{file_path}" truncated at 10000 characters]'}")
            
    return file_content_string