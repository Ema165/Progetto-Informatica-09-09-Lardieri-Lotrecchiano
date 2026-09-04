# Progetto-Esame-info-13-07-Lardieri-Lotrecchiano
 Genetic Editing Project

Il progetto permette di:

- modificare un genoma con un singolo edit;
- modificare un genoma con più edit consecutivi;
- gestire insertion ripetute tramite repliche;
- annullare un singolo edit;
- annullare una sequenza di edit;
- validare genomi, insertion point e insertion;
- gestire casi limite ed errori.


Struttura del progetto

genetic_editing_project/
├── README.md
├── main.py 
├── genetic_editor.py
└── exceptions.py


Descrizione dei file:


 1)Main.py

Contiene gli esempi di utilizzo del progetto.
Mostra tutte le funzionalità richieste:
- edit singolo;
- edit multiplo;
- undo singolo;
- undo multiplo;
- gestione delle repliche;
- gestione di sequenze non valide;
- gestione di insertion point assenti;
- interruzione dell'undo multiplo in caso di rimozione non valida.


2)Genetic_editor.py
Contiene la logica principale del progetto.

Funzioni principali:

-Validate_genetic_sequence(sequence, sequence_name)
Controlla che una sequenza genetica sia valida.  
Una sequenza è valida se:
- è una stringa;
- non è vuota;
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


Parte A

1)Edit singolo
Dato un genoma, un insertion point e una insertion, la insertion viene inserita subito dopo l'ultimo insertion point presente nel genoma.

Esempio:
genome = "ACCTGCAACTGC"
insertion_point = "CT"
insertion = "GGGTGGG"

Risultato:
ACCTGCAACTGGGTGGGGC


2)Edit multiplo
Gli edit vengono applicati in ordine.
Ogni edit modifica il genoma, quindi l'edit successivo lavora sul genoma già modificato.

Esempio:
genome = "ACCGCAACGC"
insertion_points = ["CG", "GC", "AA", "TT"]
insertions = ["TT", "C", "TT", "GGG"]

Risultato finale:
ACCGCCAATTTTCGTTGGGC


3)Repliche
Se una stessa insertion compare più volte:
- alla prima occorrenza viene inserita 1 volta;
- alla seconda occorrenza viene inserita 2 volte;
- alla terza occorrenza viene inserita 3 volte;
- e così via.

Esempio:
insertions = ["TT", "C", "TT", "GGG"]
La insertion `"TT"` compare due volte:
- primo inserimento: `"TT"`;
- secondo inserimento: `"TTTT"`.



Parte B

1)Undo singolo
Rimuove una sola insertion dal genoma.
La rimozione avviene subito dopo l'ultimo insertion point valido.

Esempio:
genome = "ACCTGCAACTGGGTGGGGC"
insertion_point = "CT"
insertion = "GGGTGGG"

Risultato:
ACCTGCAACTGC


2)Undo multiplo
Rimuove più insertion in sequenza.
Anche nell'undo valgono le repliche:
- alla prima occorrenza di una insertion si tenta di rimuoverla 1 volta;
- alla seconda occorrenza si tenta di rimuoverla 2 volte;
- alla terza occorrenza si tenta di rimuoverla 3 volte;
- e così via.
Se una rimozione non è valida, l'undo multiplo si interrompe subito.
Le rimozioni successive non vengono eseguite.


Validazione
Sono considerate valide solo sequenze:
- di tipo `str`;
- non vuote;
- composte solo da `A`, `C`, `G`, `T`.

Esempi validi:
ACGT
AACCGGTT
TTTAAA

Esempi non validi:
ACCTX
123
