import os

def main():
    print("Current Working Directory:", os.getcwd())
    
    # Create a new directory
    dir_name = "test_directory"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")
    
    # Create a new file inside the directory
    file_path = os.path.join(dir_name, "sample.txt")
    with open(file_path, "w") as file:
        file.write("Hello, this is a test file.\n")
    print(f"File '{file_path}' created and written to.")
    
    # List files in the directory
    print("Files in directory:", os.listdir(dir_name))
    
    # Rename the file
    new_file_path = os.path.join(dir_name, "renamed_sample.txt")
    os.rename(file_path, new_file_path)
    print(f"File renamed to '{new_file_path}'.")
    
    # Delete the file
    os.remove(new_file_path)
    print(f"File '{new_file_path}' deleted.")
    
    # Remove the directory
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")
    
if __name__ == "__main__":
    main()