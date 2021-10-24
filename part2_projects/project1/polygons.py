from .polygon import Polygon


class Polygons:
    """
    A class to represent a sequence of polygons, takes the largest
    number of vertices and a common circumradius as arguments and
    will generate a sequence containing polygons from
    Polygon(3, common_radius), up to and including
    Polygon(n, common_radius).
    """

    def __init__(self, largest_n: int, common_circumradius: float):
        self.largest_n = largest_n
        self.common_circumradius = common_circumradius
        self._polygons = []
        self._max_efficiency_polygon = None

    @property
    def polygons(self):
        if not self._polygons:
            # the polygon list is empty
            n = 3
            while n <= self.largest_n:
                self._polygons.append(Polygon(n, self.common_circumradius))
                n += 1
        return self._polygons

    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            self._max_efficiency_polygon = max(
                self.polygons, key=lambda p: p.area / p.perimeter)
        return self._max_efficiency_polygon

    def __getitem__(self, s):
        return self.polygons[s]

    def __len__(self):
        return len(self.polygons)
