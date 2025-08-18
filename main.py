import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from google.genai import types

from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python import schema_run_python_file
from functions.write_file import schema_write_file

from functions.write_file import write_file
from functions.run_python import run_python_file
from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
Do no
"""
avaliable_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

avaliable_function_calls = {
    "write_file": write_file,
    "run_python_file": run_python_file,
    "get_file_content": get_file_content,
    "get_files_info": get_files_info,
}

def call_function(function_call_part, verbose=False):
    name = ""
    args = ""
    if verbose == False:
        for function_call_part in function_call_part.function_calls:
            print(f" - Calling function: {function_call_part.name}")
        # return

    print(f"Function calls are: {function_call_part}")
    for function_call_part in function_call_part.function_calls:
        function_call_part.args['working_directory'] = './calculator'
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        function_name = function_call_part.name
        args = function_call_part.args
    
    print(f'This is the name of the function in call_function: {function_name}')
    print(f"These are the arguments in call_function: {args}")
    # print(type(args))

    if function_name not in avaliable_function_calls:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )

    # function_result = avaliable_function_calls[function_name](working_directory=args['working_directory'], file_path=args['file_path'], content=args['content'])
    function_result = avaliable_function_calls[function_name](**args)

    print(function_result)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
def main():

    # Load enviorment variables
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    # Create instance of Gemini client
    client = genai.Client(api_key=api_key)

    # Check if verbose flag is included in command
    verbose = "--verbose" in sys.argv[1:]
    # Check if all user passed commands follow valid syntax
    valid_args = [arg for arg in sys.argv[1:] if not arg.startswith('--')]

    # Display propper command use when invalid commands are passed
    if not valid_args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    user_prompt = " ".join(valid_args)



    # if user uses verbose command display additional information
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    # Store conversation history and assign roles
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    generate_content(client,messages,verbose)



def generate_content(client, messages, verbose):
    # Generate reponse based on messages argument
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[avaliable_functions], system_instruction=system_prompt
        ),
        
    )

    print("Response:")

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        result = call_function(response, verbose)
        try:
            print(f"-> {result.parts[0].function_response.response}")
            return
        except Exception as e:
            raise Exception(e)

    if not response.function_calls:
        return response.text

    # print(f"The response I am passing is : {response}")
    result = call_function(response)
    print(f"The result is {result}")

    try:
        print(result.parts[0].function_response.response)
        return
    except Exception as e:
        raise Exception(e)

    # print(response.text)
    




if __name__ == "__main__":
    main()
