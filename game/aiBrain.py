import tkinter
from PIL import Image, ImageTk
from gameBrain import Brain
import random

CROSS = r".\png\cross.png"
CIRCLE = r".\png\circle.png"
EMPTY_SPACE = r".\png\empty_space.png"

class AIBrain(Brain):
    def __init__(self, turn):
        super().__init__()
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
        self.ai_turn = True

        self.turn = turn
        self.difficulty_list = ['rookie', 'average', 'advanced']
        self.difficulty = random.choice(self.difficulty_list)
        self.turn_skipped = False

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

    def bot_rookie_thinks(self):
        empty_space = [field for field in self.map if self.map[field] == 'empty']
        return random.choice(empty_space)

    def bot_average_thinks(self):
        if self.turn == 'cross':
            enemy_turn = 'circle'
        if self.turn == 'circle':
            enemy_turn = 'cross'
        my_map = self.map
        empty_space = [field for field in self.map if self.map[field] == 'empty']

        if my_map['lu'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cu'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == enemy_turn and my_map['cu'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'

        elif my_map['lc'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cc'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lc'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'

        elif my_map['ld'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'
        elif my_map['cd'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'
        elif my_map['ld'] == enemy_turn and my_map['cd'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == enemy_turn and my_map['lc'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['ld'] == enemy_turn and my_map['lu'] == enemy_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lu'] == enemy_turn and my_map['lc'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'

        elif my_map['cd'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cd'] == enemy_turn and my_map['cu'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cu'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'

        elif my_map['rd'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['rd'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'
        elif my_map['ru'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['cc'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['lu'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['ru'] == enemy_turn and my_map['ld'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['ru'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'
        else:
            my_choice = random.choice(empty_space)
        return my_choice

    def bot_advanced_thinks(self):
        my_turn = self.turn
        if self.turn == 'cross':
            enemy_turn = 'circle'
        if self.turn == 'circle':
            enemy_turn = 'cross'
        my_map = self.map
        empty_space = [field for field in self.map if self.map[field] == 'empty']

        if my_map['lu'] == my_turn and my_map['ru'] == my_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cu'] == my_turn and my_map['ru'] == my_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == my_turn and my_map['cu'] == my_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'

        elif my_map['lc'] == my_turn and my_map['rc'] == my_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cc'] == my_turn and my_map['rc'] == my_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lc'] == my_turn and my_map['cc'] == my_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'

        elif my_map['ld'] == my_turn and my_map['rd'] == my_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'
        elif my_map['cd'] == my_turn and my_map['rd'] == my_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'
        elif my_map['ld'] == my_turn and my_map['cd'] == my_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == my_turn and my_map['lc'] == my_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['ld'] == my_turn and my_map['lu'] == my_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lu'] == my_turn and my_map['lc'] == my_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'

        elif my_map['cd'] == my_turn and my_map['cc'] == my_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cd'] == my_turn and my_map['cu'] == my_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cu'] == my_turn and my_map['cc'] == my_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'

        elif my_map['rd'] == my_turn and my_map['rc'] == my_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['rd'] == my_turn and my_map['ru'] == my_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'
        elif my_map['ru'] == my_turn and my_map['rc'] == my_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['cc'] == my_turn and my_map['rd'] == my_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == my_turn and my_map['rd'] == my_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['lu'] == my_turn and my_map['cc'] == my_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == my_turn and my_map['cc'] == my_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['ru'] == my_turn and my_map['ld'] == my_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['ru'] == my_turn and my_map['cc'] == my_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'

        elif my_map['lu'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cu'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == enemy_turn and my_map['cu'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'

        elif my_map['lc'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cc'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lc'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'

        elif my_map['ld'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'
        elif my_map['cd'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'
        elif my_map['ld'] == enemy_turn and my_map['cd'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == enemy_turn and my_map['lc'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['ld'] == enemy_turn and my_map['lu'] == enemy_turn and my_map['lc'] == 'empty':
            my_choice = 'lc'
        elif my_map['lu'] == enemy_turn and my_map['lc'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'

        elif my_map['cd'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['cu'] == 'empty':
            my_choice = 'cu'
        elif my_map['cd'] == enemy_turn and my_map['cu'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['cu'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['cd'] == 'empty':
            my_choice = 'cd'

        elif my_map['rd'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['rd'] == enemy_turn and my_map['ru'] == enemy_turn and my_map['rc'] == 'empty':
            my_choice = 'rc'
        elif my_map['ru'] == enemy_turn and my_map['rc'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['cc'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['lu'] == 'empty':
            my_choice = 'lu'
        elif my_map['lu'] == enemy_turn and my_map['rd'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['lu'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['rd'] == 'empty':
            my_choice = 'rd'

        elif my_map['ld'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['ru'] == 'empty':
            my_choice = 'ru'
        elif my_map['ru'] == enemy_turn and my_map['ld'] == enemy_turn and my_map['cc'] == 'empty':
            my_choice = 'cc'
        elif my_map['ru'] == enemy_turn and my_map['cc'] == enemy_turn and my_map['ld'] == 'empty':
            my_choice = 'ld'

        elif len(empty_space) == 9:
            my_choice = 'cc'

        elif my_map['cc'] == enemy_turn and len(empty_space) == 8:
            my_choice = 'lu'
        elif my_map['cc'] == enemy_turn and my_map['lu'] == my_turn and my_map['rd'] == enemy_turn and len(empty_space) == 6:
            my_choice = 'ld'

        elif (my_map['lu'] == enemy_turn or my_map['ru'] == enemy_turn or my_map['ld'] == enemy_turn or my_map['rd'] == enemy_turn) and len(empty_space) == 8:
            my_choice = 'cc'
        elif (my_map['lu'] == enemy_turn and my_map['rd'] == enemy_turn) or (my_map['ru'] == enemy_turn and my_map['ld'] == enemy_turn) and my_map['cc'] == my_turn and len(empty_space) == 6:
            my_choice = 'lc'
        elif (my_map['cu'] == enemy_turn or my_map['cd'] == enemy_turn or my_map['lc'] == enemy_turn or my_map['rc'] == enemy_turn) and len(empty_space) == 8:
            my_choice = 'cc'

        else:
            my_choice = random.choice(empty_space)
        return my_choice

    def bot_make_turn(self, lu, cu, ru, lc, cc, rc, ld, cd, rd):
        self.__change_turn()
        map = {
            "lu": lu,
            "cu": cu,
            "ru": ru,

            "lc": lc,
            "cc": cc,
            "rc": rc,

            "ld": ld,
            "cd": cd,
            "rd": rd
        }

        if self.difficulty == 'rookie':
            bot_choice = self.bot_rookie_thinks()
        elif self.difficulty == 'average':
            bot_choice = self.bot_average_thinks()
        elif self.difficulty == 'advanced':
            bot_choice = self.bot_advanced_thinks()
        picture = map[bot_choice]
        image_path = self.__check_turn()
        cross_img = ImageTk.PhotoImage(Image.open(image_path))
        picture.config(image=cross_img)
        picture.image = cross_img
        self.map[bot_choice] = self.turn
        self.__change_turn()

    def _ck(self):
        self.__change_turn()

    def bot_moves(self, lu, cu, ru, lc, cc, rc, ld, cd, rd):
        if self.turn_skipped:
            return True
        self.__change_turn()
        self.bot_make_turn(lu, cu, ru, lc, cc, rc, ld, cd, rd)

        self.__change_turn()
        self.__check_victory()
        self.__change_turn()
        if self.game_is_on:
            return True
        else:
            return False
        return True

    def make_turn(self, event, cell, picture):
        image_path = self.__check_turn()
        if self.__check_space(cell):
            cross_img = ImageTk.PhotoImage(Image.open(image_path))
            picture.config(image=cross_img)
            picture.image = cross_img
            self.map[cell] = self.turn
            self.turn_skipped = False
            self.__check_victory()
            if self.game_is_on:
                self.__change_turn()
                return True
            else:
                return False
        self.turn_skipped = True
        return True














