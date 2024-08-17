from typing import Tuple, Optional, Literal
import pygame
from config import NUMBER_IMG_PATHS, NUMBER_WIDTH, NUMBER_HEIGHT
from helper import image_loader


class Number_(pygame.sprite.Sprite):
    imgs = [
        image_loader(path, (NUMBER_WIDTH, NUMBER_HEIGHT)) for path in NUMBER_IMG_PATHS
    ]

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, value: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.__number = value
        self.image = Number_.imgs[self.__number]

    def __init__(
        self,
        position: Tuple[float, float],
        init_value: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ):
        pygame.sprite.Sprite.__init__(self)
        self.number = init_value
        self.rect = self.image.get_rect()
        self.rect.topleft = position

    def update(self, new_value: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] = -1):
        if not (new_value == -1 or new_value == self.number):
            self.number = new_value


class Number:
    """
    單一位數的數字物件

    Attributes:
        number (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): 此數字物件的數字
    Methods:
        update(new_value): 更新此數字物件的數字成new_value
        draw(screen): 將數字畫到視窗中
    """

    def __init__(
        self,
        position: Tuple[int, int],
        init_value: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
    ):
        """
        初始化函式

        Args:
            position (Tuple[int, int]): 初始位置 (x, y), x 為數字(圖片)左方的水平位置, y 為數字(圖片)上方的垂直位置
            init_value (0, 1, 2, 3, 4, 5, 6, 7, 8, 9): 初始數字
        """
        self.__number = Number_(position, init_value)
        self.number_group = pygame.sprite.GroupSingle(self.__number)

    @property
    def number(self):
        return self.__number.number

    @number.setter
    def number(self, value: Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        self.__number.number = value

    def update(self, new_value: Optional[Literal[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]] = -1):
        """
        更新數字函式

        Args:
            new_value (Optional)(0, 1, 2, 3, 4, 5, 6, 7, 8, 9): 欲更新的數字, 留空則不更新
        """
        self.__number.update(new_value)

    def draw(self, screen: pygame.surface):
        self.number_group.draw(screen)
