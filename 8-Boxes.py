import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def CalculateDistance(self, p2):
        delta_x = abs(self.x - p2.x)
        delta_y = abs(self.y - p2.y)
        if delta_x == 0:
            return delta_y
        else:
            return delta_x

class Box:
    def __init__(self, upper_left, upper_right, bottom_left, bottom_right):
        self.upper_left = upper_left
        self.upper_rigt = upper_right
        self.bottom_left = bottom_left
        self.bottom_rigt = bottom_right
        self.width = upper_left.CalculateDistance(upper_right)
        self.height = upper_left.CalculateDistance(bottom_left)

    def CalculatePerimeter(self):
        return int(2 * self.width + 2 * self.height)

    def CalculateArea(self):
        return int(self.width * self.height)


box_list = []

data = input()

while data != "end":
    temp_list = data.split(" | ")

    up_left_list = list(map(int,temp_list[0].split(":")))
    upper_left = Point(up_left_list[0], up_left_list[1])

    up_right_list = list(map(int,temp_list[1].split(":")))
    upper_right = Point(up_right_list[0], up_right_list[1])

    bot_left_list = list(map(int,temp_list[2].split(":")))
    bottom_left = Point(bot_left_list[0], bot_left_list[1])

    bot_right_list = list(map(int,temp_list[3].split(":")))
    bottom_right = Point(bot_right_list[0], bot_right_list[1])

    box_list.append(Box(upper_left, upper_right, bottom_left, bottom_right))
    data = input()


for box in box_list:
    print(f"Box: {box.width}, {box.height}")
    print(f"Perimeter: {box.CalculatePerimeter()}")
    print(f"Area: {box.CalculateArea()}")
