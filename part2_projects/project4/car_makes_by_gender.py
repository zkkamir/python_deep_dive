from collections import defaultdict
from itertools import groupby

from person_iterator import non_stale_person_iter


male_car_make_counter = defaultdict(int)
female_car_make_counter = defaultdict(int)

persons = groupby(non_stale_person_iter(), lambda x: x.gender)

for gender, data in persons:
    if gender == 'Male':
        for person in data:
            male_car_make_counter[person.vehicle_make] += 1
    else:
        for person in data:
            female_car_make_counter[person.vehicle_make] += 1

sorted_male = {k: v for k, v in sorted(
    male_car_make_counter.items(), key=lambda x: x[1], reverse=True)}
sorted_female = {k: v for k, v in sorted(
    female_car_make_counter.items(), key=lambda x: x[1], reverse=True)}

print(sorted_male)
print(sorted_female)
