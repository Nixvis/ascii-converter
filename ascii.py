chars = "@%#*+=-:. "
from PIL import Image
import tkinter as tk
X_SCALE = 2

def load_pil(image, target_width=128):
    img = Image.open(image)

    img = img.convert("L")

    original_width, original_height = img.size
    aspect_ratio = original_height / original_width
    new_height = int(aspect_ratio * target_width * 0.35)
    img = img.resize((target_width, new_height))

    pixels = list(img.get_flattened_data())
    width, height = img.size

    rows = []
    for y in range(height):
        row = pixels[y * width : (y + 1) * width]
        rows.append(row)

    return rows, width, height

def load_pgm(pgm):

    with open(pgm, "r") as f:

        data = f.read()
        tokens = data.split()
        width = int(tokens[1])
        height = int(tokens[2])
        pixel_tokens = tokens[4:]
        pixels = [int(p) for p in pixel_tokens]

        image = []
        index = 0

    for row in range(height):
        image_row = []
        for col in range(width):
            image_row.append(pixels[index])
            index += 1
        image.append(image_row)

    return image, width, height

image, width, height = load_pil("xv_9_t.jpg",1300)


def converter(image, chars):

    ascii_rows = []

    for i in range(len(image)):
        ascii_row = ""
        for j in range(0, len(image[i]), X_SCALE):
            brightness = image[i][j]
            index = brightness * (len(chars) - 1) // 255
            ascii_row += chars[index]
        ascii_rows.append(ascii_row)

    return ascii_rows

ascii_image = converter(image, chars)

def show_ascii(ascii_image):

    root = tk.Tk()
    root.title("ascii")
    text = tk.Text(
        root,
        font=("Courier", 3),  # monospaced is mandatory
        bg="black",
        fg="white"
    )
    text.pack(fill="both", expand=True)

    for line in ascii_image:
        text.insert("end", line + "\n")

    text.config(state="disabled")  # prevent editing
    root.mainloop()

show_ascii(ascii_image)



