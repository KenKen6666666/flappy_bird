from typing import Tuple, Literal
import pygame as pg
from config import *
from helper import image_loader

import math

class Bird(pg.sprite.Sprite):
    """
    遊戲中的鳥(玩家)物件

    Attributes:
        y (float): 表示鳥頭頂(圖片上方)的垂直位置
        rotation_degree (float): 鳥的旋轉角度(degree), 逆時針為正
        image_index (0, 1, 2, 3): 鳥的圖片狀態(0-翅膀朝下, 1-翅膀置中, 2-翅膀朝上, 3-翅膀置中)
    Methods:
        move(): 處理鳥和移動(y座標)相關的更新
        update_image(): 處理鳥和圖片(圖片狀態, 旋轉角度)相關的更新
        update(): 處理鳥的所有更新
        draw(screen): 將鳥畫到視窗中
    """

    images = [image_loader(path, (BIRD_WIDTH, BIRD_HEIGHT)) for path in BIRD_IMG_PATHS]

    def __init__(self, position: Tuple[float, float]):
        """
        初始化函式

        Args:
            position (Tuple[int, int]): 初始位置 (x, y), x 為鳥(圖片)左方的水平位置, y 為鳥(圖片)中心的垂直位置
        """
        pg.sprite.Sprite.__init__(self)
        self.image_index_ = 1
        self.image = Bird.images[self.image_index_]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.rect.left = position[0]
        self.rotation_degree_ = 0

        self.counter = 0
        self.vel = 0
        self.clicked = False
        self.JUMP_COOLDOWN = 250
        self.last_jump_time = 0
        self.wing_index = 0
        self.wing_angle = 0
        self.game_over = False 


        self.gameover_image = image_loader(GAMEOVER_IMG_PATH, (int(GAME_OVER_WIDTH), int(GAME_OVER_HEIGHT))) 
        self.gameover_rect = self.gameover_image.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)) 
        self.gameover_rect.y -= 50 

            
        return

    def get_input(self) -> bool:  # 回傳滑鼠是否按下(True: 按下/False: 沒有按下)
        if pg.mouse.get_pressed()[0]:
            return True
        return False

    @property
    def y(self):
        return self.rect.top

    @y.setter
    def y(self, value: float):
        self.rect.top = value

    @property
    def rotation_degree(self):
        return self.rotation_degree_

    @rotation_degree.setter
    def rotation_degree(self, value: float):
        self.rotation_degree_ = value
        self.image = pg.transform.rotate(self.image, self.rotation_degree_)

    @property
    def image_index(self):
        return self.image_index_

    @image_index.setter
    def image_index(self, value: Literal[0, 1, 2, 3]):
        self.image_index_ = value
        self.image = Bird.images[self.image_index_]

    # 處理鳥的移動
    def move(self):
        # TODO1 讓鳥鳥動起來
        self.vel += 0.65
        if self.vel > 8:
            self.vel = 8

        if self.y >= SCREEN_HEIGHT - BASE_HEIGHT-25:
            self.game_over = True
        else:
            # 自由落體
            self.y += int(self.vel)

        if self.game_over:
            self.screen.blit(self.background_image, (0, 0))
            self.screen.blit(self.gameover_image, self.gameover_rect) 
            pg.display.update()
            return 
        
        if self.y > 0 and pg.time.get_ticks() - self.last_jump_time >= self.JUMP_COOLDOWN:
            if self.get_input(): # 當滑鼠點擊時條件為True, 反之為False
                # TODO2 在接受到 input 時讓鳥有向上的抬升力
                self.vel = -8
                self.y -= 2.1
                self.last_jump_time = pg.time.get_ticks()
                self.rotation_degree = -30
            else:
                self.rotation_degree = 0

 
 
    # 處理鳥的圖片設定(實現動畫)
    def update_image(self):
        # TODO4 讓鳥鳥更生動(增加動畫)
        self.counter += 1
        flap_cooldown = 7

        if self.counter >= flap_cooldown:
            self.counter = 0 
            self.image_index = (self.image_index + 1) % len(Bird.images)

        self.image = pg.transform.rotate(Bird.images[self.image_index], self.vel * -3)


    def update(self):
        self.update_image()
        self.move()



