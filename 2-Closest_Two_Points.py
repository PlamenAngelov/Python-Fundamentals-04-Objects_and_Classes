import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def distance_between_points(p1, p2):
    delta_x = abs(p1.x - p2.x)
    delta_y = abs(p1.y - p2.y)
    return math.sqrt(delta_x ** 2 + delta_y ** 2)

def find_closest_points(points):
    m = len(points)
    result_list = []
    min_distance = None
    if m > 0:
        min_distance = distance_between_points(points[0], points[1])
        result_list = [points[0], points[1]]

    for i in range(0, m):
        for j in range(0, m):
            if i != j:
                temp_distance = distance_between_points(points[i], points[j])
                if temp_distance < min_distance:
                    min_distance = temp_distance
                    result_list = [points[i], points[j]]
    return result_list

n = int(input())
point_list = []

for i in range(0, n):
    temp_list = list(map(float,input().split(" ")))
    point_list.append(Point(temp_list[0], temp_list[1]))


res_list = find_closest_points(point_list)

print(f"{distance_between_points(res_list[0], res_list[1]):.3f}")
print(f"({res_list[0].x:.2g}, {res_list[0].y:.2g})")
print(f"({res_list[1].x:.2g}, {res_list[1].y:.2g})")


