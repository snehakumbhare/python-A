#Building a drawing program with Python and Tkinter
import tkinter as tk

class DrawingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing Program")

        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack()

        self.rectangle_button = tk.Button(root, text="Draw Rectangle", command=self.draw_rectangle)
        self.rectangle_button.pack()

        self.rectangles = []

        self.canvas.bind("<ButtonPress-1>", self.start_draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw)

        self.drawing = False
        self.start_x, self.start_y = None, None

    def start_draw(self, event):
        self.drawing = True
        self.start_x, self.start_y = event.x, event.y

    def stop_draw(self, event):
        if self.drawing:
            end_x, end_y = event.x, event.y
            rectangle = self.canvas.create_rectangle(
                self.start_x, self.start_y, end_x, end_y, outline="black", width=2
            )
            self.rectangles.append(rectangle)
            self.drawing = False

    def draw_rectangle(self):
        self.canvas.bind("<ButtonPress-1>", self.start_draw_rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.stop_draw_rectangle)

    def start_draw_rectangle(self, event):
        self.drawing = True
        self.start_x, self.start_y = event.x, event.y

    def stop_draw_rectangle(self, event):
        if self.drawing:
            end_x, end_y = event.x, event.y
            rectangle = self.canvas.create_rectangle(
                self.start_x, self.start_y, end_x, end_y, outline="black", width=2
            )
            self.rectangles.append(rectangle)
            self.drawing = False

if __name__ == "__main__":
    root = tk.Tk()
    app = DrawingApp(root)
    root.mainloop()
