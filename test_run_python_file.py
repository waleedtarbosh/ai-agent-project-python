from functions.run_python_file import run_python_file

print("--- Testing run main.py (Usage) ---")
print(run_python_file("calculator", "main.py"))

print("\n--- Testing run main.py with args (3 + 5) ---")
print(run_python_file("calculator", "main.py", ["3 + 5"]))

print("\n--- Testing run tests.py ---")
print(run_python_file("calculator", "tests.py"))

print("\n--- Testing Security (../main.py) ---")
print(run_python_file("calculator", "../main.py"))

print("\n--- Testing non-existent file ---")
print(run_python_file("calculator", "nonexistent.py"))

print("\n--- Testing non-python file (lorem.txt) ---")
print(run_python_file("calculator", "lorem.txt"))