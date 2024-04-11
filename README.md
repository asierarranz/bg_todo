# ToDo List Background Integrator for Windows

This project provides a Python script that integrates your ToDo list directly into your desktop wallpaper on Windows systems. It dynamically updates the wallpaper to display your current tasks, notes, or any text-based content that you wish to keep visible at all times.

![ToDo List on Desktop Wallpaper](sample.png)

## Features

- **Dynamic ToDo List Update**: Automatically updates the wallpaper with the contents of a `.txt` file—your ToDo list.
- **Customizable Text Appearance**: Customize the font, color, and size of the text displayed on your desktop.
- **Automatic Refresh**: The wallpaper refreshes immediately when the ToDo list file changes, thanks to real-time monitoring.
- **Multi-Monitor Support** (Pending): Plans to support different ToDo lists on multiple monitors.
- **System Tray Integration**: Conveniently runs from the system tray for easy access to settings and controls.
- **Robust Background Operation**: Utilizes a background scheduler to ensure that updates do not interrupt your workflow.

## Prerequisites

Before you can use this script, make sure you have the following installed:

- [Python](https://www.python.org/downloads/) (3.6 or higher) - Required to run the script.

## Installation

First, clone the repository or download the source code:

\```bash
git clone https://github.com/asierarranz/bg_todo.git
cd yourrepository
\```

Then, install the necessary packages using the provided `requirements.txt`:

\```bash
pip install -r requirements.txt
\```

## Configuration

Configure the paths and appearance settings in the script file before running:

- `IMAGE_PATH`: Path to the background image.
- `TEXT_FILE_PATH`: Path to the text file containing your ToDo list.
- `FONT_PATH`: Path to the `.ttf` font file used for displaying the list (e.g., `C:\\Windows\\Fonts\\consola.ttf`).
- `FONT_SIZE`: Font size of the list text.
- `FONT_COLOR`: Color of the list text (e.g., `"yellow"`).

## Usage

To run the script:

1. Open a command prompt or terminal.
2. Navigate to the folder containing the script.
3. Execute the script using Python:

\```bash
python run.py
\```

The script will minimize to the system tray. Right-click the tray icon to open the ToDo list file, update the wallpaper, or quit the application.

## Building as an Executable

Create a standalone executable that runs without a visible console:

1. Install PyInstaller if not already installed:

\```bash
pip install pyinstaller
\```

2. Compile the script:

\```bash
pyinstaller --onefile --windowed --hidden-import='apscheduler.schedulers.background' --hidden-import='apscheduler.triggers.interval' --hidden-import='apscheduler.executors.default' run.py
\```

This will generate an executable in the `dist` folder that operates in the background.

## Logging

The application logs its operations in `app.log`. Check this file for troubleshooting or understanding application behavior.
