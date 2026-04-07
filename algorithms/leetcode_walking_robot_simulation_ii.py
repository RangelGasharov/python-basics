from typing import List


class Robot:
    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.direction = "East"
        self.width = width
        self.height = height

    def step(self, num: int) -> None:
        perimeter = 2 * (self.width - 1) + 2 * (self.height - 1)
        num %= perimeter
        if num == 0:
            num = perimeter

        while num > 0:
            if self.direction == "East":
                max_x = min(self.x + num, self.width - 1)
                rem = num - (max_x - self.x)
                num = rem
                if rem == 0:
                    self.x = max_x
                else:
                    self.x = max_x
                    self.direction = "North"
            elif self.direction == "West":
                min_x = max(self.x - num, 0)
                rem = num - (self.x - min_x)
                num = rem
                if rem == 0:
                    self.x = min_x
                else:
                    self.x = min_x
                    self.direction = "South"
            elif self.direction == "North":
                max_y = min(self.y + num, self.height - 1)
                rem = num - (max_y - self.y)
                num = rem
                if rem == 0:
                    self.y = max_y
                else:
                    self.y = max_y
                    self.direction = "West"
            elif self.direction == "South":
                min_y = max(self.y - num, 0)
                rem = num - (self.y - min_y)
                num = rem
                if rem == 0:
                    self.y = min_y
                else:
                    self.y = min_y
                    self.direction = "East"

    def getPos(self) -> List[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        return self.direction
