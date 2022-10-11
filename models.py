from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    def __init__(self, **info):
        self.designation = info.get('designation')
        self.name = info.get('name')
        self.diameter = info.get('diameter')
        self.hazardous = info.get('hazardous')

        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name != None:
            return self.designation + ' ' + self.name
        else:
            return self.designation

    def serialize(self):
        """Return a dictionary containing  relevant attribues for CSV or JSON serialization"""
        return {'designation': self.designation,
                'name': self.name if self.name else '',
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}

    def __str__(self):
        """Return `str(self)`."""
        return f"NEO {self.fullname} has a diamter {self.diameter:.3f} km and {'is' if self.hazardous else 'is not'} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"
    
class CloseApproach:
    def __init__(self, **info):
        self._designation = info.get('_designation')
        self.time = cd_to_datetime(info.get('time')) 
        self.distance = info.get('distance')
        self.velocity = info.get('velocity')

        self.neo = None

    @property
    def time_str(self):
        return datetime_to_str(self.time)

    def serialize(self):
        """Return a dictionary containing  relevant attribues for CSV or JSON serialization"""
        return {'neo': self.neo,
                'datetime_utc': datetime_to_str(self.time),
                'distance_au': self.distance,
                'velocity_km_s': self.velocity}

    def __str__(self):
        return f"On {self.time_str}, {self.neo.fullname} approaches Earth at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, " \
               f"velocity={self.velocity:.2f}, neo={self.neo!r})"
