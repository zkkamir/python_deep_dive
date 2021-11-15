import csv
from contextlib import contextmanager
from os import path

FILE_PATH = path.dirname(__file__)


def parse_data(file_name):
    f = open(file_name)
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)  # skip the header row
        yield from csv.reader(f, dialect=dialect)
    finally:
        f.close()


def coroutine(func):
    def inner(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro
    return inner


@coroutine
def save_csv(file_name):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        while True:
            row = yield
            writer.writerow(row)


@coroutine
def filter_data(filter_pred, target):
    while True:
        row = yield
        if filter_pred(row):
            target.send(row)


@coroutine
def pipeline_coro(out_file, name_filters):
    save = save_csv(out_file)

    target = save
    for name_filter in name_filters:
        # use 'v' instead of name_filter in the loop body. becuase the
        # reference to the 'name_filter' at runtime would be the same for
        # every iteration otherwise.
        target = filter_data(lambda dr, v=name_filter: v in dr[0], target)

    while True:
        received = yield
        target.send(received)


@contextmanager
def pipeline(out_file, name_filters):
    p = pipeline_coro(out_file, name_filters)
    try:
        yield p
    finally:
        p.close()


with pipeline(path.join(FILE_PATH, 'out.csv'), ('Chevrolet', 'Landau', 'Carlo')) as p:
    for row in parse_data(path.join(FILE_PATH, 'cars.csv')):
        p.send(row)


with open(path.join(FILE_PATH, 'out.csv')) as f:
    for row in f:
        print(row)
