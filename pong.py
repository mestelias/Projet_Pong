from tkinter import *
from tkinter import messagebox
import random
import time

def rules():
    window.withdraw()

    def backtomenu():
        window.deiconify()
        windowRules.withdraw()

    #Création de la fenêtre des règles
    windowRules = Tk()
    windowRules.title(title)
    windowRules.geometry("600x600")
    windowRules['bg'] = background_color

    TitleRules = Label(windowRules, text = "LES RÈGLES", background = background_color, font = ("Georgia", 26), fg = "green")
    TitleRules.pack()

    TextRules = Label(windowRules, fg = "white", text = "Les règles du jeu sont simple: \n Jouez en 1vs1 en déplaçant votre paddle de haut en bas \n pour empêcher la balle de toucher votre mur \n et ainsi essayer de toucher le mur adverse. \n Chaque mur touché donne 1 point. \n Le premier arrivé a 10 gagne le match.\n\n J1: Z=Haut & S=Bas \n J2: Utilisez les flèches Haut & Bas", background = background_color, font = ("Helvetica", 16))
    TextRules.pack()
    TextRules2 = Label(windowRules, fg = "red", text = "Bonne chance !", background = background_color, font = ("Helvetica", 16))
    TextRules2.pack()

    ButtonReturn = Button(windowRules, text = "Retour", command = backtomenu, width = 11, height = 1, bg = "orange", fg = "white", font = ("Impact", 12))
    ButtonReturn.place(x = 380, y = 450)
    
def play():
    window.withdraw()
    global counter
    global counter1
    counter = 0
    counter1 = 0

    tk = Tk()
    tk.focus_force()
    tk.title('Pong')
    tk.resizable(0, 0)
    tk.wm_attributes('-topmost', 1)
    canvas = Canvas(tk, width = 500, height = 400, bd = 0, highlightthickness = 0)
    canvas.config(bg = "black")
    canvas.pack()
    tk.update()
    tk.deiconify()

    canvas.create_line(250, 0, 250, 400, fill = "white")

    class Ball:
        def __init__(self, canvas, color, paddle, paddle1):
            self.canvas = canvas
            self.paddle = paddle
            self.paddle1 = paddle1
            self.id = canvas.create_oval(10, 10, 25, 25, fill = color)
            self.canvas.move(self.id, 235, 200)
            starts = [-3, 3]
            random.shuffle(starts)
            self.x = starts[0]
            self.y = -3
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()

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

            if self.hit_paddle(pos) == True:
                self.x = 3
            if self.hit_paddle1(pos) == True:
                self.x = -3

        def score(self, val):
            global counter
            global counter1

            if val == False:
                a = self.canvas.create_text(125, 40, text = counter, font = ("Arial", 60), fill = "white")
                canvas.itemconfig(a, fill = "black")
                counter += 1
                a = self.canvas.create_text(125, 40, text = counter, font = ("Arial", 60), fill = "white")

            if val == True:
                a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial", 60), fill = "white")
                canvas.itemconfig(a, fill = "black")
                counter1 += 1
                a = self.canvas.create_text(375, 40, text = counter1, font = ("Arial", 60), fill = "white")      

        def hit_paddle(self, pos):
            paddle_pos = self.canvas.coords(self.paddle.id)
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                    return True
                return False
        def hit_paddle1(self, pos):
            paddle_pos = self.canvas.coords(self.paddle1.id)
            if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
                if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                    return True
                return False

    class Paddle:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(0, 150, 30, 250, fill = color)
            self.y = 0
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('z', self.turn_left)
            self.canvas.bind_all('s', self.turn_right)

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

    class Paddle1:
        def __init__(self, canvas, color):
            self.canvas = canvas
            self.id = canvas.create_rectangle(470, 150, 500, 250, fill = color)
            self.y = 0
            self.canvas_height = self.canvas.winfo_height()
            self.canvas_width = self.canvas.winfo_width()
            self.canvas.bind_all('<KeyPress-Down>', self.turn_left)
            self.canvas.bind_all('<KeyPress-Up>', self.turn_right)

        def draw(self):
            self.canvas.move(self.id, 0, self.y)
            pos = self.canvas.coords(self.id)
            if pos[1] <= 0:
                self.y = 0
            if pos[3] >= 400:
                self.y = 0

        def turn_left(self, evt):
            self.y = 3

        def  turn_right(self, evt):
            self.y = -3

    paddle = Paddle(canvas, 'blue')
    paddle1 = Paddle1(canvas, 'red')
    ball = Ball(canvas, "orange", paddle, paddle1)

    while 1:
        ball.draw()
        paddle.draw()
        paddle1.draw()
        if counter == 10:
            ball.x = 0
            ball.y = 0
            paddle.y = 0
            paddle1.y = 0
            canvas.create_text(250, 200, text = "Félicitations Joueur1 ! Tu as gagné !", font = 32, fill = "red")
            canvas.create_text(250, 215, text = "Score:" + str(counter) + " - " + str(counter1), font = 32, fill = "red")
            def backtomenu():
                tk.withdraw()
                window.update()
                window.deiconify()
            ButtonReturn = Button(tk, text = "Retour", command = backtomenu, width = 11, height = 1, bg = "orange", fg = "white", font = ("Impact", 12))
            ButtonReturn.pack()
        if counter1 == 10:
            ball.x = 0
            ball.y = 0
            paddle.y = 0
            paddle1.y = 0
            canvas.create_text(250, 200, text = "Félicitations Joueur2 ! Tu as gagné !", font = 32, fill = "red")
            canvas.create_text(250, 215, text = "Score:" + str(counter) + " - " + str(counter1), font = 32, fill = "red") 
            def backtomenu():
                tk.withdraw()
                window.update()
                window.deiconify()
            ButtonReturn = Button(tk, text = "Retour", command = backtomenu, width = 11, height = 1, bg = "orange", fg = "white", font = ("Impact", 12))
            ButtonReturn.pack()
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

        if counter == 10 or counter1 == 10:
            time.sleep(2.5)
    tk.mainloop()
title = "Pong" #Titre du jeu

#Couleurs
background_color = "#2a2a2a"
green = "#016d2b"


window = Tk()
window.title(title)
window.geometry("600x600")
window['bg'] = background_color
filename = PhotoImage(file = "pop.png")
bg_label = Label(window, image = filename)
bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)

TextMore = Label(window, text = "Pong", background = 'black', font = ("Georgia", 26), fg = "white")
TextMore.pack()

ButtonPlay = Button(window, text = "Jouer", command = play, width = 28, height = 1, bg = "orange", fg = "white", font = ("Impact", 24))
ButtonPlay.pack(pady = 110)

ButtonRules = Button(window, text = "Règles", command = rules, width = 28, height = 1, bg = "orange", fg = "white", font = ("Impact", 24))
ButtonRules.pack(pady = 10)

ButtonQuit = Button(window, text = "Quitter", command = quit, width = 28, height = 1, bg = "orange", fg = "white", font = ("Impact", 24))
ButtonQuit.pack(pady = 10, side = BOTTOM)
