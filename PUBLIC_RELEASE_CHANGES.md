# Public-release derivative record

This file documents the changes from the locally staged C1 reproducibility package to the public derivative identified as `v1.0.0`. It is an audit record, not a new license or a claim that a DOI has been minted.

## Content retained

The derivative retains all numerical feature and outcome columns, row identifiers, DOI fields, page/locator fields, source and laboratory identifiers, cohort/status flags, model predictions, seeds, scripts, figures, and concise author-derived unit/interpretation notes. The UCI pretraining CSV is retained under the notice in `THIRD_PARTY_NOTICES.md`.

## Literature-text redaction

The derivative removes these source-quotation fields:

- JSON object keys `evidence`, `column_decoding_evidence`, and `source_evidence`.
- The `evidence` column from `external_validation/extracted_data.csv`.
- The `pressure_excerpt` column from `pressure_audit_rows.csv` and `pressure_audit_sources.csv`.
- Long `unit_note` values that contain source-location markers; each is replaced by an explicit public-release redaction marker. Concise notes remain.
- The pressure-audit Markdown’s quoted source passage. Its DOI/location and non-verbatim audit explanation remain.

`PUBLIC_RELEASE_ORIGINAL_SHA256.json` records each modified source file’s pre-release and public SHA-256 values, the original manifest hash, and transformation counts. `source/MANIFEST_SHA256.json` was then regenerated over the public package contents.

## Verification scope

The public verifier recomputes reported external metrics from retained predictions and observed numeric outcomes. It does not depend on removed quotation fields, refit a model, retrieve literature, or modify original study inputs.
