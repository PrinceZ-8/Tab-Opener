import os
import webbrowser

def get_app_support_path():
    # Get the path to the Application Support directory in the user's home folder
    app_support_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Temp2")

    # Create the directory if it doesn't exist
    if not os.path.exists(app_support_dir):
        print("Created")
        os.makedirs(app_support_dir)

    return app_support_dir


def write_to_file(filename, content):
    app_support_dir = get_app_support_path()
    file_path = os.path.join(app_support_dir, filename)

    with open(file_path, "w") as file:
        file.write(content)
    print(f"Data written to {file_path}")

write_to_file("Tabs.txt", "https://www.apple.com/")

file_path = os.path.join(get_app_support_path(), "Tabs.txt")
with open(file_path, "r") as f:
    url = f.readline()
    webbrowser.open_new_tab(url)