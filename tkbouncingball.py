#Creating a bouncing ball animation with Python and Tkinter
import tkinter as tk

# Constants for the canvas size
CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300

# Ball properties
BALL_RADIUS = 15
BALL_COLOR = "yellow"
BALL_SPEED_X = 2
BALL_SPEED_Y = 2

class BouncingBallApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bouncing Ball")

        self.canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="white")
        self.canvas.pack()

        # Create the bouncing ball
        self.ball = self.canvas.create_oval(
            CANVAS_WIDTH // 2 - BALL_RADIUS,
            CANVAS_HEIGHT // 2 - BALL_RADIUS,
            CANVAS_WIDTH // 2 + BALL_RADIUS,
            CANVAS_HEIGHT // 2 + BALL_RADIUS,
            fill=BALL_COLOR
        )

        # Initial ball position and direction
        self.ball_x, self.ball_y = CANVAS_WIDTH // 2, CANVAS_HEIGHT // 2
        self.speed_x, self.speed_y = BALL_SPEED_X, BALL_SPEED_Y

        # Start the animation
        self.animate()

    def animate(self):
        # Move the ball
        self.ball_x += self.speed_x
        self.ball_y += self.speed_y

        # Check for collisions with the canvas boundaries
        if self.ball_x + BALL_RADIUS >= CANVAS_WIDTH or self.ball_x - BALL_RADIUS <= 0:
            self.speed_x *= -1
        if self.ball_y + BALL_RADIUS >= CANVAS_HEIGHT or self.ball_y - BALL_RADIUS <= 0:
            self.speed_y *= -1

        # Update the ball's position
        self.canvas.move(self.ball, self.speed_x, self.speed_y)

        # Schedule the next animation frame
        self.root.after(10, self.animate)

if __name__ == "__main__":
    root = tk.Tk()
    app = BouncingBallApp(root)
    root.mainloop()
