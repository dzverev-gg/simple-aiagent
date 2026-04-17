import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

from prompts import system_prompt
from functions.get_files_info import schema_get_files_info

def main():

    parser = argparse.ArgumentParser(description= "simple-aiagent")
    parser.add_argument("user_prompt", type=str, help="Input your question to recieve an imfinite wisdom from AI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("missing gemini api key")

    client = genai.Client(api_key=api_key)
    available_functions = types.Tool(
            function_declarations=[schema_get_files_info],
            )
    

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]
    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(system_instruction=system_prompt,
                                               tools=[available_functions]),
            )
    

    if response.usage_metadata is None:
        raise RuntimeError('empty usage data')



    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count


    if args.verbose:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

    if response.function_calls is not None:
        for function_call in response.function_calls:
            print(f"Calling function: {function_call.name}({function_call.args})")
    
    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
