from collections import namedtuple
from datetime import datetime

import iterators


def person_iter():
    Person = namedtuple('Person', 'ssn fname lname gender language \
                                   employer department employee_id \
                                   vehicle_make vehicle_model model_year \
                                   last_updated created')

    to_be_used_up_iterator = iterators.personal_info_iter()

    personal_info = iterators.personal_info_iter()
    employees = iterators.employees_iter()
    vehicles = iterators.vehicles_iter()
    update_status = iterators.update_status_iter()

    for _ in to_be_used_up_iterator:
        ssn, fname, lname, gender, lang = next(personal_info)
        employer, department, employee_id, _ = next(employees)
        _, vehicle_make, vehicle_model, model_year = next(vehicles)
        _, last_updated, created = next(update_status)

        yield Person(ssn, fname, lname, gender, lang,
                     employer, department, employee_id,
                     vehicle_make, vehicle_model, model_year,
                     last_updated, created)


# persons = person_iter()

# for _ in range(5):
#     print(next(persons))

def stale_person_iter():
    persons = person_iter()

    for person in persons:
        if person.last_updated < datetime(2017, 3, 1).date():
            yield person


stale_persons = stale_person_iter()

for _ in range(5):
    print(next(stale_persons))
