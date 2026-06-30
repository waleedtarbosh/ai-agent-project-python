import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt

from call_function import available_functions, call_function

def main():
    parser = argparse.ArgumentParser(description="AI Agent CLI")
    parser.add_argument("user_prompt", type=str, help="The prompt to send to the AI")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    if api_key is None:
        raise RuntimeError("Error: GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part.from_text(text=args.user_prompt)])
    ]

    max_iterations = 20
    for i in range(max_iterations):
        if args.verbose:
            print(f"\n--- Iteration {i+1} ---")

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt,
                tools=[available_functions],
                temperature=0
            ),
        )

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls:
            function_results = []
            
            for function_call in response.function_calls:
                function_call_result = call_function(function_call, verbose=args.verbose)
                
                if not function_call_result.parts:
                    raise Exception("Function call result has no parts.")
                    
                first_part = function_call_result.parts[0]
                
                if not first_part.function_response:
                    raise Exception("Part does not contain a function_response.")
                    
                if first_part.function_response.response is None:
                    raise Exception("Function response does not contain a response dictionary.")
                    
                function_results.append(first_part)
                
                if args.verbose:
                    print(f"-> {first_part.function_response.response}")
            
            messages.append(types.Content(role="user", parts=function_results))
            
        else:
            if args.verbose:
                print("\nFinal Response:")
            
            print(response.text)
            return

    print("\nError: Agent reached maximum iterations (20) without completing the task.")
    sys.exit(1)

if __name__ == "__main__":
    main()