user_input = input("Enter some text to write to the file: ")

with open("newfile.txt", "w") as file:
    file.write(user_input + "\n")

print("Initial data written to output.txt.")

additional_input = input("Enter additional text to append to the file: ")

with open("newfile.txt", "a") as file:
    file.write(additional_input + "\n")

print("Additional data appended to output.txt.")

print("\nFinal contents of output.txt:")
with open("newfile.txt", "r") as file:
    content = file.read()
    print(content)
