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
        if largest_n < 3:
            raise ValueError("largest_n must be greater than 3.")
        self.largest_n = largest_n
        self.common_circumradius = common_circumradius
        # self._polygons = [Polygon(i, common_circumradius)
        #                   for i in range(3, largest_n+1)]
        self._max_efficiency_polygon = None

    @property
    def max_efficiency_polygon(self):
        if self._max_efficiency_polygon is None:
            self._max_efficiency_polygon = max(
                self.PolygonsIterator(
                    self.largest_n, self.common_circumradius),
                key=lambda p: p.area / p.perimeter)
        return self._max_efficiency_polygon

    def __iter__(self):
        return self.PolygonsIterator(self.largest_n, self.common_circumradius)

    class PolygonsIterator:
        def __init__(self, largest_n, common_circumradius):
            self.largest_n = largest_n
            self.R = common_circumradius
            self.i = 3

        def __iter__(self):
            return self

        def __next__(self):
            if self.i > self.largest_n:
                raise StopIteration
            else:
                result = Polygon(self.i, self.R)
                self.i += 1
                return result

    # def __getitem__(self, s):
    #     return self._polygons[s]

    def __len__(self):
        return self.largest_n - 2

    def __repr__(self) -> str:
        return f"Polygons({self.largest_n}, {self.common_circumradius})"
