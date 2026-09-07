from exceptions import (
    InvalidEditSequenceError,
    InvalidGenomeError,
    InvalidInsertionError,
    InvalidInsertionPointError,
)
GENOMIC_ALPHABET = {"A", "C", "G", "T"}
def validate_genetic_sequence(sequence: str, sequence_name: str) -> None:
    if not isinstance(sequence, str):
        raise TypeError(f"{sequence_name} deve essere una stringa.")
    if not sequence:
        if sequence_name == "genome":
            raise InvalidGenomeError("Il genoma non può essere vuoto.")
        if sequence_name == "insertion":
            raise InvalidInsertionError("L'insertion non può essere vuota.")
        raise InvalidInsertionPointError("L'insertion point non può essere vuoto.")
    invalid_bases = set(sequence) - GENOMIC_ALPHABET
    if not invalid_bases:
        return
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
    point_index = genome.rfind(insertion_point)
    if point_index == -1:
        raise InvalidInsertionPointError(
            f"L'insertion point '{insertion_point}' non è presente nel genoma."
        )
    insertion_index = point_index + len(insertion_point)
    return genome[:insertion_index] + insertion + genome[insertion_index:]
def edit_genome_sequence(
    genome: str,
    insertion_points: list[str],
    insertions: list[str],
) -> str:
    validate_genetic_sequence(genome, "genome")
    if len(insertion_points) != len(insertions):
        raise InvalidEditSequenceError()
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
    search_end = len(genome)
    point_found = False
    while True:
        point_index = genome.rfind(insertion_point, 0, search_end)
        if point_index == -1:
            if point_found:
                raise InvalidInsertionError(
                    f"L'insertion point '{insertion_point}' è presente nel "
                    f"genoma, ma non è mai seguito dall'insertion "
                    f"'{insertion}' da rimuovere."
                )
            raise InvalidInsertionPointError(
                f"L'insertion point '{insertion_point}' non è presente nel genoma."
            )
        point_found = True
        insertion_index = point_index + len(insertion_point)
        following_text = genome[
            insertion_index : insertion_index + len(insertion)
        ]
        if following_text == insertion:
            return insertion_index
        search_end = point_index
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
    return genome[:insertion_index] + genome[insertion_index + len(insertion):]
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
    for step, (insertion_point, insertion) in (
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
        except (InvalidInsertionPointError, InvalidInsertionError) as error:
            if strict:
                raise
           print(f"undo_genome_edit_sequence interrotta allo step {step}: {error}")
            break
    return edited_genome
