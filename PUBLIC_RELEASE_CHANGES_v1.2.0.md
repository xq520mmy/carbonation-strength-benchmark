# Public release correction record: v1.2.0

`v1.2.0` succeeds `v1.1.0` without altering any historical release asset. It carries forward the v1.0.0 public-redaction policy and the v1.1.0 schema-sensitivity update.

The correction reclassifies two retained records (`EXT-0209`, `EXT-0210`) as explicit ambient-pressure carbonation records under the pre-existing 0.1-MPa convention. It updates the redacted row/source audit CSVs, the two primary-cohort rerun JSON files, the corrected DCE Figures 1 and 4, the Figure 5 external decision comparison, and the dependent schema/input-range diagnostics. It adds the corrected versioned density-sensitivity v2 outputs and removes the ambiguous unversioned density outputs derived from the earlier 39-record cohort. The correction adds a public, non-verbatim audit note. It does not change training data, model code, hyperparameters, seeds, fitted models, stored predictions, strict cohort, or legacy cohorts.

`CORRECTION_PROVENANCE_v1.2.0.json` records the reviewed local and public SHA-256 digests. `source/MANIFEST_SHA256.json` covers every source file in this archive.
