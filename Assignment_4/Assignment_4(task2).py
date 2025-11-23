file_name = "output.txt"

text_to_write = input("Enter text to write to the file: ")
with open(file_name, "w") as file:
    file.write(text_to_write + "\n")
print("Data successfully written to output.txt.")


text_to_append = input("Enter additional text to append: ")
with open(file_name, "a") as file:
    file.write(text_to_append + "\n")
    print("Data successfully appended.")

print("/nFinal content of output.txt:")
with open(file_name, "r") as file:
    content = file.read()
print(content)