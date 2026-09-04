import logging

from exceptions import (
    InvalidEditSequenceError,
    InvalidGenomeError,
    InvalidInsertionError,
    InvalidInsertionPointError,
)

GENOMIC_ALPHABET: set[str] = {"A", "C", "G", "T"}

logger = logging.getLogger(__name__)


def validate_genetic_sequence(sequence: str, sequence_name: str) -> None:

    if not isinstance(sequence, str):
        raise TypeError(f"{sequence_name} deve essere una stringa.")

    if len(sequence) == 0:
        if sequence_name == "genome":
            raise InvalidGenomeError("Il genoma non può essere vuoto.")
        if sequence_name == "insertion":
            raise InvalidInsertionError("L'insertion non può essere vuota.")
        raise InvalidInsertionPointError("L'insertion point non può essere vuoto.")

    invalid_bases = set(sequence) - GENOMIC_ALPHABET

    if invalid_bases:
        invalid_bases_text = ", ".join(sorted(invalid_bases))

        if sequence_name == "genome":
            raise InvalidGenomeError(
                f"Il genoma contiene basi non valide: {invalid_bases_text}."
            )

        if sequence_name == "insertion":
            raise InvalidInsertionError(
                f"L'insertion contiene basi non valide: {invalid_bases_text}."
            )

        raise InvalidInsertionPointError(
            f"L'insertion point contiene basi non valide: {invalid_bases_text}."
        )


def edit_genome(genome: str, insertion_point: str, insertion: str) -> str:

    validate_genetic_sequence(genome, "genome")
    validate_genetic_sequence(insertion_point, "insertion_point")
    validate_genetic_sequence(insertion, "insertion")

    insertion_point_index = genome.rfind(insertion_point)

    if insertion_point_index == -1:
        raise InvalidInsertionPointError(
            f"L'insertion point '{insertion_point}' non è presente nel genoma."
        )

    insertion_index = insertion_point_index + len(insertion_point)

    return genome[:insertion_index] + insertion + genome[insertion_index:]


def edit_genome_sequence(
    genome: str,
    insertion_points: list[str],
    insertions: list[str],
) -> str:

    validate_genetic_sequence(genome, "genome")

    if len(insertion_points) != len(insertions):
        raise InvalidEditSequenceError(
            "La lista degli insertion point e la lista delle insertion "
            "devono avere la stessa lunghezza."
        )

    edited_genome = genome
    insertion_counter: dict[str, int] = {}

    for insertion_point, insertion in zip(insertion_points, insertions):
        validate_genetic_sequence(insertion_point, "insertion_point")
        validate_genetic_sequence(insertion, "insertion")

        insertion_counter[insertion] = insertion_counter.get(insertion, 0) + 1
        replicated_insertion = insertion * insertion_counter[insertion]

        edited_genome = edit_genome(
            edited_genome,
            insertion_point,
            replicated_insertion,
        )

    return edited_genome


def find_last_valid_edit_index(
    genome: str,
    insertion_point: str,
    insertion: str,
) -> int:

    search_start_index = len(genome)
    insertion_point_found_at_least_once = False

    while True:
        insertion_point_index = genome.rfind(
            insertion_point,
            0,
            search_start_index,
        )

        if insertion_point_index == -1:
            if insertion_point_found_at_least_once:
                # L'insertion point esiste nel genoma, ma nessuna delle sue
                # occorrenze è seguita dall'insertion da rimuovere: il
                # problema è l'insertion, non l'insertion point.
                raise InvalidInsertionError(
                    f"L'insertion point '{insertion_point}' è presente nel "
                    f"genoma, ma non è mai seguito dall'insertion "
                    f"'{insertion}' da rimuovere."
                )
            raise InvalidInsertionPointError(
                f"L'insertion point '{insertion_point}' non è presente nel "
                "genoma."
            )

        insertion_point_found_at_least_once = True

        insertion_index = insertion_point_index + len(insertion_point)
        possible_insertion = genome[
            insertion_index : insertion_index + len(insertion)
        ]

        if possible_insertion == insertion:
            return insertion_index

        search_start_index = insertion_point_index


def undo_genome_edit(
    genome: str,
    insertion_point: str,
    insertion: str,
) -> str:

    validate_genetic_sequence(genome, "genome")
    validate_genetic_sequence(insertion_point, "insertion_point")
    validate_genetic_sequence(insertion, "insertion")

    insertion_index = find_last_valid_edit_index(
        genome,
        insertion_point,
        insertion,
    )

    return (
        genome[:insertion_index]
        + genome[insertion_index + len(insertion) :]
    )


def undo_genome_edit_sequence(
    genome: str,
    insertion_points: list[str],
    insertions: list[str],
    strict: bool = False,
) -> str:

    validate_genetic_sequence(genome, "genome")

    if len(insertion_points) != len(insertions):
        raise InvalidEditSequenceError(

        )

    edited_genome = genome
    insertion_counter: dict[str, int] = {}

    for step, (insertion_point, insertion) in enumerate(
        zip(insertion_points, insertions)
    ):
        try:
            validate_genetic_sequence(insertion_point, "insertion_point")
            validate_genetic_sequence(insertion, "insertion")

            insertion_counter[insertion] = insertion_counter.get(insertion, 0) + 1
            replicated_insertion = insertion * insertion_counter[insertion]

            edited_genome = undo_genome_edit(
                edited_genome,
                insertion_point,
                replicated_insertion,
            )

        except (
            InvalidInsertionPointError,
            InvalidInsertionError,
        ) as error:
            if strict:
                raise
            logger.warning(
                "undo_genome_edit_sequence interrotta allo step %d "
                "(insertion_point=%r, insertion=%r): %s",
                step,
                insertion_point,
                insertion,
                error,
            )
            break

    return edited_genome