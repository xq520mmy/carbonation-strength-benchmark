#!/usr/bin/env python3
"""Verify a SHA-256 checksum and safely extract a .tar.xz release archive."""
from __future__ import annotations
import argparse
import hashlib
from pathlib import Path
import tarfile

p=argparse.ArgumentParser(description=__doc__)
p.add_argument('archive', type=Path)
p.add_argument('--sha256', required=True, help='expected SHA-256 digest')
p.add_argument('--output-dir', type=Path, default=Path('.'))
a=p.parse_args()

digest=hashlib.sha256(a.archive.read_bytes()).hexdigest()
if digest.lower()!=a.sha256.lower():
    raise SystemExit(f'SHA-256 mismatch: expected {a.sha256}, got {digest}')
root=a.output_dir.resolve()
with tarfile.open(a.archive, 'r:xz') as t:
    members=t.getmembers()
    for m in members:
        target=(root/m.name).resolve()
        if not target.is_relative_to(root):
            raise SystemExit(f'unsafe archive member: {m.name}')
        if m.issym() or m.islnk() or m.isdev():
            raise SystemExit(f'unsafe archive member type: {m.name}')
    t.extractall(root, members=members)
print(f'Verified {a.archive.name} ({digest}) and extracted to {root}')
