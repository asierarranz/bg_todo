# Dynamic Wallpaper Changer for Windows

This project provides a Python script that dynamically updates the wallpaper on Windows systems based on the contents of a text file. It allows for displaying task lists, notes, or any text-based content directly on your desktop wallpaper.

## Features

- **Dynamic Update**: Change the wallpaper by modifying the text in a `.txt` file.
- **Customizable Text Appearance**: Customize the font, color, and size of the text displayed on the wallpaper.
- **Automatic Refresh**: Automatically updates the wallpaper when the text file changes.
- **Multi-Monitor Support** (Pending): Planning to support different wallpapers on multiple monitors.

## Prerequisites

Before you can use this script, make sure you have the following installed:
- [Python](https://www.python.org/downloads/) (3.6 or higher)
- [Pillow](https://pillow.readthedocs.io/en/stable/installation.html): Python Imaging Library (Fork)
- [pywin32](https://pypi.org/project/pywin32/): Python for Windows Extensions

To install Pillow and pywin32, run:
```bash
pip install Pillow pywin32
