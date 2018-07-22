import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(p1, p2):
    delta_x = abs(p1.x - p2.x)
    delta_y = abs(p1.y - p2.y)
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


# Read both points separately
# Calculate the distance between them
inp_point1 = list(map(float,input().split(" ")))
inp_point2 = list(map(float,input().split(" ")))
p1 = Point(inp_point1[0], inp_point1[1])
p2 = Point(inp_point2[0], inp_point2[1])

distance = distance_between_points(p1, p2);

# Print the distance
print(f'{distance:.3f}')
