from tkinter import*
import random
import time

tk = Tk()
tk.title('Pong!')
tk.resizable(0, 0)
tk.wm_attributes('-topmost', 1)
canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
canvas.config(bg = "black")
canvas.pack()
tk.update()

canvas.create_line(250, 0, 250, 400, fill = "white")

class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
        self.canvas.move(self.id, 235, 200)
        starts = [-3, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = 500

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)

        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False
    
class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 150, 30, 250, fill = color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('a', self.turn_left)
        self.canvas.bind_all('d', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_left(self, evt):
        self.y = -3

    def  turn_right(self, evt):
        self.y = 3

paddle = Paddle(canvas, 'blue')
ball = Ball(canvas, "orange", paddle)

while 1:
    ball.draw()
    paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)

tk.mainloop()
