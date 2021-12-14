from functools import total_ordering


@total_ordering
class Mod:
    def __init__(self, value, modulus):
        self.initial_value = self.validate_is_int(value, 'Value')
        self._modulus = self.validate_is_positive(
            self.validate_is_int(modulus, 'Modulus'))
        self._value = None

    @staticmethod
    def validate_is_int(value, field_name):
        if not isinstance(value, int):
            raise ValueError(f'{field_name} must be an integer.')
        return value

    @staticmethod
    def validate_is_positive(value):
        if value <= 0:
            raise ValueError('Modulus must be positive.')
        return value

    @property
    def value(self):
        if self._value is None:
            self._value = self.initial_value % self.modulus
        return self._value

    @property
    def modulus(self):
        return self._modulus

    def __eq__(self, other):
        if isinstance(other, int):
            return self.value == other % self.modulus
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Comparison can only be done between two '
                                 f'Mod objects with the same modulus.')
            return self.value == other.value

    def __lt__(self, other):
        if isinstance(other, int):
            return self.value < other % self.modulus
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Comparison can only be done between two '
                                 f'Mod objects with the same modulus.')
            return self.value < other.value

    def __hash__(self):
        # hash the value, modulus pair as a tuple
        return hash((self.value, self.modulus))

    def __int__(self):
        return self.value

    def __repr__(self):
        return (f'Mod({self.initial_value}, {self.modulus}) '
                f'== Mod({self.value}, {self.modulus})')

    def __add__(self, other):
        if isinstance(other, int):
            result_value = self.value + (other % self.modulus)
            return Mod(result_value, self.modulus)
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Addition can only be done between two '
                                 f'Mod objects with the same modulus.')
            result_value = self.value + other.value
            return Mod(result_value, self.modulus)

    def __sub__(self, other):
        if isinstance(other, int):
            result_value = self.value - (other % self.modulus)
            return Mod(result_value, self.modulus)
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Subtraction can only be done between two '
                                 f'Mod objects with the same modulus.')
            result_value = self.value - other.value
            return Mod(result_value, self.modulus)

    def __mul__(self, other):
        if isinstance(other, int):
            result_value = self.value * (other % self.modulus)
            return Mod(result_value, self.modulus)
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Multipication can only be done between two '
                                 f'Mod objects with the same modulus.')
            result_value = self.value * other.value
            return Mod(result_value, self.modulus)

    def __pow__(self, other):
        if isinstance(other, int):
            result_value = self.value ** (other % self.modulus)
            return Mod(result_value, self.modulus)
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Raising to power can only be done between'
                                 f' two Mod objects with the same modulus.')
            result_value = self.value ** other.value
            return Mod(result_value, self.modulus)

    def __iadd__(self, other):
        if isinstance(other, int):
            self._value = self.value + (other % self.modulus)
            return self
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Addition can only be done between two '
                                 f'Mod objects with the same modulus.')
            self._value = self.value + other.value
            return self

    def __isub__(self, other):
        if isinstance(other, int):
            self._value = self.value - (other % self.modulus)
            return self
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Subtraction can only be done between two '
                                 f'Mod objects with the same modulus.')
            self._value = self.value - other.value
            return self

    def __imul__(self, other):
        if isinstance(other, int):
            self._value = self.value * (other % self.modulus)
            return self
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Multipication can only be done between two '
                                 f'Mod objects with the same modulus.')
            self._value = self.value * other.value
            return self

    def __ipow__(self, other):
        if isinstance(other, int):
            self._value = self.value ** (other % self.modulus)
            return self
        elif isinstance(other, Mod):
            if not self.modulus == other.modulus:
                raise ValueError('Raising to power can only be done between two '
                                 f'Mod objects with the same modulus.')
            self._value = self.value ** other.value
            return self


a = Mod(7, 12)
b = Mod(7, 24)
c = Mod(19, 12)
d = 7
e = 19

print('a == a >> True')
print(a == a)
print('a == b >> ValueError')
try:
    print(a == b)
except ValueError as ex:
    print('ValueError: ', ex)
print('a == c >> True')
print(a == c)
print('a == d >> True')
print(a == d)
print('c == d >> True')
print(c == d)
print('b == d >> True')
print(a == c)
print('c == e >> False')
print(c == e)

print('*' * 10)
print('hash(a) == hash(c) >> True')
print(hash(a) == hash(c))

print('*' * 10)
print('a + a >> Mod(14, 12)')
print(a + a)
print('a + c >> Mod(14, 12)')
print(a + c)
print('a + b >> ValueError')
try:
    print(a + b)
except ValueError as ex:
    print('ValueError: ', ex)
print('a + d >> Mod(14, 12)')
print(a + d)
print('a + e >> Mod(14, 12)')
print(a + e)

print('*' * 10)
print(f'a = {a}')
print(f'id a = {id(a)}')
a += a
print(f'a = {a}')
print(f'id a = {id(a)}')


print('*' * 10)
print(a < a)
print(a < c)
print(a < d)
print(a < e)
print(a >= a)
print(a >= c)
print(a >= d)
print(a >= e)
