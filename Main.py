from exceptions import GeneticEditingError
from genetic_editor import (
    edit_genome,
    edit_genome_sequence,
    undo_genome_edit,
    undo_genome_edit_sequence,
)


def show_result(title: str, result: str) -> None:

    print(f"\n{title}")
    print("-" * len(title))
    print(result)


def show_error(title: str, error: Exception) -> None:

    print(f"\n{title}")
    print("-" * len(title))
    print(f"Errore gestito: {error}")


def run_single_edit_example() -> None:

    genome = "ACCTGCAACTGC"
    insertion_point = "CT"
    insertion = "GGGTGGG"

    edited_genome = edit_genome(genome, insertion_point, insertion)

    show_result("Parte A - Edit singolo", edited_genome)


def run_multiple_edit_example() -> None:

    genome = "ACCGCAACGC"
    insertion_points = ["CG", "GC", "AA", "TT"]
    insertions = ["TT", "C", "TT", "GGG"]

    edited_genome = edit_genome_sequence(
        genome,
        insertion_points,
        insertions,
    )

    show_result("Parte A - Edit multiplo con repliche", edited_genome)


def run_single_undo_example() -> None:

    genome = "ACCTGCAACTGGGTGGGGC"
    insertion_point = "CT"
    insertion = "GGGTGGG"

    restored_genome = undo_genome_edit(genome, insertion_point, insertion)

    show_result("Parte B - Undo singolo", restored_genome)


def run_multiple_undo_example() -> None:

    genome = "ACCGCCAATTTTCGTTGGGC"
    insertion_points = ["TT", "AA", "GC", "CG"]
    insertions = ["GGG", "TT", "C", "TT"]

    restored_genome = undo_genome_edit_sequence(
        genome,
        insertion_points,
        insertions,
    )

    show_result("Parte B - Undo multiplo con repliche", restored_genome)


def run_invalid_genome_example() -> None:

    genome = "ACCTX"
    insertion_point = "CT"
    insertion = "GGG"

    try:
        edit_genome(genome, insertion_point, insertion)
    except GeneticEditingError as error:
        show_error("Caso limite - Genoma non valido", error)


def run_missing_insertion_point_example() -> None:

    genome = "AACCGGTT"
    insertion_point = "AAA"
    insertion = "CG"

    try:
        edit_genome(genome, insertion_point, insertion)
    except GeneticEditingError as error:
        show_error("Caso limite - Insertion point assente", error)


def run_invalid_undo_sequence_example() -> None:

    genome = "ACCGCCAATTTTCGTTGGGC"
    insertion_points = ["TT", "AA", "GC"]
    insertions = ["AAA", "TT", "C"]

    restored_genome = undo_genome_edit_sequence(
        genome,
        insertion_points,
        insertions,
    )

    show_result(
        "Caso limite - Undo multiplo interrotto da richiesta non valida",
        restored_genome,
    )


def main() -> None:

    run_single_edit_example()
    run_multiple_edit_example()
    run_single_undo_example()
    run_multiple_undo_example()
    run_invalid_genome_example()
    run_missing_insertion_point_example()
    run_invalid_undo_sequence_example()


if __name__ == "__main__":
    main()