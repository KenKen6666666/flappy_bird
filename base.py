import pygame as pg
from config import *
from helper import image_loader


class Base(pg.sprite.Sprite):
    """
    遊戲中最下方的地基

    Attributes:
        scroll (float): 表示地基的向右滑動量, 向右滑動為正, 向左滑動為負
    Methods:
        update(): 更新地基的狀態(位置)
        draw(screen): 將地基畫到視窗中
    """

    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = image_loader(BASE_IMG_PATH, (BASE_WIDTH, BASE_HEIGHT))
        self.rect = self.image.get_rect()
        self.rect.bottomleft = (0, SCREEN_HEIGHT)
        return

    @property
    def scroll(self):
        return self.rect.left

    @scroll.setter
    def scroll(self, value: float):
        self.rect.left = value

    def update(self):
        SCROLL_SPEED = 2
        # TODO0 讓底下綠色的bar動起來
        """
        hint:   透過在每次update時增加一點base圖片向左的滑動量(設定self.scroll), 可達成視覺上向左動的效果.
                因為base的圖片並非無限延伸, 在圖片要滑出畫面(self.scroll + BASE_WIDTH < SCREEN_WIDTH)時, 可以把base拉回原位(self.scroll = 0)做修正.
        """
        self.scroll -= SCROLL_SPEED
        if self.scroll + BASE_WIDTH < SCREEN_WIDTH:
            self.scroll = 0