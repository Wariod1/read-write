# Prompt the user to enter the name of the file to read
filename = input("Enter the name of the file to read: ")

try:
    # Open the file in read mode
    with open(filename, "r") as file:
        content = file.read()
    
    # Transform the content 
    modified_content = content.upper()
    
    # Define the name for the output file
    new_filename = "modified_" + filename

    # Open the output file in write mode and save the modified content
    with open(new_filename, "w") as new_file:
        new_file.write(modified_content)
    
    # Confirm success to the user
    print(f"File processed successfully! Modified file saved as {new_filename}")

except FileNotFoundError:
    # Handle the case where the file doesn't exist
    print("Error: The file does not exist.")
except PermissionError:
    # Handle the case where the file can't be accessed due to permissions
    print("Error: You do not have permission to read this file.")
except Exception as e:
    # Catch any other unexpected exceptions
    print(f"An unexpected error occurred: {e}")
