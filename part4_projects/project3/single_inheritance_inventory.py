class Resource:
    def __init__(self, name, manufacturer, total, allocated=0):
        self.name = Resource.validate_is_str(name, 'name')
        self.manufacturer = Resource.validate_is_str(
            manufacturer, 'manufacturer')
        self._total = Resource.validate_is_positive_int(total, 'total')
        if not isinstance(allocated, int) or allocated < 0:
            raise ValueError('Allocated value must be a non-negative integer.')
        self._allocated = allocated

    @property
    def total(self):
        return self._total

    @property
    def allocated(self):
        return self._allocated

    @property
    def category(self):
        return f'{self.__class__.__name__.lower()}'

    @property
    def remaining(self):
        return self._total - self.allocated

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'Resource({self.name}, {self.manufacturer}, {self.total})'

    def claim(self, value):
        if (self.allocated + value) > self.total:
            raise ValueError('Cannot claim more than total.')
        self._allocated += value

    def freeup(self, value):
        if self.allocated < value:
            raise ValueError('Cannot free up more than allocated.')
        self._allocated -= value

    def died(self, value):
        self._allocated -= value
        self._total -= value

    def purchased(self, value):
        self._total += value

    @staticmethod
    def validate_is_positive_int(value, field_name):
        if not isinstance(value, int) or value < 1:
            raise ValueError(f'{field_name} must be a positive integer.')
        return value

    @staticmethod
    def validate_is_str(value, field_name):
        if not isinstance(value, str):
            raise ValueError(f'{field_name} must be an string.')
        return value


class CPU(Resource):
    def __init__(self, name, manufacturer, total, cores, socket, power_watts, allocated=0):
        super().__init__(name, manufacturer, total, allocated=allocated)
        self.cores = Resource.validate_is_positive_int(cores, 'cores')
        self.socket = Resource.validate_is_str(socket, 'socket')
        self.power_watts = Resource.validate_is_positive_int(
            power_watts, 'power watts')


class Storage(Resource):
    def __init__(self, name, manufacturer, total, capacity_GB, allocated=0):
        super().__init__(name, manufacturer, total, allocated=allocated)
        self.capacity_GB = Resource.validate_is_positive_int(
            capacity_GB, 'capacity_GB')


class HDD(Storage):
    def __init__(self, name, manufacturer, total, capacity_GB, size, rpm, allocated=0):
        if size not in {2.5, 3.5}:
            raise ValueError('Size must be 2.5" or 3.5"')
        super().__init__(name, manufacturer, total, capacity_GB, allocated=allocated)
        self.size = size
        self.rpm = Resource.validate_is_positive_int(rpm, 'rpm')


class SSD(Storage):
    def __init__(self, name, manufacturer, total, capacity_GB, interface, allocated=0):
        super().__init__(name, manufacturer, total, capacity_GB, allocated=allocated)
        self.interface = Resource.validate_is_str(interface)


cpu = CPU('CPU', 'Intel', 5, 200, 'a')
