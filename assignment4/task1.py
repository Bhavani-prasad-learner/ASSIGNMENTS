try:
    # Try to open the file in read mode
    with open('sample.txt', 'r') as file:
        print("reading file content")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
