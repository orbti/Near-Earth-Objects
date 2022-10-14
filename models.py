"""
Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.
The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.
You'll edit this file in Task 1.
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """
    A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self.designation = info.get('designation')
        self.name = info.get('name')
        self.diameter = info.get('diameter')
        self.hazardous = info.get('hazardous')
        self.approaches = []

    @property
    def fullname(self):
        """
        Return fullname.

        Return a representation of the
        full name of this NEO.
        """
        if self.name is not None:
            return self.designation + ' ' + self.name
        else:
            return self.designation

    def serialize(self):
        """
        Return dict of serialized attributes.

        Return a dictionary containing  relevant
        attribues for CSV or JSON serialization
        """
        return {'designation': self.designation,
                'name': self.name if self.name else '',
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}

    def __str__(self):
        """Return `str(self)`."""
        return f"NEO {self.fullname} has a diamter {self.diameter:.3f} km and"\
            f"{ 'is' if self.hazardous else 'is not'} potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject(designation={self.designation!r}, " \
            f"name={self.name!r}, "\
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"


class CloseApproach:
    """
    A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """
        Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        self._designation = info.get('_designation')
        self.time = info.get('time')
        self.distance = info.get('distance')
        self.velocity = info.get('velocity')
        self.neo = None

    @property
    def time_str(self):
        """Return datetime to string."""
        return datetime_to_str(self.time)

    def serialize(self):
        """
        Return dict of serialized attributes.

        Return a dictionary containing  relevant
        attribues for CSV or JSON serialization
        """
        return {'neo': self.neo,
                'datetime_utc': datetime_to_str(self.time),
                'distance_au': self.distance,
                'velocity_km_s': self.velocity}

    def __str__(self):
        """Return `str(self)`."""
        return f"On {self.time_str}, {self.neo.fullname} approaches " \
            f"Earth at a distance of {self.distance:.2f} au " \
            f"and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time={self.time_str!r}, "\
            f"distance={self.distance:.2f}, " \
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
