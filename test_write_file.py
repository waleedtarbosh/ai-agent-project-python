from functions.write_file import write_file

print("--- Testing writing to existing file ---")
print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

print("\n--- Testing writing to new file in sub-directory ---")
print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

print("\n--- Testing invalid path (Security Check) ---")
print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))