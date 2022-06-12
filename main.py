class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        print('getting width')
        return self.width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError("width must be positive.")
        else:
            self._width = width

    @property
    def height(self):
        return self.height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError("height must be positive.")
        else:
            self._height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return self.width + self.height

    def __str__(self):
        return f'Rectangle: width={self.width}, height={self.height}'

    def __repr__(self):
        return f'Rectangle({self.width}, {self.height})'

    def __eq__(self, other):
        return (self.width, self.height) == (other.width, other.height)


r1 = Rectangle(10, 20)

print(r1)
r1.width = -125