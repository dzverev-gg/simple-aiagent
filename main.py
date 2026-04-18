import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

from prompts import system_prompt
#import functions schemas
# TODO: move schemas to a separate file
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
#import function call
from call_function import call_function

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
            function_declarations=[schema_get_files_info, schema_get_file_content, schema_write_file, schema_run_python_file],
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

    function_results = []
    if response.function_calls is not None:
        for function_call in response.function_calls:
            function_call_result = call_function(function_call, args.verbose)
            if len(function_call_result.parts) == 0:
                raise Exception("Incorrect function result")
            if function_call_result.parts[0].function_response is None:
                raise Exception("Empty function result paramenter")
            if function_call_result.parts[0].function_response.response is None:
                raise Exception("Empty function call result")
            function_results.append(function_call_result.parts[0])
            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    print("Response:")
    print(response.text)


if __name__ == "__main__":
    main()
