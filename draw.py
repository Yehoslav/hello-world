import tkinter
import math
from typing import List


class Vector:
    """This object only allows an accuracy of 2 digits, it will automatically round to the second digit."""

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __repr__(self):
        return f"Vector(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            return Vector(self.x * other, self.y * other)
        else:
            raise TypeError("Only multiplication with scalars is possible.")

    def __add__(self, other):
        if type(other) == list or type(other) == tuple:
            if len(other) == 2:
                return Vector(self.x + other[0], self.y + other[1])
            else:
                raise ValueError("To perform addition the size of the list or tuple must be 2.")
        if type(other) == Vector:
            return Vector(self.x + other.x, self.y + other.y)

    def lst(self):
        return self.x, self.y


class Triangle:
    """A triangle object that represents the geometrical shape of a triangle.
    This object sotres the edge lengths and automatically calculates the angles.
    The object also gives prebuilt functoins to calculate the triangles surface, perimeter and height (for now).

    Raises:
        ValueError: To create this object the dimensions of all the edges should be given. any other dimensions will
         be seen as an error.
    """
    _angles: list

    def __init__(self, edges: list) -> None:
        if len(edges) != 3:
            raise ValueError("A triangle has 3 edges.")

        self.edges = edges
        self.edges.sort(reverse=True)

    def perimeter(self) -> float:
        """Returns the perimeter of the triangle."""
        return sum(self.edges)

    def surface(self):
        """Returns the suface of the sfere."""
        s = self.perimeter() / 2
        return math.sqrt(s*(s - self.edges[0])*(s - self.edges[1])*(s - self.edges[2]))

    def height(self, base_edge: int = 0) -> float:
        """
        Args:
            base_edge (int, optional): The position of the edge in the list. Defaults to 0. **Mention** The list of
            edges in self.edges
            is sorted.

        Returns:
            float: The height of the triangle to the given base edge.
        """
        return self.surface() * 2 / self.edges[base_edge]

    @property
    def angles(self):
        """Returns a list that contains all the angles of the triangle in radians."""
        angles = [0., 0., 0.]
        angles[0] = math.asin(self.height()/self.edges[1])
        angles[1] = math.asin(self.height()/self.edges[2])
        angles[2] = math.pi - angles[0] - angles[1]
        return angles
    
    def to_degree(self):
        """Returns the angles converted to degrees."""
        return [round(math.degrees(angle), 2) for angle in self.angles]

    def draw_on_tkcanvas(self, canvas: tkinter.Canvas, fill: str, pos:tuple = (20, 20), scale: int = 56):
        """Draws the triangle to the given tkinter Canvas.

        Args:
            canvas (tkinter.Canvas): The given tk Canvas.
            fill (str): The color of the triangle.
            pos (tuple, optional): The position of the upper-lef corner of the square's container. Defaults to (20, 20).
            scale (int, optional): Changes the size of the triangle. Defaults to 56, 
            which represents with some error a scale of 1 to 1 cm on display.
        """
        start_point = pos[0] + math.cos(self.angles[0]) * self.edges[1] * scale, pos[1]
        mid_point = pos[0] + self.edges[0] * scale, self.height() * scale + pos[1]
        end_point = pos[0], self.height() * scale + pos[1]  

        canvas.create_polygon(start_point, mid_point, end_point, fill=fill)


class VectorTriangle:
    """A triangle object that represents the geometrical shape of a triangle.
    This object sotres the edge lengths and automatically calculates the angles.
    The object also gives prebuilt functoins to calculate the triangles surface, perimeter and height (for now).

    Raises:
        ValueError: To create this object the dimensions of all the edges should be given. any other dimensions will be
        seen as an error.
    """
    _vectors: List[Vector]

    def __init__(self, edges: list) -> None:
        if len(edges) != 3:
            raise ValueError("A triangle has 3 edges.")

        if edges[0] >= edges[1] + edges[2] or edges[1] >= edges[0] + edges[2] or edges[2] >= edges[0] + edges[1]:
            raise ValueError("Edges do not add up to a triangle.")

        self.edges = edges
        self.edges.sort(reverse=True)

    def perimeter(self) -> float:
        """Returns the perimeter of the triangle."""
        return sum(self.edges)

    def surface(self):
        """Returns the suface of the sfere."""
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.edges[0]) * (s - self.edges[1]) * (s - self.edges[2]))

    def height(self, base_edge: int = 0) -> float:
        """
        Args:
            base_edge (int, optional): The position of the edge in the list. Defaults to 0. **Mention** The list of
             edges in self.edges
            is sorted.

        Returns:
            float: The height of the triangle to the given base edge.
        """
        return self.surface() * 2 / self.edges[base_edge]

    @property
    def vectors(self):
        """Returns a list that contains all the angles of the triangle in radians."""
        angles = []
        angles += [Vector(-self.edges[0], 0)]
        angles += [Vector(self.pythagoras(c1=self.height(), h=self.edges[1]), self.height())]
        angles += [Vector(self.pythagoras(c1=self.height(), h=self.edges[2]), -self.height())]
        return angles

    def to_degree(self):
        """Returns the angles converted to degrees."""
        return [round(math.degrees(angle), 2) for angle in self.vectors]

    def draw_on_tkcanvas(self, canvas: tkinter.Canvas, fill: str, pos: tuple = (20, 20), scale: int = 56):
        """Draws the triangle to the given tkinter Canvas.

        Args:
            canvas (tkinter.Canvas): The given tk Canvas.
            fill (str): The color of the triangle.
            pos (tuple, optional): The position of the upper-lef corner of the square's container. Defaults to (20, 20).
            scale (int, optional): Changes the size of the triangle. Defaults to 56,
            which represents with some error a scale of 1 to 1 cm on display.
        """
        start_point = self.vectors[1] * scale + pos
        mid_point = (self.vectors[1] + self.vectors[2]) * scale + pos
        end_point = (self.vectors[0] + self.vectors[1] + self.vectors[2]) * scale + pos
        print(self.vectors)
        print(start_point, mid_point, end_point)
        canvas.create_polygon(start_point.lst(), mid_point.lst(), end_point.lst(), fill=fill)

    @staticmethod
    def pythagoras(c1: float, c2: float = 0, h: float = 0):
        if h == c2 == 0:
            raise ValueError("Both hypotenuse and a leg cannot be equal to 0.")
        if c2 == 0:
            return round(math.sqrt(h**2-c1**2), 2)
        if h == 0:
            return round(math.sqrt(c1**2+c2**2), 2)
