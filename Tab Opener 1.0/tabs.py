# import webbrowser
# #f = open("../Resources/tabs.txt", "r")
# #f = open("./tabs.txt", "r")
#
# #ls = ["https://www.youtube.com/","https://www.apple.com/","https://www.chatgpt.com/"]
#
# for url in f:
#     url = url.strip()
#     webbrowser.open(url)
#
# f.close()


import os
import sys
import webbrowser

def get_resource_path(filename):
    # When bundled, PyInstaller sets _MEIPASS to the temp extraction dir
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        # Development mode
        return os.path.join(os.path.abspath("."), filename)

file_path = get_resource_path("tabs.txt")

with open(file_path, "r") as f:
    for url in f:
        url = url.strip()
        if url:
            webbrowser.open(url)
