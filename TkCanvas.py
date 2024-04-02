#Python Tkinter canvas shape editor: Drawing and manipulating shapes
import tkinter as tk
class ShapeEditorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Editor")

        # Create Canvas widget
        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # Initialize shape variables
        self.current_shape = None
        self.start_x = None
        self.start_y = None
        self.current_shape_item = None

        # Create buttons
        self.rect_button = tk.Button(root, text="Rectangle", command=self.create_rectangle)
        self.circle_button = tk.Button(root, text="Circle", command=self.create_circle)
        self.clear_button = tk.Button(root, text="Clear", command=self.clear_canvas)
        self.rect_button.pack(side=tk.LEFT)
        self.circle_button.pack(side=tk.LEFT)
        self.clear_button.pack(side=tk.LEFT)

        # Bind mouse events
        self.canvas.bind("<Button-1>", self.start_draw)
        self.canvas.bind("<B1-Motion>", self.draw_shape)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

    def create_rectangle(self):
        self.current_shape = "rectangle"

    def create_circle(self):
        self.current_shape = "circle"

    def start_draw(self, event):
        self.start_x = event.x
        self.start_y = event.y
        if self.current_shape == "rectangle":
            self.current_shape_item = self.canvas.create_rectangle(
                self.start_x, self.start_y, self.start_x, self.start_y, outline="black"
            )
        elif self.current_shape == "circle":
            self.current_shape_item = self.canvas.create_oval(
                self.start_x, self.start_y, self.start_x, self.start_y, outline="black"
            )

    def draw_shape(self, event):
        if self.current_shape_item:
            x, y = event.x, event.y
            self.canvas.coords(self.current_shape_item, self.start_x, self.start_y, x, y)

    def stop_draw(self, event):
        self.current_shape_item = None

    def clear_canvas(self):
        self.canvas.delete("all")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeEditorApp(root)
    root.mainloop()
