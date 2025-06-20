import os
import shutil
import re


# Idea 1 - Move all .jpg files from one folder to another
def move_jpg_files(source_folder, destination_folder):
    """Moves all .jpg files from a source folder to a destination folder."""

    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for filename in os.listdir(source_folder):
        if filename.endswith(".jpg"):
            source_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)
            shutil.move(source_path, destination_path)
            print(f"Moved {filename} to {destination_folder}")

# This script moves all .jpg files from a specified source folder to a specified destination folder.
# Ensure that the source folder exists and contains .jpg files before running the script.
# The script creates the destination folder if it does not exist. 


# Idea 2 - Extract email addresses from a text file and save them to another file
def extract_emails(input_file, output_file):
    """
    Extracts all email addresses from a text file and saves them to another file.

    Args:
        input_file (str): The path to the input text file.
        output_file (str): The path to the output file to save the extracted email addresses.
    """
    try:
        with open(input_file, 'r') as infile:
            text = infile.read()
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
        return

    emails = re.findall(r'[a-zA-Z0-9._%+-+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text)

    try:
        with open(output_file, 'w') as outfile:
            for email in emails:
                outfile.write(email + '\n')
        print(f"Successfully extracted {len(emails)} email addresses and saved to '{output_file}'")
    except Exception as e:
        print(f"Error writing to output file '{output_file}': {e}")
# This script extracts email addresses from a specified input text file and saves them to an output file.
# Ensure that the input file exists and contains text before running the script.
# The script uses regular expressions to find email patterns and writes them to the output file.


# Idea 3 - Rename files in a directory by adding a prefix
def rename_files_with_prefix(directory, prefix):
    """
    Renames all files in a directory by adding a specified prefix.

    Args:
        directory (str): The path to the directory containing files to rename.
        prefix (str): The prefix to add to each file name.
    """
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            new_name = prefix + filename
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
            print(f"Renamed '{filename}' to '{new_name}'")

# This script renames all files in a specified directory by adding a given prefix to each file name.
# Ensure that the directory exists and contains files before running the script.
# The script checks if the directory exists and renames each file accordingly.


if __name__ == "__main__":
    # Idea 1 - Move all .jpg files from one folder to another
    source_folder_1 = "source_folder_1"  # Example folder name
    destination_folder_1 = "destination_folder_1"  # Example folder name
    instance_move_jpg_files = move_jpg_files(source_folder_1, destination_folder_1) #Calling the function will execute it, there is nothing to instance.

    # Idea 2 - Extract email addresses from a text file and save them to another file
    input_file_2 = "input.txt"  # Example input file name
    output_file_2 = "emails.txt"  # Example output file name
    instance_extract_emails = extract_emails(input_file_2, output_file_2) # Calling the function will execute it, there is nothing to instance.

    # Idea 3 - Rename files in a directory by adding a prefix
    directory_3 = "my_directory"  # Example directory name
    prefix_3 = "prefix_"  # Example prefix
    instance_rename_files_with_prefix = rename_files_with_prefix(directory_3, prefix_3) # Calling the function will execute it, there is nothing to instance.

