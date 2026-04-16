import os

def find_folder(folder_name):

    start_directory = "C:\\" if os.name == "nt" else "/"
    found_paths = []

    for root, dirs, files in os.walk(start_directory):
        if folder_name in dirs:
            found_paths.append(os.path.join(root, folder_name))

    return found_paths