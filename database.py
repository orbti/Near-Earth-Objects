class NEODatabase:
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches

        # TODO: What additional auxiliary data structures will be useful?
        self._des_neo = {neo.designation: neo for neo in self._neos}
        self._name_neo = {neo.name: neo for neo in self._neos if neo.name != None}
        

        # TODO: Link together the NEOs and their close approaches.
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

    def query(self, filters=()):
        if filters:
            for approach in self._approaches:
                if all(map(lambda f: f(approach), filters)):
                    yield approach
        else:
            for approach in self._approaches:
                yield approach
