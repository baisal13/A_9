import math
import random

from abc import ABC, abstractmethod

class Shape3D(ABC):
    @abstractmethod
    def surface_area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

class Cube(Shape3D):
    def __init__(self, side: float):
        self.side = side

    def surface_area(self) -> float:
        return 6 * self.side ** 2

    def volume(self) -> float:
        return self.side ** 3


class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def surface_area(self) -> float:
        return 4 * math.pi * self.radius ** 2

    def volume(self) -> float:
        return (4/3) * math.pi * self.radius ** 3


class Cylinder(Shape3D):
    def __init__(self, radius: float, height: float):
        self.radius = radius
        self.height = height

    def surface_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def volume(self) -> float:
        return math.pi * self.radius ** 2 * self.height

def random_shape() -> Shape3D:
    shape_type = random.choice(['cube', 'sphere', 'cylinder'])

    if shape_type == 'cube':
        side = random.uniform(1.0, 10.0)
        return Cube(side)

    elif shape_type == 'sphere':
        radius = random.uniform(1.0, 10.0)
        return Sphere(radius)

    elif shape_type == 'cylinder':
        radius = random.uniform(1.0, 10.0)
        height = random.uniform(1.0, 20.0)
        return Cylinder(radius, height)

def main():
    shapes = [random_shape() for _ in range(5)]  # create 5 random shapes

    for idx, shape in enumerate(shapes, start=1):
        print(f"Shape {idx}: {shape.__class__.__name__}")

        if isinstance(shape, Cube):
            print(f"  Side length: {shape.side:.2f}")
        elif isinstance(shape, Sphere):
            print(f"  Radius: {shape.radius:.2f}")
        elif isinstance(shape, Cylinder):
            print(f"  Radius: {shape.radius:.2f}")
            print(f"  Height: {shape.height:.2f}")

        print(f"  Surface Area: {shape.surface_area():.2f}")
        print(f"  Volume: {shape.volume():.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
