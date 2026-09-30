# Carbonation-strength benchmark v1.2.0

The current reproducibility archive is `carbonation-strength-benchmark-v1.2.0.tar.xz` in this repository. Version `v1.2.0` corrects two source records to explicit ambient-pressure carbonation under the unchanged 0.1-MPa convention. The primary mixed-age cohort now contains 41 records from five reports and four author-merged clusters, including seven 28-day observations. The model, training data, seed predictions and strict cohort were not changed. The older `v1.1.0` archive remains in this repository as an immutable historical record; its 39-row primary results are superseded. See `PUBLIC_RELEASE_CHANGES_v1.2.0.md` and `CORRECTION_PROVENANCE_v1.2.0.json`.

Terminology clarification: the archive's introductory README uses "four laboratory clusters" for the four author-merged source clusters. This is an operational grouping for the sensitivity analysis; it does not establish four independent laboratories or independence from all training sources. The `lab_key` field must be read in that limited sense. The archived files and version tag remain unchanged; this clarification changes no cohort membership, prediction or numerical result.

## Verify and extract

Compare the downloaded archive with its entry in `SHA256SUMS.txt`, then run:

```sh
python unpack.py carbonation-strength-benchmark-v1.2.0.tar.xz --sha256 32fa49a39ace81dc043aa6c3e7abac09e2939be6cf5414e3ad9094e11e5f4d61
cd carbonation-strength-benchmark-v1.2.0/source
python _shared/revision_20260921/C1/verify_reproduction_outputs.py
python _shared/revision_20260921/C1/schema_alignment_sensitivity.py
```

These checks recalculate numerical results from frozen predictions; they do not refit a model. Full refitting requires the separate publisher workbook and a compatible environment. The archive excludes that workbook, article full texts and quoted passages from source literature. Its 100-file source manifest documents the included shareable materials. The separate source-deletion and train-only lookup submission addenda are not part of this repository. No archival DOI or new software license is claimed; reuse requires checking the applicable permissions and `THIRD_PARTY_NOTICES.md`.
