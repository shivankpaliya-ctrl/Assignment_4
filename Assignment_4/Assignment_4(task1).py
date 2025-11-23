file_name = "sample.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()
        print("Reading file content:")
        for i, line in enumerate(lines,start=1):
            print(f"Line {i}: {line.strip()}")
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")


