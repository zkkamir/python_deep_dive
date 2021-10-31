import os
from collections import defaultdict, namedtuple
from datetime import datetime


FILE_PATH = os.path.dirname(__file__)

file_name = "nyc_parking_tickets_extract.csv"


with open(os.path.join(FILE_PATH, file_name)) as f:
    column_headers = next(f).strip('\n').split(',')

column_names = [header.replace(' ', '_').lower()
                for header in column_headers]

Ticket = namedtuple('Ticket', column_names)


def read_data():
    """A generator that yields one line of data at a time"""
    with open(os.path.join(FILE_PATH, file_name)) as f:
        # Skipping the first line of the file because it contains the headers
        next(f)
        yield from f


def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default


def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default


def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            # It's an empty string
            return default
        else:
            return cleaned
    except ValueError:
        return default


column_parsers = (parse_int,  # summon_number, default is None
                  parse_string,  # plate_id, default is None
                  lambda x: parse_string(x, default=''),  # state
                  lambda x: parse_string(x, default=''),  # plate_type
                  parse_date,  # issue_date, default is None
                  parse_int,  # violation_code
                  lambda x: parse_string(x, default=''),  # body type
                  parse_string,  # make, default is None
                  lambda x: parse_string(x, default='')  # description
                  )


def parse_row(row, *, default=None):
    fields = row.strip('\n').split(',')
    parsed_data = [func(field)
                   for func, field in zip(column_parsers, fields)]
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default


def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed


def violation_count_by_make():
    makes_counts = defaultdict(int)

    for data in parsed_data():
        makes_counts[data.vehicle_make] += 1

    return {make: count
            for make, count in sorted(makes_counts.items(),
                                      key=lambda t: t[1],
                                      reverse=True)
            }


if __name__ == "__main__":
    print(violation_count_by_make())
