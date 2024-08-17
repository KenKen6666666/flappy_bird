import random
import pygame as pg
from config import *
from helper import image_loader, MyList
from scoreboard import Scoreboard

# a single pipe
class Pipe(pg.sprite.Sprite):
    """
    遊戲中的單一根水管物件
    """

    img = image_loader(PIPE_IMG_PATH, (PIPE_WIDTH, PIPE_HEIGHT))
    flipped_img = pg.transform.flip(img, False, True)

    def __init__(self, position: tuple[float, float], direction: str):
        """
        初始化函式
        """
        pg.sprite.Sprite.__init__(self)
        self.direction = direction
        if self.direction == "DOWN":
            self.image = Pipe.flipped_img
            self.rect = self.image.get_rect()
            self.rect.bottomleft = position
        else:
            self.image = Pipe.img
            self.rect = self.image.get_rect()
            self.rect.topleft = position

    @property
    def x(self):
        return self.rect.left

    @x.setter
    def x(self, value):
        self.rect.left = value

    @property
    def y(self):
        if self.direction == "UP":
            return self.rect.top
        else:
            return self.rect.bottom

    @y.setter
    def y(self, value):
        if self.direction == "UP":
            self.rect.top = value
        else:
            self.rect.bottom = value

    def update(self):
        self.x -= BASE_SCROLLING_SPEED
        if self.x + PIPE_WIDTH < 0:
            self.kill()


# an upper pipe and a lower pipe
class PipePair:
    """
    遊戲中的一對(上下兩根)水管物件
    """

    def __init__(self):
        """
        初始化函式
        """
        min_gap = 125  # Minimum gap between pipes
        max_gap = 200  # Maximum gap between pipes
        center = HEIGHT_LIMIT / 2

        # Generate a random gap for each new pipe pair
        pipe_gap = random.randint(min_gap, max_gap)  # Varying gap between pipes
        pipe_gap_variation = random.randint(-50, 50)  # Variation in gap position

        pipe_top = Pipe((SCREEN_WIDTH, center - (pipe_gap / 2) + pipe_gap_variation), "DOWN")
        pipe_btm = Pipe((SCREEN_WIDTH, center + (pipe_gap / 2) + pipe_gap_variation), "UP")

        self.pipes = pg.sprite.Group()
        self.pipes.add(pipe_btm), self.pipes.add(pipe_top)

        # Track the start time of the pipe pair
        self.start_time = pg.time.get_ticks()

        # Randomly choose the direction of movement and speed
        self.move_direction = random.choice([-1, 1])  # Randomly move up or down
        self.move_speed = random.uniform(0.5, 1.5)  # Random speed between 0.5 and 1.5 pixels per frame

        # Track if vertical movement should stop
        self.stopped = False

    @property
    def bottom_pipe(self):
        return self.pipes.sprites()[0]

    @property
    def top_pipe(self):
        return self.pipes.sprites()[1]

    @property
    def x(self):
        return self.bottom_pipe.x

    def update(self) -> bool:
        self.pipes.update()

    def draw(self, screen: pg.surface):
        self.pipes.draw(screen)

    def is_alive(self) -> bool:
        if len(self.pipes) == 0:
            return False
        return True

    def move_vertical(self):
        if not self.stopped:
            self.bottom_pipe.y += self.move_direction * self.move_speed
            self.top_pipe.y += self.move_direction * self.move_speed

            if self.bottom_pipe.y < 0 or self.top_pipe.y > SCREEN_HEIGHT:
                self.move_direction *= -1

    def stop_vertical(self):
        self.stopped = True


# all pipes
class Pipes:
    """
    遊戲中控制所有水管的物件
    """

    def __init__(self):
        self.pipes_counter = 0
        self.pipe_pairs = MyList()
        self.last_pipe_added_time = 0
        self.initial_pipe_count = 2  # 初始水管數量
        self.pipe_add_interval = 2000  # 初始水管添加間隔，單位為毫秒
        self.pipe_add_interval_step = 100  # 每次增加水管間隔的步長，單位為毫秒
        self.pipe_add_count = 1  # 每次增加的水管數量
        self.scoreboard = Scoreboard()


    @property
    def pipes(self):
        re = pg.sprite.Group()
        cursor = self.pipe_pairs.head
        while cursor != None:
            sprites = cursor.data.pipes.sprites()
            re.add(sprites[0]), re.add(sprites[1])
            cursor = cursor.nxt
        return re

    def add_pipes(self, count):
        for _ in range(count):
            self.pipes_counter += 1
            self.pipe_pairs.push_back(PipePair())
            self.last_pipe_added_time = pg.time.get_ticks()

    def update(self):
        cursor = self.pipe_pairs.head
        while cursor != None:
            cursor.data.update()
            cursor = cursor.nxt

        cursor = self.pipe_pairs.peek()
        while cursor != None and not cursor.is_alive():
            self.pipe_pairs.pop_top()
            cursor = self.pipe_pairs.peek()

        current_time = pg.time.get_ticks()
        if current_time - self.last_pipe_added_time >= self.pipe_add_interval:
            self.add_pipes(self.pipe_add_count)
            self.pipe_add_interval += self.pipe_add_interval_step

        cursor = self.pipe_pairs.head
        while cursor != None:
            if not cursor.data.stopped:
                cursor.data.move_vertical()
                if current_time - cursor.data.start_time >= 1500:
                    cursor.data.stop_vertical()
            cursor = cursor.nxt

    def draw(self, screen: pg.surface):
        cursor = self.pipe_pairs.head
        while cursor != None:
            cursor.data.draw(screen)
            cursor = cursor.nxt

    def passed_pipe(self, bird):
        """
        檢查鳥是否通過了水管

        Args:
            bird (Bird): 鳥物件

        Returns:
            bool: 如果鳥通過了水管，返回True；否則返回False。
        """
        passed = False
        for pipe in self.pipes:
            if pipe.rect.right < bird.rect.left and not pipe.passed:
                pipe.passed = True
                passed = True
                self.score += 1
        return passed
