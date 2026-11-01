import os
import shutil
from pathlib import Path

# File extension categories
FILE_CATEGORIES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".ppt": "Documents",
    ".pptx": "Documents",
    ".xls": "Documents",
    ".xlsx": "Documents",

    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".bmp": "Images",

    ".mp4": "Videos",
    ".mkv": "Videos",
    ".avi": "Videos",
    ".mov": "Videos",

    ".zip": "Archives",
    ".rar": "Archives",
    ".7z": "Archives",
    ".tar": "Archives",

    ".py": "Code",
    ".java": "Code",
    ".c": "Code",
    ".cpp": "Code",
    ".html": "Code",
    ".css": "Code",
    ".js": "Code"
}


def organize_files(directory):

    folder = Path(directory)

    if not folder.exists() or not folder.is_dir():
        print("Error: Invalid directory!")
        return

    moved_count = 0
    skipped_count = 0

    print("\n================================")
    print("    AUTOMATED FILE ORGANIZER")
    print("================================")

    # Inspect files in the selected directory
    try:
        with os.scandir(folder) as entries:

            for entry in entries:

                if not entry.is_file():
                    continue

                file_path = Path(entry.path)
                extension = file_path.suffix.lower()

                # Identify file category
                category = FILE_CATEGORIES.get(extension)

                if category is None:
                    continue

                # Create category folder
                destination_folder = folder / category

                try:
                    destination_folder.mkdir(
                        parents=True,
                        exist_ok=True
                    )

                    destination = destination_folder / file_path.name

                    # Handle duplicate file names
                    counter = 1

                    while destination.exists():
                        destination = destination_folder / (
                            f"{file_path.stem}_{counter}"
                            f"{file_path.suffix}"
                        )
                        counter += 1

                    # Move the file
                    shutil.move(
                        str(file_path),
                        str(destination)
                    )

                    print(
                        f"[MOVED] {file_path.name}"
                        f" -> {category}/"
                    )

                    moved_count += 1

                except PermissionError:
                    print(
                        f"[ERROR] Permission denied: "
                        f"{file_path.name}"
                    )
                    skipped_count += 1

                except OSError as error:
                    print(
                        f"[ERROR] {file_path.name}: {error}"
                    )
                    skipped_count += 1

    except PermissionError:
        print("Error: Cannot access this directory!")
        return

    # Display summary
    print("\n================================")
    print("       EXECUTION SUMMARY")
    print("================================")
    print(f"Files relocated : {moved_count}")
    print(f"Files skipped   : {skipped_count}")
    print("Organization completed!")


if __name__ == "__main__":

    print("Enter the directory path to organize:")

    directory_path = input("> ").strip().strip('"')

    organize_files(directory_path)