# Jesus Carlos Martinez Gonzalez
# 08/07/23
# Simple Random Color Palette Generator

# App was made following this https://www.youtube.com/watch?v=ujfsn6u-1QU&ab_channel=AlinaChudnova tutorial made by youtuber Alina Chudnova.

import tkinter as tk
import random


def generate_color():
    """Returns a string representing a hex color"""
    # color's rgb values
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = f"#{r:02x}{g:02x}{b:02x}"
    return color


def generate_palette():
    """Generates color palette"""
    num_colors = int(select_field.get())

    # Destroys previous color frame
    for widget in color_frame.winfo_children():
        widget.destroy()

    # Generates color data
    for i in range(num_colors):
        # Color
        color = generate_color()

        # Color display
        color_label = tk.Label(color_frame, bg=color, width=10, height=5)
        color_label.grid(row=i, column=0, padx=5, pady=5)

        # Color's hex value
        hex_label = tk.Label(color_frame, text=color, width=10)
        hex_label.grid(row=i, column=1, padx=5, pady=5)


# Window data
root = tk.Tk()
root.title("Color Palette Generator")
root.geometry("300x600")

# Select field (number of colors in palette)
select_field = tk.StringVar(value="1")
select = tk.OptionMenu(root, select_field, "1", "2", "3", "4", "5")
select.pack(side="top", pady=10)

# Generate button
generate_button = tk.Button(root, text="Generate", command=generate_palette)
generate_button.pack(side="top")

# Frame for color palette
color_frame = tk.Frame(root)
color_frame.pack(pady=10)

root.mainloop()
