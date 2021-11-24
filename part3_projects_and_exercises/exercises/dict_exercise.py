# # exercise 1

# composers = {'Johann': 65, 'Ludwig': 56, 'Frederic': 39, 'Wolfgang': 35}
# print(composers)

# # solution
# sorted_composers = {k: composers[k] for k in
#                     sorted(composers, key=lambda x: composers[x])}
# print(sorted_composers)


# # exercise 2

# d1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# d2 = {'b': 20, 'c': 30, 'y': 40, 'z': 50}

# # solution


# def common_keys_dict(d1, d2):
#     result = {k: (d1[k], d2[k])
#               for k in (d1.keys() & d2.keys())}
#     return result


# print(common_keys_dict(d1, d2))


# # exercise 3
# from collections import defaultdict

# d1 = {'python': 10, 'java': 3, 'c#': 8, 'javascript': 15}
# d2 = {'java': 10, 'c++': 10, 'c#': 4, 'go': 9, 'python': 6}
# d3 = {'erlang': 5, 'haskell': 2, 'python': 1, 'pascal': 1}


# # solution

# d = defaultdict(int)


# def process(*args):
#     for dict in args:
#         for item in dict.items():
#             d[item[0]] += item[1]

#     sorted_results = {k: d[k]
#                       for k in sorted(d, key=lambda x: d[x], reverse=True)}

#     print(sorted_results)


# process(d1, d2, d3)


# # exercise 4
# from itertools import product


# n1 = {'employees': 100, 'employee': 5000, 'users': 10, 'user': 100}
# n2 = {'employees': 250, 'users': 23, 'user': 230}
# n3 = {'employees': 150, 'users': 4, 'login': 1000}

# # solution
# result = {}


# def process(n1, n2, n3):
#     union = n1.keys() | n2.keys() | n3.keys()
#     intersection = n1.keys() & n2.keys() & n3.keys()
#     difference = union - intersection

#     for key in difference:
#         result[key] = (n1.get(key, 0), n2.get(key, 0), n3.get(key, 0))

#     print(result)


# process(n1, n2, n3)
