# Dynamic Wallpaper Changer for Windows

This project provides a Python script that dynamically updates the wallpaper on Windows systems based on the contents of a text file. It allows for displaying task lists, notes, or any text-based content directly on your desktop wallpaper.

## Features

- **Dynamic Update**: Automatically changes the wallpaper by modifying the text in a `.txt` file.
- **Customizable Text Appearance**: Customize the font, color, and size of the text displayed on the wallpaper.
- **Automatic Refresh**: The wallpaper updates immediately when the text file changes, thanks to real-time monitoring.
- **Multi-Monitor Support** (Pending): Planning to support different wallpapers on multiple monitors.
- **System Tray Integration**: Runs from the system tray for easy access to wallpaper settings and controls.
- **Robust Background Operation**: Utilizes a background scheduler to manage updates smoothly without affecting system performance.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.6 or higher) - Programming language required to run the script.
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html) - Python Imaging Library (Fork), used for image manipulation.
- [pywin32](https://pypi.org/project/pywin32/) - Python extensions for Windows.
- [APScheduler](https://apscheduler.readthedocs.io/en/stable/) - Advanced Python Scheduler used for scheduling tasks.

## Installation

First, clone the repository or download the source code. Then, navigate to the script directory and install the required packages:

\```bash
pip install Pillow pywin32 APScheduler
\```

## Configuration

Before running the script, configure the paths and appearance settings in the script file:

- `IMAGE_PATH`: Path to the background image.
- `TEXT_FILE_PATH`: Path to the text file that contains the text to display on the wallpaper.
- `FONT_PATH`: Path to the `.ttf` file for the font used for text (e.g., `C:\\Windows\\Fonts\\consola.ttf`).
- `FONT_SIZE`: Font size for the text.
- `FONT_COLOR`: Color of the text (e.g., `"yellow"`).

## Usage

To run the script:

1. Open a command prompt or terminal.
2. Navigate to the folder containing the script.
3. Run the script using Python:

\```bash
python run.py
\```

The script will minimize to the system tray. Right-click the tray icon to open the text file, update the wallpaper, or quit the application.

## Building as an Executable

To create a standalone executable that runs without a visible console:

1. Install PyInstaller:

\```bash
pip install pyinstaller
\```

2. Compile the script:

\```bash
pyinstaller --onefile --windowed --hidden-import='apscheduler.schedulers.background' --hidden-import='apscheduler.triggers.interval' --hidden-import='apscheduler.executors.default' run.py
\```

This will generate an executable in the `dist` folder that runs in the background without showing a console window.

## Logging

The application logs its operations in `app.log`. Check this file if you encounter issues or need to troubleshoot.
