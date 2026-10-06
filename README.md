# Carbonation-strength benchmark v1.3.0

Version `v1.3.0` adds the bounded publication-lineage and exact-row audit completed on 5 October 2026. The earlier cohort benchmark `v1.2.0` and all older archive bytes remain unchanged. This additive version contains the new audit in `c1-lineage-twin-audit-20261005.tar.xz`; it does not claim new physical validation, an archival DOI, or a new blanket software license.

## New lineage and exact-row audit

The new bundle preserves 42 historical files, 55 total payload files, all 2,200 saved prediction groups, 600 frozen split definitions, 800 fixed-Test stratum rows and all 50 seeds. It records 33 size-two exact-row groups and source-bound equality of 2,376 numeric cells. The identified broad frame bounds distinct complete compilations at six to seven; independent physical-origin K remains unknown. Grouped splits with R² ≥ 0.95 and all adverse results are retained.

Verify the archive checksum before extraction:

```sh
python unpack.py c1-lineage-twin-audit-20261005.tar.xz --sha256 79cc3c135177a61d5a4e5d61fce1aba0b751e2a9d12d2d5fcfb647c3f17d38c2
cd c1-lineage-twin-audit-20261005
python tools/verify_saved_results.py
```

The verifier recomputes saved metrics without fitting. With lawful local copies of the separate provider and Chu workbooks, use the opt-in input adapter and `--bind-workbooks` instructions inside the bundle for source-byte and seven-input identity checks. No workbook, publisher PDF/HTML, long quotation, model, environment, contact record or private conversation is included.

The bundle's inner README records its prepublication staging status; this repository wrapper and `LINEAGE_AUDIT_PROVENANCE_v1.3.0.json` identify the later additive publication. Original code, seals and saved scientific outputs were not changed to hide failures. The original strict stratum-summary equality check has six Python-runtime SD discrepancies of at most 2.22×10⁻¹⁶. A separately identified independent verifier passes every saved cell at an explicit 10⁻¹² absolute tolerance. The actual QA environment differs from the original frozen Python/NumPy environment; no refit-equivalence claim is made. See `PORTABILITY_NOTES.md` inside the bundle and `PUBLIC_RELEASE_CHANGES_v1.3.0.md`.

## Earlier cohort benchmark

The earlier cohort reproducibility archive is `carbonation-strength-benchmark-v1.2.0.tar.xz` in this repository. Version `v1.2.0` corrects two source records to explicit ambient-pressure carbonation under the unchanged 0.1-MPa convention. The primary mixed-age cohort now contains 41 records from five reports and four author-merged clusters, including seven 28-day observations. The model, training data, seed predictions and strict cohort were not changed. The older `v1.1.0` archive remains in this repository as an immutable historical record; its 39-row primary results are superseded. See `PUBLIC_RELEASE_CHANGES_v1.2.0.md` and `CORRECTION_PROVENANCE_v1.2.0.json`.

Terminology clarification: the archive's introductory README uses "four laboratory clusters" for the four author-merged source clusters. This is an operational grouping for the sensitivity analysis; it does not establish four independent laboratories or independence from all training sources. The `lab_key` field must be read in that limited sense. The archived files and version tag remain unchanged; this clarification changes no cohort membership, prediction or numerical result.

## Verify and extract

Compare the downloaded archive with its entry in `SHA256SUMS.txt`, then run:

```sh
python unpack.py carbonation-strength-benchmark-v1.2.0.tar.xz --sha256 32fa49a39ace81dc043aa6c3e7abac09e2939be6cf5414e3ad9094e11e5f4d61
cd carbonation-strength-benchmark-v1.2.0/source
python _shared/revision_20260921/C1/verify_reproduction_outputs.py
python _shared/revision_20260921/C1/schema_alignment_sensitivity.py
```

These checks recalculate numerical results from frozen predictions; they do not refit a model. Full refitting requires the separate training workbook and a compatible environment. The official Mendeley Data deposit [10.17632/2myr3k8n4g.1](https://data.mendeley.com/datasets/2myr3k8n4g/1) labels the workbook CC BY 4.0; the file has been downloaded and verified byte-identical to the historical input. See `DATA_ACCESS_20261002.md` for attribution and use `fetch_training_workbook.py` to obtain and verify it at the expected refitting path. This is the same 198-row dataset, not new external validation.

The archive excludes that workbook, article full texts and quoted passages from source literature. Its 100-file source manifest documents the included shareable materials. The separate source-deletion and train-only lookup submission addenda are not part of this repository. No archival DOI or new software license is claimed for this code package; the provider's dataset has its own DOI and license. Reuse requires checking the applicable permissions and `THIRD_PARTY_NOTICES.md`.
