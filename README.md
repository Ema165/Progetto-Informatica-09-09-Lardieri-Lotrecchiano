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

Il programma segue queste regole:

* il genoma può contenere solamente le basi `A`, `C`, `G` e `T`;
* un edit singolo modifica l'ultima occorrenza dell'insertion point;
* negli edit multipli, ogni modifica viene eseguita sul risultato della modifica precedente;
* se la stessa insertion compare più volte, viene replicata in base al numero delle sue occorrenze;
* nell'annullamento multiplo, le rimozioni vengono eseguite nell'ordine inserito dall'utente;
* se una rimozione non può essere effettuata, l'operazione si interrompe e restituisce errore.

Le sequenze inserite in minuscolo vengono automaticamente convertite in maiuscolo, mentre gli spazi all'inizio e alla fine vengono rimossi.

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

## Stile del codice

Il progetto è organizzato in più moduli per mantenere il codice più ordinato e leggibile.

Sono stati utilizzati:

* nomi in `snake_case` per funzioni e variabili;
* nomi in `CamelCase` per le classi di eccezione;
* type hint per parametri e valori restituiti;
* docstring per le funzioni principali.

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
