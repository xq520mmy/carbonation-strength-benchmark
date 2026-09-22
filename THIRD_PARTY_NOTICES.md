# Third-party notices

## UCI Concrete Compressive Strength dataset

`source/C1_crossdb_audit/model_experiments/data/uci_concrete.csv` is a CSV-form conversion of the UCI Machine Learning Repository **Concrete Compressive Strength** dataset. It is retained only for transfer pretraining in the supplied scripts and is not used to evaluate the carbonation-strength benchmark.

- Dataset: Yeh, I.-C. (1998), *Concrete Compressive Strength*.
- UCI dataset page: <https://archive.ics.uci.edu/dataset/165/concrete+compressive+strength>
- Dataset DOI: <https://doi.org/10.24432/C5PK67>
- License: [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/)

The release stores a comma-delimited CSV representation of the nine UCI tabular fields so that the existing Python readers can load it directly. It retains the held 1,030 rows and field order; it does not create new observations, labels, or splits.

Other cited source literature and the 198-row publisher spreadsheet are not redistributed. Their identifiers and retained locations are provided only to support independent, lawful source access.
