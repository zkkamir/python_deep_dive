from os import path
import csv
from collections import namedtuple
from contextlib import contextmanager
from itertools import islice

FILE_PATH = path.dirname(__file__)
file_names = path.join(FILE_PATH, 'cars.csv'), path.join(
    FILE_PATH, 'personal_info.csv')


@contextmanager
def parsed_data(file_name):
    f = open(file_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(1000))
        # return the read head to the beginning
        f.seek(0)
        reader = csv.reader(f, dialect)
        headers = map(lambda s: s.lower(), next(reader))
        nt = namedtuple('Data', headers)
        yield (nt(*row) for row in reader)
    finally:
        f.close()


with parsed_data(file_names[0]) as data:
    for row in islice(data, 5):
        print(row)

with parsed_data(file_names[1]) as data:
    for row in islice(data, 5):
        print(row)
