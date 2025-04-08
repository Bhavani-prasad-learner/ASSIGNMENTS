# Step 1: Take user input and write it to output.txt
user_input = input("Enter some text to write to the file: ")

with open('output.txt', 'w') as file:
    file.write(user_input + '\n')  # Write the user input to the file
print("data successfilly written in to output.txt")
# Step 2: Append additional data to the same file
additional_data = input("Enter additional text to append to the file: ")

with open('output.txt', 'a') as file:
    file.write(additional_data + '\n')  # Append the additional data
print("data is succesfully appended")
# Step 3: Read and display the final content of the file
print("\nFinal content of the file 'output.txt':")
with open('output.txt', 'r') as file:
    content = file.read()
    print(content)
