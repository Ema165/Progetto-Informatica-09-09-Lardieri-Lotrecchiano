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

### 1. `main.py`

Il file `main.py` rappresenta il **punto di ingresso del programma**, nel quale vengono richiamate ed eseguite le funzioni precedentemente definite, coordinandone il flusso di esecuzione.

---

### 2. `genetic_editor.py`

Il file `genetic_editor.py` contiene la **logica principale del progetto** e le funzioni necessarie per la gestione e la modifica delle sequenze genomiche.

#### Funzioni principali

**`validate_genetic_sequence(sequence, sequence_name)`**
Controlla che una sequenza genetica sia valida. Una sequenza è considerata valida se:

* è una stringa;
* contiene esclusivamente caratteri appartenenti all'alfabeto genomico `A, C, G, T`.

**`edit_genome(genome, insertion_point, insertion)`**
Esegue un singolo editing genetico. L'`insertion` viene inserita subito dopo l'ultima occorrenza di `insertion_point` presente nel genoma. Se l'`insertion_point` compare più volte, viene utilizzata esclusivamente l'ultima occorrenza.

**`edit_genome_sequence(genome, insertion_points, insertions)`**
Esegue una sequenza di editing consecutivi, considerando le eventuali ripetizioni degli `insertion point`. Gli edit vengono applicati nell'ordine specificato. Ogni modifica aggiorna il genoma, pertanto gli edit successivi operano sul genoma già modificato.

**`find_last_valid_edit_index(...)`**
Individua l'ultimo punto valido in cui è possibile rimuovere un'insertion. Un punto viene considerato valido quando nel genoma è presente un `insertion_point` seguito immediatamente dall'`insertion` da rimuovere.

**`undo_genome_edit(genome, insertion_point, insertion)`**
Annulla un singolo edit. La funzione rimuove una sola occorrenza dell'`insertion`, cercandola immediatamente dopo l'ultimo `insertion_point` valido.

**`undo_genome_edit_sequence(genome, insertion_points, insertions)`**
Annulla una sequenza di edit. Le rimozioni vengono tentate nell'ordine specificato e l'operazione si interrompe nel caso in cui una delle rimozioni non risulti valida.

---

### 3. `exceptions.py`

Il file `exceptions.py` contiene le **eccezioni personalizzate del progetto**, utilizzate per rendere più chiara e strutturata la gestione degli errori.

#### Eccezioni principali

**`GeneticEditingError`**
Eccezione base dalla quale derivano tutti gli errori relativi alle operazioni di editing genetico.

**`InvalidGenomeError`**
Viene sollevata quando una sequenza genomica è vuota oppure contiene caratteri non validi.

**`InvalidInsertionPointError`**
Viene sollevata quando un `insertion_point` è vuoto, non valido oppure non è presente nel genoma.

**`InvalidInsertionError`**
Viene sollevata quando un'`insertion` è vuota oppure contiene caratteri non validi.

**`InvalidEditSequenceError`**
Viene sollevata quando una sequenza di `insertion point` e `insertion` non è coerente, ad esempio quando le due liste hanno lunghezze differenti.


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
