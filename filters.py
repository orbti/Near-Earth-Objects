import operator
from re import X


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""


class AttributeFilter:
    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        raise UnsupportedCriterionError

    def __repr__(self):
        return f"{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})"

class DateFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.time.date()

class HazardousFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.hazardous

class DiameterFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.neo.diameter

class VelocityFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.velocity

class DistanceFilter(AttributeFilter):
    @classmethod
    def get(cls, approach):
        return approach.distance

def create_filters(
        date=None, start_date=None, end_date=None,
        distance_min=None, distance_max=None,
        velocity_min=None, velocity_max=None,
        diameter_min=None, diameter_max=None,
        hazardous=None
):
    args = locals()
    filters = []
    for key, value in args.items():
        if value == None:
            continue
        if key == 'date':
            filters.append(DateFilter(operator.eq,value))
        elif key == 'start_date':
            filters.append(DateFilter(operator.ge,value))
        elif key == 'end_date':
            filters.append(DateFilter(operator.le,value))
        elif key == 'distance_min':
            filters.append(DistanceFilter(operator.ge, value))
        elif key == 'distance_max':
            filters.append(DistanceFilter(operator.le, value))
        elif key == 'velocity_max':
            filters.append(VelocityFilter(operator.le, value))
        elif key == 'velocity_min':
            filters.append(VelocityFilter(operator.ge, value))
        elif key == 'diameter_max':
            filters.append(DiameterFilter(operator.le, value))
        elif key == 'diameter_min':
            filters.append(DiameterFilter(operator.ge, value))
        elif value == True:
            filters.append(HazardousFilter(operator.eq, True))
        elif value == False:
            filters.append(HazardousFilter(operator.eq, False))
    return filters

def limit(iterator, n=None):
    count = 1
    if n == 0 or n == None:
        for x in iterator:
            yield x
    else:
        for x in iterator:
            if count > n:
                break
            count += 1
            yield x
    
        
                
            
