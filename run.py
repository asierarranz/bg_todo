from PIL import Image, ImageDraw, ImageFont
import os, ctypes

# Configuración
imagen_fondo_path = 'bg.png'  # Ruta de la imagen de fondo
texto_archivo_path = 'todo.txt'  # Ruta del archivo de texto
fuente_path = 'C:\\Windows\\Fonts\\consola.ttf'  # Ruta de la fuente Consolas
color_fuente = 'yellow'  # Color del texto
tamanio_fuente = 14  # Tamaño de la fuente

# Cargar la imagen de fondo
imagen = Image.open(imagen_fondo_path)
draw = ImageDraw.Draw(imagen)

# Cargar la fuente
fuente = ImageFont.truetype(fuente_path, tamanio_fuente)

# Leer el archivo de texto
with open(texto_archivo_path, 'r') as archivo:
    lineas = archivo.readlines()

# Posición inicial del texto
x = 1760
y = 10
line_spacing = 10  # Espaciado entre líneas

# Escribir texto sobre la imagen
for linea in lineas:
    texto = linea.strip()
    draw.text((x, y), texto, font=fuente, fill=color_fuente)
    # Usar getbbox para obtener las dimensiones del texto
    text_width, text_height = fuente.getbbox(texto)[2], fuente.getbbox(texto)[3]
    y += text_height + line_spacing

# Guardar la nueva imagen
imagen_guardada_path = 'bg2.png'
imagen_guardada_full_path = os.path.abspath(imagen_guardada_path)
imagen.save(imagen_guardada_full_path)

# Cambiar el fondo de pantalla usando SystemParametersInfo
SPI_SETDESKWALLPAPER = 20
SPIF_UPDATEINIFILE = 0x1
SPIF_SENDCHANGE = 0x2
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, imagen_guardada_full_path, SPIF_UPDATEINIFILE | SPIF_SENDCHANGE)
