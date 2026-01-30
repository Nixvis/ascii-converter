chars = "@%#*+=-:. "
from PIL import Image
import tkinter as tk

X_SCALE = 2 # Step in the iteration of the list so the image isn't stretched width-wise

def load_pil(image, target_width=128): # Target width can be changed
    img = Image.open(image)
    
    img = img.convert("L") # Makes it grayscale

    original_width, original_height = img.size            # Resizing the image because of the size differnence between pixel and ascii chars
    aspect_ratio = original_height / original_width       # With tkinter and courier font 0.35 is ideal
    new_height = int(aspect_ratio * target_width * 0.35)
    img = img.resize((target_width, new_height))

    pixels = list(img.get_flattened_data())
    width, height = img.size

    rows = []
    for y in range(height): # Reshaping the list as a matrix
        row = pixels[y * width : (y + 1) * width]
        rows.append(row)

    return rows, width, height

image, width, height = load_pil("example.png")


def converter(image, chars): 

    ascii_rows = []                                  

    for i in range(len(image)):                            # Converts the matrix into strings so it can be displayed on tkinter
        ascii_row = ""
        for j in range(0, len(image[i]), X_SCALE):
            brightness = image[i][j]
            index = brightness * (len(chars) - 1) // 255
            ascii_row += chars[index]
        ascii_rows.append(ascii_row)

    return ascii_rows

ascii_image = converter(image, chars)

def show_ascii(ascii_image):

    root = tk.Tk()            # Actually creates the window
    root.title("ascii")
    text = tk.Text(           # Makes the widget that displayes the text
        root,
        font=("Courier", 3), 
        bg="black",
        fg="white"
    )
    text.pack(fill="both", expand=True)

    for line in ascii_image:              # Displays the text
        text.insert("end", line + "\n")

    text.config(state="disabled")  # Prevent editing
    root.mainloop()

show_ascii(ascii_image)



