import os
import re

def update_logo():
    """
    Updates the logo path in all HTML files in the current directory and its subdirectories.
    """
    file_counter = 0
    for root, _, files in os.walk("."):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                # Regex to find img tags with LOGO in src
                logo_regex = re.compile(r'<img[^>]*src=(['"])(.*?LOGO.*?)\1', re.IGNORECASE)
                matches = logo_regex.finditer(content)

                # Keep track of the changes to be made
                changes = []

                for match in matches:
                    old_path = match.group(2)
                    # Normalize path separators
                    normalized_filepath = os.path.normpath(filepath)
                    # Determine the depth of the file relative to the root
                    depth = len(normalized_filepath.split(os.sep)) - 1
                    # Construct the new relative path
                    new_path = os.path.join(*([".."] * (depth-1)), "Images", "SpecCon-LOGO.png").replace("\", "/")
                    if not new_path.startswith("..") and not new_path.startswith("Images"):
                        new_path = "./" + new_path

                    changes.append((old_path, new_path))

                if changes:
                    # Apply the changes to the content
                    for old, new in changes:
                        content = content.replace(old, new)

                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    
                    print(f"Updated logo in {filepath}")
                    file_counter += 1
                else:
                    print(f"No logo found in {filepath}")

    print(f"Finished updating logos. Updated {file_counter} files.")

if __name__ == "__main__":
    update_logo()