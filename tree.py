## Code reference Charnesky:
## https://github.com/EricCharnesky/CIS2001-Winter2022/blob/main/Trees/main.py

class Tree:

    class Position:

        def element(self):
            raise NotImplementedError

        def __eq__(self, other):
            raise NotImplementedError

        def __ne__(self, other):
            return not (self==other)

    def root(self):
        raise NotImplementedError

    def parent(self, position):
        raise NotImplementedError

    def number_of_children(self, position):
        raise NotImplementedError

