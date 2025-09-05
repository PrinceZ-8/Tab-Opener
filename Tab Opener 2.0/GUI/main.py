import flet as ft
import os
import webbrowser
import subprocess

def get_file_dir():
    # Get the path to the Application Support directory in the user's home folder
    file_dir = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "TabOpenerFlet")

    # Create the directory if it doesn't exist
    fp = os.path.join(file_dir, "Tabs.txt")

    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
        with open(fp, 'w') as f:
            pass  # No content is written, resulting in a blank file

    return file_dir

file_path = os.path.join(get_file_dir(), "Tabs.txt")


def open_file_click(e):
    print("Button 1 clicked")
    subprocess.run(["open", "-a", "TextEdit", file_path])

def launch_tabs_click(e):
    print("Button 2 clicked")
    with open(file_path, "r") as f:
        for url in f:
            url = url.strip()
            webbrowser.open(url)


def main(page: ft.Page):
    page.title = "Tab Opener"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    open_file = ft.ElevatedButton(
        text="Open File",
        on_click=open_file_click  # Event handler for Button 1 here
    )

    launch_tabs = ft.ElevatedButton(
        text="Launch Tabs",
        on_click=launch_tabs_click  # Event handler for Button 2 here
    )

    # Add buttons to the page
    page.add(open_file, launch_tabs)

# Run the app
ft.app(target=main)
