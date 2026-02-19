import os

def print_folder_structure(folder_path, indent="", is_last=True):
    """
    Recursively prints the folder structure of a given directory,
    including both folders and files.
    """
    name = os.path.basename(folder_path)

    # Print root or subtree element
    if indent == "":
        print(name)
    else:
        prefix = "└── " if is_last else "├── "
        print(indent + prefix + name)

    try:
        items = sorted(os.listdir(folder_path))

        # Separate folders and files
        folders = [item for item in items if os.path.isdir(os.path.join(folder_path, item))]
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]

        # Combine folders first, then files
        all_items = folders + files

        # Prepare indentation for children
        if indent == "":
            new_indent = "    "
        else:
            new_indent = indent + ("    " if is_last else "│   ")

        for i, item in enumerate(all_items):
            is_last_item = (i == len(all_items) - 1)
            item_path = os.path.join(folder_path, item)

            if os.path.isdir(item_path):
                print_folder_structure(item_path, new_indent, is_last_item)
            else:
                prefix = "└── " if is_last_item else "├── "
                print(new_indent + prefix + item)

    except PermissionError:
        print(indent + "    [Permission Denied]")
    except FileNotFoundError:
        print(f"Error: The folder '{folder_path}' does not exist.")
    except NotADirectoryError:
        print(f"Error: '{folder_path}' is not a directory.")


def main():
    folder_path = input("Enter the folder path: ").strip()
    folder_path = folder_path.strip('"').strip("'")

    if not os.path.exists(folder_path):
        print(f"Error: The path '{folder_path}' does not exist.")
        return

    if not os.path.isdir(folder_path):
        print(f"Error: '{folder_path}' is not a directory.")
        return

    print(f"\nFolder structure for: {folder_path}\n")
    print_folder_structure(folder_path)


if __name__ == "__main__":
    main()
