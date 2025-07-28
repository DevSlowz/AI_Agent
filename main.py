import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys


SYSTEM_PROMPT = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'
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
        config=types.GenerateContentConfig(system_instruction=SYSTEM_PROMPT),
    )

    if verbose:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
