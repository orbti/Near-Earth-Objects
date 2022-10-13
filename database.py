

class NEODatabase:
    """ NEODatabase class useed to build the database. Database will be able to search on 
    designation or name to get NEO or user will submit filters to show all close 
    approaches within the filters. """
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches
        
        # Build key-value pair for better look ups
        self._des_neo = {neo.designation: neo for neo in self._neos}
        self._name_neo = {neo.name: neo for neo in self._neos if neo.name != None}

        #Link together the NEOs and their close approaches.
        for approache in self._approaches:
            neo = self._des_neo[approache._designation]
            neo.approaches.append(approache)
            approache.neo = neo
        
    def get_neo_by_designation(self, designation):
        if designation in self._des_neo:
            return self._des_neo[designation]
        return None

    def get_neo_by_name(self, name):
        if name in self._name_neo:
            return self._name_neo[name]
        return None

    def query(self, filters=None):
        if filters:
            for approach in self._approaches:
                if all(map(lambda f: f(approach), filters)):
                    yield approach
                
        else:
            for approach in self._approaches:
                yield approach
