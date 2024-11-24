# File name
file_name = "mine.txt"

# File names
original_file = "mine.txt"
new_file = "modified_mine.txt"

# Read the content from the original file
with open(original_file, "r") as file:
    content = file.read()  # Read the entire content

# Modify the content (convert to uppercase in this case)
modified_content = content.upper()

# Write the modified content to a new file
with open(new_file, "w") as file:
    file.write(modified_content)

#print(f"Modified content has been written to '{new_file}'!")



#Error handling and exception
try:
    file = open("text.txt", "r")
    print(file.read())
except FileNotFoundError:
    print("this file is not found")
finally:
    print("any statement")




 













