# # exercise 1

# from collections import defaultdict, Counter
# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}

# # solution 1

# d = defaultdict(int)


# def process_with_defaultdict(*args):
#     for dict in args:
#         for item in dict.items():
#             d[item[0]] += item[1]

#     sorted_results = {k: d[k]
#                       for k in sorted(d, key=lambda x: d[x], reverse=True)}

#     print(sorted_results)


# process_with_defaultdict(d1, d2, d3)

# # solution 2

# d = Counter()


# def process_with_counter(*args):
#     for dict in args:
#         d.update(Counter(dict))

#     sorted_results = {k: d[k]
#                       for k in sorted(d, key=lambda x: d[x], reverse=True)}

#     print(sorted_results)


# process_with_counter(d1, d2, d3)


# # exercise 2
# from collections import Counter
# from random import seed, choices

# eye_colors = 'amber', 'blue', 'brown', 'gray', 'green', 'hazel', 'red', 'violet'


# class Person:
#     def __init__(self, eye_color):
#         self.eye_color = eye_color


# seed(0)
# persons = [Person(color) for color in choices(eye_colors[2:], k=50)]

# # solution


# def eye_color_counter(colors, persons):
#     d = Counter(person.eye_color for person in persons)
#     for color in colors:
#         d[color] = d[color]
#     return d.most_common()


# print(eye_color_counter(eye_colors, persons))

# # exercise 3
# # solution
# from collections import ChainMap
# import json
# from pprint import pprint


# def load_settings(env):
#     with open(f'exercises/specialized_dicts_files/{env}.json') as f:
#         settings = json.load(f)
#     return settings


# def chain_recursive(d1, d2):
#     chain = ChainMap(d1, d2)
#     for k, v in d1.items():
#         if isinstance(v, dict) and k in d2:
#             chain[k] = chain_recursive(d1[k], d2[k])
#         return chain


# def settings(env):
#     common_settings = load_settings('common')
#     env_settings = load_settings(f'{env}')
#     return chain_recursive(env_settings, common_settings)


# dev = settings('dev')

# pprint(dev)
