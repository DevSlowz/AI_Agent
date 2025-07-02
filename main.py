import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import sys

# Load enviorment variables
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# Create instance of Gemini client
client = genai.Client(api_key=api_key)

def main():


    print("Hello from ai-agent!")
    # print(sys.argv)
    if len(sys.argv) == 1:
        print("ERROR: Prompt not provided")
        exit(1)
    else:
        messages = [
            types.Content(role="user", parts=[types.Part(text=sys.argv[1])]),
        ]
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages,
        )
        print(response.text)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
