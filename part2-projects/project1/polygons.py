from . import polygon


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
        self.max_efficiency_polygon = None

    def __getitem__(self):
        pass

    def __len__(self):
        pass
