import os

def main():
    print("Current Working Directory:", os.getcwd())
    dir_name = "test_directory"
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
        print(f"Directory '{dir_name}' created.")
    else:
        print(f"Directory '{dir_name}' already exists.")
    file_path = os.path.join(dir_name, "sample.txt")
    with open(file_path, "w") as file:
        file.write("Hello, this is a test file.\n")
    print(f"File '{file_path}' created and written to.")
    print("Files in directory:", os.listdir(dir_name))
    new_file_path = os.path.join(dir_name, "renamed_sample.txt")
    os.rename(file_path, new_file_path)
    print(f"File renamed to '{new_file_path}'.")
    os.remove(new_file_path)
    print(f"File '{new_file_path}' deleted.")
    os.rmdir(dir_name)
    print(f"Directory '{dir_name}' removed.")
    
if __name__ == "__main__":
    main()