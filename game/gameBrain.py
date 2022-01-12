import tkinter
from PIL import Image, ImageTk

CROSS = r".\png\cross.png"
CIRCLE = r".\png\circle.png"
EMPTY_SPACE = r".\png\empty_space.png"

class Brain:
    def __init__(self):
        self.map = {
            "lu": "empty",
            "cu": "empty",
            "ru": "empty",

            "lc": "empty",
            "cc": "empty",
            "rc": "empty",

            "ld": "empty",
            "cd": "empty",
            "rd": "empty",
        }
        self.turn = 'cross'
        self.game_is_on = True
        self.draw = False
        self.ai = False

    def __check_space(self, cell):
        if self.map[cell] == "empty":
            return True
        else:
            return False

    def __check_turn(self):
        if self.turn == 'cross':
            return r".\png\cross.png"
        elif self.turn == 'circle':
            return r".\png\circle.png"

    def __change_turn(self):
        if self.turn == 'cross':
            self.turn = 'circle'
        elif self.turn == 'circle':
            self.turn = 'cross'

    def __check_victory(self):
        if self.map["lu"] == self.map["cu"] == self.map["ru"] == self.turn:
            self.game_is_on = False
        elif self.map["lc"] == self.map["cc"] == self.map["rc"] == self.turn:
            self.game_is_on = False
        elif self.map["ld"] == self.map["cd"] == self.map["rd"] == self.turn:
            self.game_is_on = False

        elif self.map["lu"] == self.map["lc"] == self.map["ld"] == self.turn:
            self.game_is_on = False
        elif self.map["cu"] == self.map["cc"] == self.map["cd"] == self.turn:
            self.game_is_on = False
        elif self.map["ru"] == self.map["rc"] == self.map["rd"] == self.turn:
            self.game_is_on = False

        elif self.map["lu"] == self.map["cc"] == self.map["rd"] == self.turn:
            self.game_is_on = False
        elif self.map["ld"] == self.map["cc"] == self.map["ru"] == self.turn:
            self.game_is_on = False

        else:
            empty_pos = 0
            for position in self.map:
                if self.map[position] == 'empty':
                    empty_pos +=1
            if empty_pos == 0:
                self.game_is_on = False
                self.turn = 'DRAW'

    def make_turn(self, event, cell, picture):
        image_path = self.__check_turn()
        if self.__check_space(cell):
            cross_img = ImageTk.PhotoImage(Image.open(image_path))
            picture.config(image=cross_img)
            picture.image = cross_img
            self.map[cell] = self.turn
            self.__check_victory()
            if self.game_is_on:
                self.__change_turn()
                return True
            else:
                return False
        return True





