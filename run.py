from PIL import Image, ImageDraw, ImageFont
import os, ctypes, time
import logging
from apscheduler.schedulers.background import BackgroundScheduler
from pystray import Icon as icon, MenuItem as item, Menu as menu
from PIL import Image as PILImage

# Setup logging
logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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

# Global to store the last modification time and privacy mode state
last_mod_time = None
privacy_mode = False

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
    global privacy_mode
    if privacy_mode:
        image_path = os.path.abspath(IMAGE_PATH)
    else:
        image_path = os.path.abspath(SAVED_IMAGE_PATH)
        create_dynamic_wallpaper(image_path)

    set_wallpaper(image_path)

def create_dynamic_wallpaper(image_path):
    logging.info("Creating wallpaper with todo items...")
    image = PILImage.open(IMAGE_PATH)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    
    with open(TEXT_FILE_PATH, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    y = START_Y
    for line in lines:
        text = line.strip()
        draw.text((START_X, y), text, font=font, fill=FONT_COLOR)
        text_height = draw.textbbox((START_X, y), text, font=font)[3] - draw.textbbox((START_X, y), text, font=font)[1]
        y += text_height + LINE_SPACING

    image.save(image_path)

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    SPIF_UPDATEINIFILE = 1
    SPIF_SENDCHANGE = 2
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
    logging.info("Wallpaper set: %s", result)

def toggle_privacy_mode(icon):
    global privacy_mode
    privacy_mode = not privacy_mode
    update_wallpaper()
    logging.info("Privacy mode toggled to: %s", privacy_mode)

def open_text_file():
    os.startfile(TEXT_FILE_PATH)

def on_quit(icon, scheduler):
    scheduler.shutdown(wait=False)
    icon.stop()

def setup(icon, scheduler):
    icon.menu = menu(
        item('Open Text File', open_text_file, default=True),
        item(lambda item: 'Disable Privacy' if privacy_mode else 'Enable Privacy', lambda item: toggle_privacy_mode(icon)),
        item('Quit', lambda icon: on_quit(icon, scheduler))
    )
    icon.visible = True

if __name__ == "__main__":
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=update_wallpaper, trigger='interval', seconds=5, id='wallpaper_update_job')
    scheduler.start()

    tray_icon = icon("Wallpaper Changer", PILImage.open(ICON_PATH), "Wallpaper Changer")
    tray_icon.run(lambda icon: setup(icon, scheduler))

    try:
        logging.info("Service started. Waiting for actions.")
    except KeyboardInterrupt:
        logging.info("Service interrupted by keyboard.")
    finally:
        scheduler.shutdown()
