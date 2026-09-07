class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = []

for i in range(1000):
    value = 1 + i * 2
    points.append(Point(value, value))

points[1].color = "yellow"
