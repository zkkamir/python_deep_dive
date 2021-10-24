import math


class Polygon:
    """A class to represent a polygon of any number of vertices."""

    def __init__(self, n: int, circumradius: float):
        if n < 3:
            raise ValueError("Polygon must have at least 3 sides.")
        self.vertices = n
        self.circumradius = circumradius
        self.edges = n
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def interior_angle(self):
        if self._interior_angle is None:
            self._interior_angle = (self.vertices - 2) * (180 / self.vertices)
        return self._interior_angle

    @property
    def edge_length(self):
        if self._edge_length is None:
            self._edge_length = 2 * self.circumradius * \
                math.sin(math.pi / self.vertices)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.circumradius * \
                math.cos(math.pi / self.vertices)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = 0.5 * self.vertices * self.edge_length * self.apothem
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self.vertices * self.edge_length
        return self._perimeter

    def __repr__(self) -> str:
        return f"Polygon({self.vertices}, {self.circumradius})"

    def __eq__(self, other) -> bool:
        """
        Compares the equality of two polygons based on their
        number of vertices and their circumradius.
        """
        if isinstance(other, self.__class__):
            return (self.vertices == other.vertices
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other) -> bool:
        """Compares two polygons based on their number of vertices."""
        if isinstance(other, Polygon):
            return self.vertices > other.vertices
        else:
            return NotImplemented
