from exceptions import GeneticEditingError
from genetic_editor import (
    edit_genome,
    edit_genome_sequence,
    undo_genome_edit,
    undo_genome_edit_sequence,
)
def ask_sequence(message: str) -> str:
    """Chiede all'utente una sequenza e rimuove gli spazi iniziali e finali."""
    return input(message).strip().upper()
def show_result(title: str, result: str) -> None:
    print(f"\n{title}")
    print("-" * len(title))
    print(result)
def ask_edit_lists() -> tuple[list[str], list[str]]:
    """Chiede all'utente gli insertion point e le insertion da usare."""
    number = int(input("Quanti edit vuoi eseguire? "))
    insertion_points = []
    insertions = []
    for index in range(number):
        print(f"\nEdit {index + 1}")
        insertion_points.append(ask_sequence("Insertion point: "))
        insertions.append(ask_sequence("Insertion: "))
    return insertion_points, insertions
def run_single_edit() -> None:
    print("\n--- Edit singolo ---")
    genome = ask_sequence("Inserisci il genoma: ")
    insertion_point = ask_sequence("Inserisci l'insertion point: ")
    insertion = ask_sequence("Inserisci l'insertion: ")
    result = edit_genome(genome, insertion_point, insertion)
    show_result("Genoma modificato", result)
def run_multiple_edits() -> None:
    print("\n--- Edit multipli ---")
    genome = ask_sequence("Inserisci il genoma: ")
    insertion_points, insertions = ask_edit_lists()
    result = edit_genome_sequence(genome, insertion_points, insertions)
    show_result("Genoma modificato", result)
def run_single_undo() -> None:
    print("\n--- Annullamento di un edit ---")
    genome = ask_sequence("Inserisci il genoma modificato: ")
    insertion_point = ask_sequence("Inserisci l'insertion point: ")
    insertion = ask_sequence("Inserisci l'insertion da rimuovere: ")
    result = undo_genome_edit(genome, insertion_point, insertion)
    show_result("Genoma dopo l'annullamento", result)
def run_multiple_undo() -> None:
    print("\n--- Annullamento di più edit ---")
    genome = ask_sequence("Inserisci il genoma modificato: ")
    insertion_points, insertions = ask_edit_lists()
    result = undo_genome_edit_sequence(
        genome,
        insertion_points,
        insertions,
    )
    show_result("Genoma dopo gli annullamenti", result)
def main() -> None:
    print("=== Genetic Editing Project ===")
    print("1 - Edit singolo")
    print("2 - Edit multipli")
    print("3 - Annulla un edit")
    print("4 - Annulla più edit")
    choice = input("Scegli un'opzione: ").strip()
    try:
        if choice == "1":
            run_single_edit()
        elif choice == "2":
            run_multiple_edits()
        elif choice == "3":
            run_single_undo()
        elif choice == "4":
            run_multiple_undo()
        else:
            print("Opzione non valida.")
    except (GeneticEditingError, TypeError, ValueError) as error:
        print(f"\nErrore gestito: {error}")
if __name__ == "__main__":
    main()
