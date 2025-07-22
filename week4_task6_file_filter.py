import os
import re

def list_and_filter_text_files(directory_path, filename_pattern):
    if not os.path.isdir(directory_path):
        print(f"Error: The folder '{directory_path}' doesn't seem to exist or isn't a directory.")
        return

    print(f"Looking for '.txt' files in '{directory_path}' that match the pattern '{filename_pattern}':")

    for filename in os.listdir(directory_path):
        if filename.endswith(".txt") and re.match(filename_pattern, filename):
            print(filename)

# Create a test folder with sample files
test_dir_name = "my_test_docs"
if not os.path.exists(test_dir_name):
    os.makedirs(test_dir_name)

# Create test .txt and non-.txt files
with open(os.path.join(test_dir_name, "report_monthly.txt"), "w") as f:
    f.write("Dummy content")
with open(os.path.join(test_dir_name, "meeting_notes.txt"), "w") as f:
    f.write("Dummy content")
with open(os.path.join(test_dir_name, "report_final_v2.txt"), "w") as f:
    f.write("Dummy content")
with open(os.path.join(test_dir_name, "summary_report.txt"), "w") as f:
    f.write("Dummy content")
with open(os.path.join(test_dir_name, "image.jpg"), "w") as f:
    f.write("Not a text file")

# Run filter on that folder
current_script_directory = os.getcwd()
full_test_folder_path = os.path.join(current_script_directory, test_dir_name)

# Match files that contain the word 'report' anywhere in the filename
list_and_filter_text_files(full_test_folder_path, r".*report.*")
