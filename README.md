# Carbonation-strength benchmark v1.0.0

This GitHub release deliberately publishes seven files only: this README, `THIRD_PARTY_NOTICES.md`, `PUBLIC_RELEASE_CHANGES.md`, `PUBLIC_RELEASE_ORIGINAL_SHA256.json`, `unpack.py`, `SHA256SUMS.txt`, and `carbonation-strength-benchmark-v1.0.0.tar.xz`. The complete numerical reproducibility package is inside the compressed archive; there is no `source/` directory in the repository checkout. The fixed release identifier is **`v1.0.0`**. No DOI is asserted for this package.

The archive preserves code, figures, numerical outputs, DOI/page locations, cohort decisions, and concise author-derived notes needed to verify reported calculations. It does not redistribute the 198-row publisher spreadsheet, full-text source papers, or quoted passages from those papers.

## Verify and extract

First compare the downloaded files with `SHA256SUMS.txt`. Then extract the archive with the included standard-library helper; substitute the archive digest listed in `SHA256SUMS.txt`:

```sh
python unpack.py carbonation-strength-benchmark-v1.0.0.tar.xz --sha256 <archive-sha256>
```

The complete package is extracted to `carbonation-strength-benchmark-v1.0.0/source/`. From that directory, run the supplied verifier with a compatible frozen project environment:

```sh
cd carbonation-strength-benchmark-v1.0.0/source
PY=/path/to/C1_crossdb_audit/model_experiments/.venv/bin/python
"$PY" _shared/revision_20260921/C1/verify_reproduction_outputs.py
```

The verifier recomputes reported external metrics from retained per-row seed predictions. It does not refit a model or access the web. A successful run prints `"passed": true`.

Figures 1–3 can be regenerated from retained numerical results after extraction:

```sh
python C1_crossdb_audit/manuscript/make_figures.py --internal-only
```

Refitting requires separately obtaining the omitted publisher spreadsheet and any model weights under their respective terms. The extracted package README identifies those requirements.

## Public-release redactions and third-party material

The public derivative removes literature verbatim from `evidence` and `pressure_excerpt` fields, and replaces long source-derived unit notes with a redaction marker. DOI/page locations, numerical columns, cohort flags, pressure statuses, and concise author-derived notes remain. `PUBLIC_RELEASE_CHANGES.md` and `PUBLIC_RELEASE_ORIGINAL_SHA256.json` give the transformation counts and original-to-public SHA-256 mapping.

The UCI Concrete Compressive Strength CSV is retained for transfer pretraining only. `THIRD_PARTY_NOTICES.md` provides Yeh (1998), UCI dataset ID 165, DOI `10.24432/C5PK67`, the CC BY 4.0 link, and the CSV conversion note.

No new license is granted for this repository or release archive. Reuse requires determining the applicable permissions for the code and each included dataset.
