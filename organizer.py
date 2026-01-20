import os
import shutil

# Ask user for folder path
folder_path = input("Enter the folder path to organize: ")

# File type categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv"],
    "PDFs": [".pdf"]
}

# Create folders if not exist
for folder in file_types:
    folder_full_path = os.path.join(folder_path, folder)
    if not os.path.exists(folder_full_path):
        os.mkdir(folder_full_path)

# Create Others folder
others_path = os.path.join(folder_path, "Others")
if not os.path.exists(others_path):
    os.mkdir(others_path)

# Move files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        moved = False
        for folder, extensions in file_types.items():
            if file.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(folder_path, folder, file))
                moved = True
                break

        if not moved:
            shutil.move(file_path, os.path.join(folder_path, "Others", file))

print("✅ Files organized successfully!")