from os import path
import csv
from collections import namedtuple
from itertools import islice

FILE_PATH = path.dirname(__file__)
file_names = path.join(FILE_PATH, 'cars.csv'), path.join(
    FILE_PATH, 'personal_info.csv')


def get_dialect(file_name):
    with open(file_name) as f:
        return csv.Sniffer().sniff(f.read(1000))


class FileParser:
    def __init__(self, file_name):
        self.file_name = file_name

    def __enter__(self):
        self._file = open(self.file_name, 'r')
        self._reader = csv.reader(self._file, get_dialect(self.file_name))
        headers = map(lambda s: s.lower(), next(self._reader))
        self._nt = namedtuple('Data', headers)
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self._file.close()
        # If an exception occured do not silence it
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._file.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._reader))


with FileParser(file_names[1]) as data:
    for row in islice(data, 10):
        print(row)
