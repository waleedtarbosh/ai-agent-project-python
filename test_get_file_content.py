from functions.get_file_content import get_file_content

print("--- Testing large file truncation ---")
result_lorem = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result_lorem)}")
print(f"lorem.txt truncated: {'truncated' in result_lorem}\n")

print("--- Testing main.py ---")
print(get_file_content("calculator", "main.py"))

print("\n--- Testing pkg/calculator.py ---")
print(get_file_content("calculator", "pkg/calculator.py"))

print("\n--- Testing out-of-bounds /bin/cat ---")
print(get_file_content("calculator", "/bin/cat"))

print("\n--- Testing non-existent file ---")
print(get_file_content("calculator", "pkg/does_not_exist.py"))