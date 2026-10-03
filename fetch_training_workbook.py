#!/usr/bin/env python3
"""Fetch and hash-check the cited, CC BY 4.0 third-party 198-row workbook.

Only the official public data URL is contacted. No local data are uploaded.
Existing files are never overwritten. The historical numerical archive is
unchanged. Run with --download to permit an inbound network transfer.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import tempfile
import urllib.request

URL = "https://data.mendeley.com/public-files/datasets/2myr3k8n4g/files/3bdf2537-862a-46b0-9b57-367921bd1568/file_downloaded"
DOI = "10.17632/2myr3k8n4g.1"
SHA256 = "f9e9e195e680d39ea89ebcaf9c50dbf90118c47dc63afcb675f22f7feb9b406b"
MAX_BYTES = 2_000_000

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def install_checked(temp_path, target):
    """Validate before installation; exclusive creation prevents overwrites."""
    if digest(temp_path) != SHA256:
        raise ValueError("Provider file differs from the frozen workbook; stop without installing.")
    target=Path(target)
    with target.open("xb") as out:
        out.write(Path(temp_path).read_bytes())

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True,
                        help="Extracted archive's source directory (contains C1_crossdb_audit).")
    parser.add_argument("--download", action="store_true", help="Allow downloading the official public file.")
    args=parser.parse_args()
    source=args.source_dir.resolve()
    if not (source / "C1_crossdb_audit/model_experiments/common.py").is_file():
        parser.error("--source-dir must identify the extracted benchmark source directory.")
    target=source / "C1_crossdb_audit/probe/data/scirep_MOESM1.xlsx"
    if target.exists():
        if digest(target)!=SHA256:
            raise ValueError("Existing workbook has a different hash; it was not modified.")
        status="existing_verified"
    else:
        if not args.download: parser.error("Workbook absent. Use --download to authorize the inbound transfer.")
        target.parent.mkdir(parents=True, exist_ok=True)
        temp_path=None
        try:
            with tempfile.NamedTemporaryFile(dir=target.parent, prefix=".workbook-",delete=False) as out:
                temp_path=Path(out.name)
                request=urllib.request.Request(URL,headers={"User-Agent":"carbonation-strength-benchmark-data-fetch/1.0"})
                with urllib.request.urlopen(request, timeout=45) as response:
                    total=0
                    while chunk:=response.read(65536):
                        total+=len(chunk)
                        if total>MAX_BYTES: raise ValueError("Download exceeded the size bound; not installed.")
                        out.write(chunk)
            install_checked(temp_path,target)
            status="downloaded_verified"
        finally:
            if temp_path is not None: temp_path.unlink(missing_ok=True)
    print(json.dumps({"status":status,"path":str(target),"sha256":SHA256,
                      "provider_doi":DOI,"provider_license":"CC BY 4.0",
                      "attribution":"wani, suhaib (2026), Compressive Strength of CO2-Cured Concrete, Mendeley Data, V1",
                      "identity":"Same historical 198 rows, not independent validation."},indent=2))

if __name__=="__main__": main()
