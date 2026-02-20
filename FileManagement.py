import os
import shutil

def organize_directory(path='.'):
    """
    Organizes files in the specified directory into folders based on their extensions.
    """
    # Map extensions to folder names
    extensions_map = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx', '.xls', '.pptx', '.csv'],
        'Archives': ['.zip', '.rar', '.tar', '.gz', '.7z'],
        'Scripts': ['.py', '.js', '.html', '.css', '.java', '.cpp'],
        'Executables': ['.exe', '.msi', '.bat', '.sh'],
        'Data': ['.json', '.xml', '.sql']
    }

    # Ensure the path exists
    if not os.path.exists(path):
        print(f"The directory '{path}' does not exist.")
        return

    # List all files in the directory
    files = os.listdir(path)

    for file in files:
        file_path = os.path.join(path, file)

        # Skip directories and this script itself so it doesn't move itself
        if os.path.isdir(file_path) or file == os.path.basename(__file__):
            continue

        # Get the file extension
        _, ext = os.path.splitext(file)
        ext = ext.lower()

        # Skip files without extensions
        if not ext:
            continue

        # Find the category for the extension
        target_folder = 'Others'
        for category, extensions in extensions_map.items():
            if ext in extensions:
                target_folder = category
                break

        # Create the category directory if it doesn't exist
        target_path = os.path.join(path, target_folder)
        if not os.path.exists(target_path):
            os.makedirs(target_path)

        # Move the file
        try:
            shutil.move(file_path, os.path.join(target_path, file))
            print(f"Moved: {file} -> {target_folder}/")
        except Exception as e:
            print(f"Error moving {file}: {e}")

if __name__ == "__main__":
    # Runs organization on the current directory
    organize_directory()
