def read_file(filename):
    try:
        with open(filename, "r") as file:
            print("Reading file content:")
            for index, line in enumerate(file, start=1):
                print(f"Line {index}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

with open("file.txt", "w") as file:
    file.write("This is a sample text file.\n")
    file.write("It contains multiple lines.")

read_file("file.txt")
print()

# if file does not exist
read_file("missing_file.txt")
