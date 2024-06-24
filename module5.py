class Point:
    """ A class to represent a point in 2D space """
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

class Rectangle:
    """ A class to manufacture rectangle objects """
    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h
    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

def create_rectangle(x, y, width, height):
    return Rectangle(Point(x, y), width, height)

def str_rectangle(rect):
    return str(rect)

def shift_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy

def offset_rectangle(rect, dx, dy):
    new_x = rect.corner.x + dx
    new_y = rect.corner.y + dy
    return Rectangle(Point(new_x, new_y), rect.width, rect.height)

r1 = create_rectangle(10, 20, 30, 40)
print(str_rectangle(r1))
shift_rectangle(r1, -10, -20)
print(str_rectangle(r1)) 
r2 = offset_rectangle(r1, 100, 100)
print(str_rectangle(r1))
print(str_rectangle(r2))
