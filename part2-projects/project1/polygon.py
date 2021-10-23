class Polygon:
    """A class to represent a polygon of any number of vertices."""

    def __init__(self, n: int, circumradius: float):
        self.n = n
        self.circumradius = circumradius
        self.interior_angle = None
        self.edge_length = None
        self.apothem = None
        self.area = None
        self.perimeter = None

    def __repr__(self) -> str:
        return f"Polygon({self.n}, {self.circumradius}"

    def __eq__(self, o) -> bool:
        """
        Compares the equality of two polygons based on their
        number of vertices and their circumradius.
        """

        return (self.n == o.n) and (self.circumradius == o.circumradius)

    def __gt__(self, o) -> bool:
        """Compares two polygons based on their number of vertices."""

        return self.n > o.n
