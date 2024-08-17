from typing import Tuple
import pygame as pg


def image_loader(path: str, size: Tuple[float, float]) -> pg.Surface:
    """
    載入圖片函式

    Args:
        path (str): 欲載入圖片之路徑
        size (Tuple[float, float]): 圖片之寬, 高
    Returns:
        pg.Surface: 載入好的圖片物件
    """
    image = pg.image.load(path)
    scaled_image = pg.transform.scale(image, size)
    return scaled_image


class Node:
    def __init__(self, data, nxt: "Node"):
        self.data = data
        self.nxt = nxt


class MyList:
    """
    酷酷的List

    Attributes:
        head (Node): 已經產生的水管對數
        tail (Node): 所有在視窗中的水管對
    Methods:
        push_back(data): 新增一筆data到MyList最後面
        peek(): 查看最前面的一筆data
        pop_top(): 將最前面的一筆data移出MyList
    """

    def __init__(self):
        self.head = self.tail = None

    def push_back(self, data):
        if self.head == None:
            self.head = self.tail = Node(data, None)
        else:
            self.tail.nxt = Node(data, None)
            self.tail = self.tail.nxt

    def peek(self):
        if self.head == None:
            return None
        return self.head.data

    def pop_top(self):
        if self.head == None:
            return None
        elif self.head == self.tail:
            node = self.head
            self.head = self.tail = None
            return node.data
        else:
            node = self.head
            self.head = node.nxt
            return node.data
