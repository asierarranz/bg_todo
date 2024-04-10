from PIL import Image, ImageDraw, ImageFont
import os, ctypes, time
from pystray import Icon as icon, MenuItem as item, Menu as menu
from PIL import Image as PILImage

# Constants for paths and text style
IMAGE_PATH = 'bg.png'
TEXT_FILE_PATH = 'todo.txt'
FONT_PATH = 'C:\\Windows\\Fonts\\consola.ttf'
SAVED_IMAGE_PATH = 'bg2.png'
ICON_PATH = 'bgicon.ico'
FONT_SIZE = 14
FONT_COLOR = 'yellow'
START_X, START_Y = 1760, 10
LINE_SPACING = 10


# Global to store the last modification time
last_mod_time = None

def check_for_changes():
    global last_mod_time
    current_mod_time = os.path.getmtime(TEXT_FILE_PATH)
    if last_mod_time is None:
        last_mod_time = current_mod_time
        return False
    if current_mod_time != last_mod_time:
        last_mod_time = current_mod_time
        return True
    return False

def update_wallpaper():
    image = PILImage.open(IMAGE_PATH)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    
    with open(TEXT_FILE_PATH, 'r') as file:
        lines = file.readlines()

    y = START_Y
    for line in lines:
        text = line.strip()
        draw.text((START_X, y), text, font=font, fill=FONT_COLOR)
        _, text_height = font.getbbox(text)[2:4]
        y += text_height + LINE_SPACING

    full_path = os.path.abspath(SAVED_IMAGE_PATH)
    image.save(full_path)

    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    SPIF_SENDCHANGE = 2
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, full_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)

def open_text_file():
    os.startfile(TEXT_FILE_PATH)

def on_quit(icon, item):
    icon.stop()

def setup(icon):
    icon.visible = True

if __name__ == "__main__":
    icon_image = PILImage.open(ICON_PATH)
    menu_items = menu(
        item('Open Text File', open_text_file, default=True),
        item('Update Wallpaper', update_wallpaper),
        item('Quit', on_quit)
    )

    tray_icon = icon("WallpaperChanger", icon_image, "Wallpaper Changer", menu=menu_items)
    tray_icon.run(setup)

    try:
        while True:
            time.sleep(5)  # Check every 5 seconds for file change
            if check_for_changes():
                update_wallpaper()
    except KeyboardInterrupt:
        pass