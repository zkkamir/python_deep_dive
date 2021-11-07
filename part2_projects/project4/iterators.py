import csv
from collections import namedtuple
from datetime import datetime
from os import path

FILE_PATH = path.dirname(__file__)
FILE_NAMES = 'employment.csv', 'personal_info.csv', 'update_status.csv', 'vehicles.csv'


def read_file(file_name):
    with open(path.join(FILE_PATH, file_name)) as f:
        reader = csv.reader(f, delimiter=',', quotechar='"')
        yield from reader


def parse_date(value, *, default=None):
    date_format = '%Y-%m-%dT%H:%M:%SZ'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def row_parser(iterator, parsers):
    for row in iterator:
        parsed_data = [parser(data)
                       for parser, data in zip(parsers, row)]
        yield parsed_data


def employees_iter():
    file = read_file(FILE_NAMES[0])
    tuple_fields = next(file)
    Employee = namedtuple('Employee', tuple_fields)

    field_parsers = str, str, str, str

    rows = row_parser(file, field_parsers)

    for row in rows:
        yield Employee(*row)


def personal_info_iter():
    file = read_file(FILE_NAMES[1])
    tuple_fields = next(file)
    PersonalInfo = namedtuple('PersonalInfo', tuple_fields)

    field_parsers = str, str, str, str, str

    rows = row_parser(file, field_parsers)

    for row in rows:
        yield PersonalInfo(*row)


def update_status_iter():
    file = read_file(FILE_NAMES[2])
    tuple_fields = next(file)
    UpdateStatus = namedtuple('UpdateStatus', tuple_fields)

    field_parsers = str, parse_date, parse_date

    rows = row_parser(file, field_parsers)

    for row in rows:
        yield UpdateStatus(*row)


def vehicles_iter():
    file = read_file(FILE_NAMES[3])
    tuple_fields = next(file)
    Vehicle = namedtuple('Vehicle', tuple_fields)

    field_parsers = str, str, str, int

    rows = row_parser(file, field_parsers)

    for row in rows:
        yield Vehicle(*row)


# employees = employees_iter()
# personal_info = personal_info_iter()
# update_status = update_status_iter()
# vehicles = vehicles_iter()

# for _ in range(5):
#     print(next(employees))
#     print(next(personal_info))
#     print(next(update_status))
#     print(next(vehicles))
