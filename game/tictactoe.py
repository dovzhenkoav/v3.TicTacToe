import tkinter
from tkinter import messagebox
from gameBrain import Brain
from aiBrain import AIBrain
from PIL import Image, ImageTk

YELLOW = "#f7f5dd"
RED = "#e7305b"
GREEN = "#9bdeac"
CROSS = r".\png\cross.png"
CIRCLE = r".\png\circle.png"
EMPTY_SPACE = r".\png\empty_space.png"
ICON = r".\png\icon.png"

def singleplayer(root):
    root.destroy()
    choice_win = tkinter.Tk()
    def decision_helper(decision, window=choice_win):
        global choice
        choice = decision
        window.destroy()
        start_game(brain_decision='singleplayer', turn=choice)

    choice_win.title("TicTacToe")
    choice_win.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file=ICON))
    choice_win.minsize(width=500, height=500)
    choice_win.maxsize(width=500, height=500)
    choice_win.config(padx=1, pady=1, bg=YELLOW)

    logo = tkinter.Label(text="Choose your\nsign", fg=GREEN, font=("Courier", 50), bg=YELLOW)
    logo.place(x=25, y=56)

    cross_img = tkinter.PhotoImage(file=CROSS)
    cross = tkinter.Label(choice_win, image=cross_img, bg=YELLOW, width=150, height=150)
    cross.bind('<Button-1>', lambda event: decision_helper('cross'))
    cross.place(x=80, y=230)

    circle_img = tkinter.PhotoImage(file=CIRCLE)
    circle = tkinter.Label(choice_win, image=circle_img, bg=YELLOW, width=150, height=150)
    circle.bind('<Button-1>', lambda event: decision_helper('circle'))
    circle.place(x=270, y=230)

    choice_win.mainloop()
    pass


def multiplayer(root):
    root.destroy()
    start_game(brain_decision='multiplayer')
    pass


def start_game(brain_decision, turn='cross'):
    global brain_dec
    brain_dec = brain_decision
    trn = turn

    brain = Brain()
    if brain_decision == 'multiplayer':
        brain = Brain()

        window = tkinter.Tk()
        window.title("TicTacToe")
        window.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file=ICON))
        window.minsize(width=500, height=500)
        window.maxsize(width=500, height=500)
        window.config(padx=4, pady=1, bg=YELLOW)

        bg = tkinter.PhotoImage(file=r".\png\board.png")
        my_label = tkinter.Label(window, image=bg, bg=YELLOW)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        def make_turn(event, cell, picture):
            if not brain.make_turn(event, cell, picture):
                if brain.turn == 'DRAW':
                    msg_box = messagebox.askquestion(title=f"It's {brain.turn}!", message=f"It's {brain.turn}!\nDo you want to play again?")
                else:
                    msg_box = messagebox.askquestion(title=f"{brain.turn} wins!", message=f"{brain.turn} wins!\nDo you want to play again?")
                if msg_box == 'yes':
                    window.destroy()
                    start_game(brain_decision)
                else:
                    window.destroy()

        lu_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        lu = tkinter.Label(window, image=lu_img, bg=YELLOW, width=150, height=150)
        lu.bind('<Button-1>', lambda event: make_turn(event, cell='lu', picture=lu))
        lu.grid(column=0, row=0, padx=7.5, pady=6)

        cu_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cu = tkinter.Label(window, image=cu_img, bg=YELLOW,width=150, height=150)
        cu.bind('<Button-1>', lambda event: make_turn(event, cell='cu', picture=cu))
        cu.grid(column=1, row=0, padx=3, pady=6)

        ru_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        ru = tkinter.Label(window, image=ru_img, bg=YELLOW,width=150, height=150)
        ru.bind('<Button-1>', lambda event: make_turn(event, cell='ru', picture=ru))
        ru.grid(column=2, row=0, padx=4.5, pady=6)

        lc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        lc = tkinter.Label(window, image=lc_img, bg=YELLOW,width=150, height=150)
        lc.bind('<Button-1>', lambda event: make_turn(event, cell='lc', picture=lc))
        lc.grid(column=0, row=1, padx=7.5, pady=6)

        cc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cc = tkinter.Label(window, image=cc_img, bg=YELLOW,width=150, height=150)
        cc.bind('<Button-1>', lambda event: make_turn(event, cell='cc', picture=cc))
        cc.grid(column=1, row=1, padx=3, pady=6)

        rc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        rc = tkinter.Label(window, image=rc_img, bg=YELLOW,width=150, height=150)
        rc.bind('<Button-1>', lambda event: make_turn(event, cell='rc', picture=rc))
        rc.grid(column=2, row=1, padx=4.5, pady=6)

        ld_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        ld = tkinter.Label(window, image=ld_img, bg=YELLOW,width=150, height=150)
        ld.bind('<Button-1>', lambda event: make_turn(event, cell='ld', picture=ld))
        ld.grid(column=0, row=2, padx=7.5, pady=8)

        cd_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cd = tkinter.Label(window, image=cd_img, bg=YELLOW,width=150, height=150)
        cd.bind('<Button-1>', lambda event: make_turn(event, cell='cd', picture=cd))
        cd.grid(column=1, row=2, padx=3, pady=8)

        rd_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        rd = tkinter.Label(window, image=rd_img, bg=YELLOW,width=150, height=150)
        rd.bind('<Button-1>', lambda event: make_turn(event, cell='rd', picture=rd))
        rd.grid(column=2, row=2, padx=4.5, pady=8)

        window.mainloop()

    elif brain_decision == 'singleplayer':
        brain = AIBrain(turn)

        window = tkinter.Tk()
        window.title("TicTacToe")
        window.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file=ICON))
        window.minsize(width=500, height=500)
        window.maxsize(width=500, height=500)
        window.config(padx=4, pady=1, bg=YELLOW)

        bg = tkinter.PhotoImage(file=r".\png\board.png")
        my_label = tkinter.Label(window, image=bg, bg=YELLOW)
        my_label.place(x=0, y=0, relwidth=1, relheight=1)

        def make_turn(event, cell, picture):
            if not brain.make_turn(event, cell, picture):
                if brain.turn == 'DRAW':
                    msg_box = messagebox.askquestion(title=f"It's {brain.turn}!",
                                                     message=f"It's {brain.turn}!\nDo you want to play again?")
                else:
                    msg_box = messagebox.askquestion(title=f"{brain.turn} wins!",
                                                     message=f"{brain.turn} wins!\nDo you want to play again?")
                if msg_box == 'yes':
                    window.destroy()
                    start_game(brain_dec, trn)
                    return None
                else:
                    window.destroy()
                    return None

            if not brain.bot_moves(lu, cu, ru, lc, cc, rc, ld, cd, rd):
                if brain.turn == 'DRAW':
                    msg_box = messagebox.askquestion(title=f"It's {brain.turn}!",
                                                     message=f"It's {brain.turn}!\nDo you want to play again?")
                else:
                    brain._ck()
                    msg_box = messagebox.askquestion(title=f"{brain.turn} wins!",
                                                     message=f"{brain.turn} wins!\nDo you want to play again?")
                if msg_box == 'yes':
                    window.destroy()
                    start_game(brain_dec, trn)
                else:
                    window.destroy()

        lu_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        lu = tkinter.Label(window, image=lu_img, bg=YELLOW, width=150, height=150)
        lu.bind('<Button-1>', lambda event: make_turn(event, cell='lu', picture=lu))
        lu.grid(column=0, row=0, padx=7.5, pady=6)

        cu_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cu = tkinter.Label(window, image=cu_img, bg=YELLOW, width=150, height=150)
        cu.bind('<Button-1>', lambda event: make_turn(event, cell='cu', picture=cu))
        cu.grid(column=1, row=0, padx=3, pady=6)

        ru_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        ru = tkinter.Label(window, image=ru_img, bg=YELLOW, width=150, height=150)
        ru.bind('<Button-1>', lambda event: make_turn(event, cell='ru', picture=ru))
        ru.grid(column=2, row=0, padx=4.5, pady=6)

        lc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        lc = tkinter.Label(window, image=lc_img, bg=YELLOW, width=150, height=150)
        lc.bind('<Button-1>', lambda event: make_turn(event, cell='lc', picture=lc))
        lc.grid(column=0, row=1, padx=7.5, pady=6)

        cc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cc = tkinter.Label(window, image=cc_img, bg=YELLOW, width=150, height=150)
        cc.bind('<Button-1>', lambda event: make_turn(event, cell='cc', picture=cc))
        cc.grid(column=1, row=1, padx=3, pady=6)

        rc_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        rc = tkinter.Label(window, image=rc_img, bg=YELLOW, width=150, height=150)
        rc.bind('<Button-1>', lambda event: make_turn(event, cell='rc', picture=rc))
        rc.grid(column=2, row=1, padx=4.5, pady=6)

        ld_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        ld = tkinter.Label(window, image=ld_img, bg=YELLOW, width=150, height=150)
        ld.bind('<Button-1>', lambda event: make_turn(event, cell='ld', picture=ld))
        ld.grid(column=0, row=2, padx=7.5, pady=8)

        cd_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        cd = tkinter.Label(window, image=cd_img, bg=YELLOW, width=150, height=150)
        cd.bind('<Button-1>', lambda event: make_turn(event, cell='cd', picture=cd))
        cd.grid(column=1, row=2, padx=3, pady=8)

        rd_img = tkinter.PhotoImage(file=EMPTY_SPACE)
        rd = tkinter.Label(window, image=rd_img, bg=YELLOW, width=150, height=150)
        rd.bind('<Button-1>', lambda event: make_turn(event, cell='rd', picture=rd))
        rd.grid(column=2, row=2, padx=4.5, pady=8)

        if turn == 'circle':
            brain.bot_make_turn(lu, cu, ru, lc, cc, rc, ld, cd, rd)

        window.mainloop()


root = tkinter.Tk()
root.title("TicTacToe")
root.tk.call('wm', 'iconphoto', root._w, tkinter.PhotoImage(file=ICON))
root.minsize(width=500, height=500)
root.maxsize(width=500, height=500)
root.config(padx=1,pady=1, bg=YELLOW)

logo = tkinter.Label(text= "Tic Tac Toe", fg=GREEN, font=("Courier", 50), bg=YELLOW)
logo.place(x=25, y=56)

button_singleplayer = tkinter.Button(text="Singleplayer", highlightthickness=0, height=2, width=10, command=lambda: singleplayer(root))
button_singleplayer.place(x=160, y=256)

button_multiplayer = tkinter.Button(text="Multiplayer", highlightthickness=0, height=2, width=10, command=lambda: multiplayer(root))
button_multiplayer.place(x=260, y=256)

root.mainloop()
