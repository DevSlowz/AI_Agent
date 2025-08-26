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
    if verbose:
        print(f" - Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    # Access the name and args directly

    # print(f"Function calls are: {function_call_part}")
    # for func_call_part in function_call_part:
    # print(f"This is the func call part - {function_call_part}")
    function_call_part.args['working_directory'] = './calculator'
    print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    function_name = function_call_part.name
    args = function_call_part.args
    
    # print(f'This is the name of the function in call_function: {function_name}')
    # print(f"These are the arguments in call_function: {args}")
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

    # print(function_result)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )




def generate_content(client, messages, verbose):
    # Make the API call
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[avaliable_functions], 
            system_instruction=system_prompt
        ),
    )
    
    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    # Add the model's response to the conversation
    for candidate in response.candidates:
        # print(f"Candidate - {candidate.content.parts}")
        messages.append(candidate.content)
    
    # Check if this is a final response (no function calls)
    if not response.function_calls:
        print(f"Response.text - {response.text}")
        return response.text  # We're done!
    
    # Process each function call
    function_responses = []
    for function_call_part in response.function_calls:
        if verbose:
            print(f" - Calling function: {function_call_part.name}")
        
        # Call your function and get the result
        function_result = call_function(function_call_part, verbose)
        
        # Extract the function response part
        function_responses.append(function_result.parts[0])
    
    # Add function results to the conversation
    messages.append(types.Content(role="user", parts=function_responses))
    
    # Return None to indicate we need another iteration
    return None
    
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
    # generate_content_result = generate_content(client,messages,verbose)
    
    # for item in generate_content_result.candidates:
    #     # print(f"Item Content: {item.content}")
    #     messages.append(item.content)

    # print(messages)

    for i in range(20):
        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:  # If we got a final text response
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error: {e}")
            break

 

if __name__ == "__main__":
    main()