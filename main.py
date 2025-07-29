import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys
from google.genai import types

from functions.get_files_info import schema_get_files_info

system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
avaliable_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
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

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
    print("Response:")
    print(response.text)
    print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")


if __name__ == "__main__":
    main()
