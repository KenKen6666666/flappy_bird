#scoreboard
import pygame as pg
from number import Number
from config import *


# TODO6 完成記分板物件
"""
記分板物件需至少支援三個方法
1. __init__(): constructor, 用來建構一個記分板物件實體
2. update(): 用來作為遊戲迴圈中每次更新呼叫的更新函式, 更新記分板物件中的邏輯部分(分數部分)
3. draw(screen): 遊戲迴圈更新後將記分板畫到視窗中的函式
"""

"""
hint: 可以利用實作好的Number物件幫忙
"""

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.score_number = Number((SCREEN_WIDTH // 2.2, SCREEN_HEIGHT / 10), 0)

    def update(self, passed_pipes):
        """
        根據通過的水管數量更新分數

        Args:
            passed_pipes (int): 通過的水管數量
        """
        self.score = passed_pipes
        self.score_number.update(self.score)

    def draw(self, screen: pg.surface):
        self.score_number.draw(screen)