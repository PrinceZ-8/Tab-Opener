import PyInstaller.__main__

PyInstaller.__main__.run([
    'tabs.py',  # Your script
    '--windowed',  # Windowed app (no console)
    '--noconsole',  # No console window on launch
    '--icon=tab.icns',  # Application icon
    '--add-data', 'tabs.txt:.'  # Include tabs.txt in the bundle's current directory
])
