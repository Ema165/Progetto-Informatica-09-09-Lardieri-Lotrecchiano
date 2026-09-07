# Genetic Editing Project

Progetto Python per simulare operazioni di editing genetico su sequenze di DNA composte dalle basi `A`, `C`, `G` e `T`.

Il programma è interattivo: i dati vengono inseriti dall'utente direttamente dal terminale e non sono presenti sequenze preimpostate nel codice.

## Struttura del progetto

```text
.
├── README.md
├── main.py
├── genetic_editor.py
└── exceptions.py
```

## Avvio

Per avviare il programma è sufficiente aprire il terminale nella cartella del progetto ed eseguire:

```bash
python main.py
```

Dopo l'avvio viene mostrato un menu dal quale è possibile scegliere l'operazione da eseguire:

```text
1 - Edit singolo
2 - Edit multipli
3 - Annulla un edit
4 - Annulla più edit
```

In base all'operazione scelta, il programma richiede all'utente le sequenze necessarie, come il genoma, l'insertion point e l'insertion.

## Funzionamento

1) Main.py
l file main.py rappresenta il punto di ingresso del programma, in cui vengono richiamate ed eseguite le funzioni precedentemente definite, coordinandone il flusso di esecuzione.

2) Genetic_editor.py
Contiene la logica principale del progetto.

Funzioni principali:

-Validate_genetic_sequence(sequence, sequence_name)
Controlla che una sequenza genetica sia valida.  
Una sequenza è valida se:
- è una stringa;
- contiene solo caratteri appartenenti all'alfabeto genomico A, C, G, T.

-Edit_genome(genome, insertion_point, insertion)
 Esegue un singolo edit genetico.L'insertion viene inserita subito dopo l'ultimo insertion point presente
 nel genoma. Se l'insertion point compare più volte, viene usata solo
 l'ultima occorrenza.

-Edit_genome_sequence(genome, insertion_points, insertions)
 Esegue più edit consecutivi, considerando le repliche delle insertion. Gli edit vengono applicati in ordine. Ogni edit modifica il genoma, quindi gli edit successivi lavorano sul genoma già modificato.

-Find_last_valid_edit_index
Cerca l'ultimo punto valido in cui una insertion può essere rimossa.Un punto è valido se nel genoma è presente un insertion point seguito immediatamente dalla insertion da rimuovere.

-Undo_genome_edit(genome, insertion_point, insertion)
 Annulla un singolo edit.La funzione rimuove una sola occorrenza dell'insertion, cercandola subito dopo l'ultimo insertion point valido.

-Undo_genome_edit_sequence(genome, insertion_points, insertions)
 Annulla una sequenza di edit, fermandosi se una rimozione non è valida, le rimozioni vengono tentate in ordine.

3)Exceptions.py
Contiene le eccezioni personalizzate del progetto:

-GeneticEditingError: Eccezione base per tutti gli errori legati all'editing genetico.

-InvalidGenomeError:Sollevata quando una sequenza genomica contiene caratteri non validi oppure è vuota.

-InvalidInsertionPointError:Sollevata quando un insertion point è vuoto, non valido,oppure non è presente nel genoma.

-InvalidInsertionError: Sollevata quando una insertion è vuota o contiene caratteri non validi.

-InvalidEditSequenceError:Sollevata quando una sequenza di insertion point e insertion non è coerente, per esempio se le due liste hanno lunghezze diverse.

Servono a rendere più chiara la gestione degli errori.

## Controlli

Il programma gestisce anche alcuni casi particolari, tra cui:

* genoma vuoto;
* insertion vuota;
* insertion point vuoto;
* caratteri non validi;
* insertion point non presente nel genoma;
* numero di edit non valido;
* rimozioni non valide.

Gli errori vengono gestiti tramite eccezioni definite nel file `exceptions.py`.

## Esempio

Un possibile utilizzo del programma è:

```text
=== Genetic Editing Project ===
1 - Edit singolo
2 - Edit multipli
3 - Annulla un edit
4 - Annulla più edit

Scegli un'opzione: 1

--- Edit singolo ---
Inserisci il genoma: ACCTGCAACTGC
Inserisci l'insertion point: CT
Inserisci l'insertion: GGGTGGG

Genoma modificato
-----------------
ACCTGCAACTGGGTGGGC
```

L'esempio è puramente dimostrativo. Il programma permette di inserire qualsiasi sequenza valida composta dalle basi `A`, `C`, `G` e `T`.
