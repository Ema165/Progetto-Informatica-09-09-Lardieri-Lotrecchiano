class GeneticEditingError(Exception):

    pass

class InvalidGenomeError(GeneticEditingError):

    pass


class InvalidInsertionPointError(GeneticEditingError):

    pass


class InvalidInsertionError(GeneticEditingError):

    pass


class InvalidEditSequenceError(GeneticEditingError):

    pass