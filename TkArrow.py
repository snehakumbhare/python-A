#Python Tkinter arrow Key game - Character movement example

import tkinter as tk

# Constants for character size and movement step
CHARACTER_SIZE = 20
MOVEMENT_STEP = 10

class CharacterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Character Game")

        self.canvas = tk.Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack()

        # Create the character as a rectangle
        self.character = self.canvas.create_rectangle(
            190, 190, 210, 210, fill="blue"
        )

        # Bind arrow key events to movement functions
        self.canvas.bind("<Left>", self.move_left)
        self.canvas.bind("<Right>", self.move_right)
        self.canvas.bind("<Up>", self.move_up)
        self.canvas.bind("<Down>", self.move_down)

        # Add focus to the canvas so that it can receive keyboard events
        self.canvas.focus_set()

    def move_left(self, event):
        self.canvas.move(self.character, -MOVEMENT_STEP, 0)

    def move_right(self, event):
        self.canvas.move(self.character, MOVEMENT_STEP, 0)

    def move_up(self, event):
        self.canvas.move(self.character, 0, -MOVEMENT_STEP)

    def move_down(self, event):
        self.canvas.move(self.character, 0, MOVEMENT_STEP)

if __name__ == "__main__":
    root = tk.Tk()
    game = CharacterGame(root)
    root.mainloop()
