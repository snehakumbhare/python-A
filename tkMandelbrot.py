
#Create a Mandelbrot Fractal image with Python and Tkinter
import tkinter as tk

# Define constants for the canvas size and zoom level
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
ZOOM_LEVEL = 150

# Function to generate a Mandelbrot fractal
def generate_mandelbrot(canvas):
    for x in range(CANVAS_WIDTH):
        for y in range(CANVAS_HEIGHT):
            zx, zy = x * 3.5 / CANVAS_WIDTH - 2.5, y * 2.0 / CANVAS_HEIGHT - 1.0
            c = zx + zy * 1j
            z = c
            color = 0
            for i in range(256):
                if abs(z) > 2.0:
                    color = i
                    break 
                z = z * z + c
            color_hex = f"#{color:02x}{color:02x}{color:02x}"
            canvas.create_rectangle(x, y, x + 1, y + 1, fill=color_hex, outline=color_hex)

# Create the main window
root = tk.Tk()
root.title("Mandelbrot Fractal")

# Create a Canvas widget
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

# Generate and display the Mandelbrot fractal
generate_mandelbrot(canvas)

# Start the Tkinter main loop
root.mainloop()
