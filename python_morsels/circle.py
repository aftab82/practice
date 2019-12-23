import math


class Circle:

    """Circle with a radius, diameter and an area."""

    def __init__(self, radius=1):
        self.radius = radius

    def __repr__(self):
        return 'Circle({radius})'.format(radius=self.radius)

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self._radius = radius


c = Circle()
print(c)
print(c.radius)
print(c.diameter)
print(c.diameter())
