import pygame as pg
from config import *
from helper import image_loader

from base import Base
from bird import Bird
from pipe import Pipes
from scoreboard import Scoreboard


class Game:
    """
    遊戲控制物件

    Attributes:
        screen (pg.Surface): 視窗物件
        background_image (pg.Surface): 背景圖片物件
    Methods:
        run(): 開始遊戲(進入遊戲迴圈)
    """

    def __init__(self, surface: pg.Surface):
        """
        初始化函式

        Args:
            surface (pg.Surface): 視窗物件
        """
        self.screen = surface
        self.background_image = image_loader(BACKGROUND_IMG_PATH, (int(SCREEN_WIDTH), int(SCREEN_HEIGHT)))
        self.gameover_image = image_loader(GAMEOVER_IMG_PATH, (int(GAME_OVER_WIDTH), int(GAME_OVER_HEIGHT)))  # 加入 gameover 圖片
        self.gameover_rect = self.gameover_image.get_rect(center=self.screen.get_rect().center)  # 在屏幕中心定位 gameover 圖片
        self.gameover_rect.y -= 50  # 將 gameover 圖片上移一點，使其居中顯示

    # TODO7 讓遊戲流程更豐富
    def run(self):
        clock = pg.time.Clock()
        running = True
        game_started = False  # 標記遊戲是否已經開始
        game_over = False  # 標記遊戲是否已結束
        base = pg.sprite.GroupSingle(Base())
        bird = pg.sprite.GroupSingle(Bird((SCREEN_WIDTH / 10, HEIGHT_LIMIT / 2)))
        pipes = Pipes()
        scoreboard = Scoreboard()

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                elif event.type == pg.MOUSEBUTTONDOWN and not game_started and not game_over:
                    game_started = True

            if game_started and not game_over:
                clock.tick(FPS)

                base.update()
                bird.update()
                pipes.update()

                collisions = pg.sprite.groupcollide(bird, pipes.pipes, False, False)
                if collisions:
                    for bird_instance, collided_pipes in collisions.items():
                        for pipe in collided_pipes:
                            if pipe.direction == "UP" or pipe.direction == "DOWN":
                                game_over = True  # 碰撞到水管，遊戲結束

                self.screen.blit(self.background_image, (0, 0))
                bird.draw(self.screen)
                pipes.draw(self.screen)
                base.draw(self.screen)
                scoreboard.draw(self.screen)

                pg.display.update()

            elif not game_over:
                # 如果遊戲還沒開始，只處理滑鼠點擊事件並顯示開始畫面
                self.screen.blit(self.background_image, (0, 0))
                font = pg.font.Font(None, 36)
                text = font.render("Click to Start", True, (255, 255, 255))
                text_rect = text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
                self.screen.blit(text, text_rect)
                pg.display.update()
            else:
                # 顯示 game over 畫面
                self.screen.blit(self.background_image, (0, 0))
                self.screen.blit(self.gameover_image, self.gameover_rect)
                pg.display.update()

                # 等待按鍵重新開始
                while game_over:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            pg.quit()
                        elif event.type == pg.KEYDOWN:
                            # 重新啟動遊戲
                                base = pg.sprite.GroupSingle(Base())
                                bird = pg.sprite.GroupSingle(Bird((SCREEN_WIDTH / 10, HEIGHT_LIMIT / 2)))
                                pipes = Pipes()
                                
                                
