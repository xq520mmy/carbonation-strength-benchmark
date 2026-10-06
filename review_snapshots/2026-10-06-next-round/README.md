# C1 next-round numerical audit — 6 October 2026

This is an additive public GitHub snapshot of the independently checked numerical/code staging archive. The exact archive bytes and its original staging README are preserved. That inner status describes its creation, while this wrapper records the later repository snapshot; this is not a Zenodo record, archival DOI, new code licence or manuscript submission. All previous tags and archive bytes remain unchanged.

The ZIP contains 351 files and is 13,800,283 bytes, SHA256 `56bd9b01411b648c7730b2e4cba6ccf6d843afe8abfcb574989e53ff3097d54b`. It preserves the original 319-job frozen matrix, every 1,151 final saved-prediction cell, all 50-seed comparisons, 1,226 exact exposure expectations and partition-draw evidence. The complete revision has 2,044 tree fits (900 CV + 1,144 final) and seven separate final CPU TabPFN contexts; one training-only TabPFN smoke is discarded.

Extract to a new directory. From `c1-next-round-audit-20261006/`, run with Python 3.11+ (standard library only):

    python tools/verify_saved_revision.py --output /tmp/new-c1-numerical-replay.json
    python tools/exposure_cli.py --sizes 4 3 2 1 --test-n 3

An actual clean-extraction replay completed successfully with 110,302 checks. An independent implementation additionally checked 1,151 final cells, 100,123 prediction rows, the exposure expectations, all retained partition bands and tool cases. This verifies saved numerical arithmetic and file identity. It does not independently recover physical specimens or omitted raw-data equality.

The optional original-matrix refit wrapper requires lawful, exact-hash source data and frozen dependencies. It covers the original 319 jobs only; later source-guided GUI/source-held-out extensions and CPU TabPFN contexts are saved-result-only in that wrapper. Do not treat the archive as a turnkey refit of every extension.

Headline misses, grouped R² >= 0.95 outcomes, Yeh intervals crossing zero, reverse deletion effects and the post-outcome source-test extension remain. Numerically identical tables do not prove shared specimen identity or misconduct. The public subset has its own member manifest; original seals can bind private inputs deliberately absent from it and have not been rewritten.

No raw workbook/CSV inputs, publisher full texts, unlicensed third-party GUI code, private provenance, emails, author records, weights, adapters, environment or credentials are included. The included data-access metadata is an explicitly named projection with its own digest. Author-code licence selection remains pending; dataset/software/model permissions are separate. The manuscript and submission letters are not uploaded here.
