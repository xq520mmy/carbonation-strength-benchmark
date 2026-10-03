# Verified access to the historical training workbook

The original dataset is deposited by **suhaib wani** as *Compressive Strength
of CO₂-Cured Concrete*, Mendeley Data, version 1 (9 March 2026),
DOI [10.17632/2myr3k8n4g.1](https://data.mendeley.com/datasets/2myr3k8n4g/1).
The official record labels the dataset **CC BY 4.0**. Preserve this attribution
and consult the [license](https://creativecommons.org/licenses/by/4.0/).

The listed `1-s2.0-S2214509525003870-mmc1.xlsx` file was downloaded on 2 October
2026. All 2,376 cells and all 12 column names match the historical workbook
used in this benchmark. The files themselves are byte-identical:

    f9e9e195e680d39ea89ebcaf9c50dbf90118c47dc63afcb675f22f7feb9b406b

This supplies a citable, licensed access route. It supplies no new specimens,
new laboratory, independently measured density, or external validation.
The provider's assertions of cleaning and source completeness are its own
description; this benchmark's provenance and duplicate findings are unchanged.

## Refit preparation

After verifying and extracting the existing `v1.2.0` numerical archive, use
the repository's helper, with Python's standard library:

```sh
python fetch_training_workbook.py --source-dir carbonation-strength-benchmark-v1.2.0/source --download
```

The helper contacts only the official public file URL, checks the frozen
SHA-256, and installs the workbook at the original reader's expected path.
It never uploads local files or overwrites an existing workbook. Omitting
`--download` only validates an already present file. A changed provider file
stops the operation instead of silently changing the benchmark.

Use the source archive's `requirements-frozen.txt` for the model environment.
The helper obtains one training workbook; it does not obtain third-party
full texts or TabPFN weights, and it does not establish their reuse rights.
Metric checking from saved predictions still needs no workbook or model fit.

## Version boundary

`v1.2.0` and its archive remain immutable. The repository update adds this
access note and helper beside that archive; it changes no model, metric,
cohort, input row or historical prediction. The original 198-row workbook
is obtained from the provider rather than copied into the code repository.
