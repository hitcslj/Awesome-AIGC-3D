#!/usr/bin/env python3
"""Extract individual BibTeX entries from sample-base.bib into citations/ directory.

Usage:
    python scripts/extract_bib.py /path/to/sample-base.bib citations/

Each entry is written to citations/<key>.txt where <key> is the BibTeX citation key.
Existing files are skipped unless --overwrite is passed.
"""

import re
import sys
import os
from pathlib import Path


def parse_bib_entries(bib_text: str) -> dict[str, str]:
    """Parse a .bib file into {key: full_entry_text} pairs."""
    entries = {}
    # Match @type{key, ... } allowing nested braces
    pattern = re.compile(r'(@\w+\s*\{)', re.MULTILINE)
    positions = [(m.start(), m.group()) for m in pattern.finditer(bib_text)]

    for i, (start, header) in enumerate(positions):
        # Find the matching closing brace
        depth = 0
        end = start
        for j in range(start, len(bib_text)):
            if bib_text[j] == '{':
                depth += 1
            elif bib_text[j] == '}':
                depth -= 1
                if depth == 0:
                    end = j + 1
                    break

        entry_text = bib_text[start:end]

        # Extract the citation key
        key_match = re.match(r'@\w+\s*\{\s*([^,\s]+)', entry_text)
        if key_match:
            key = key_match.group(1).strip()
            entries[key] = entry_text

    return entries


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} <bib_file> <output_dir> [--overwrite]")
        sys.exit(1)

    bib_path = Path(sys.argv[1])
    out_dir = Path(sys.argv[2])
    overwrite = "--overwrite" in sys.argv

    if not bib_path.exists():
        print(f"Error: {bib_path} not found")
        sys.exit(1)

    out_dir.mkdir(parents=True, exist_ok=True)

    bib_text = bib_path.read_text(encoding="utf-8")
    entries = parse_bib_entries(bib_text)

    created = 0
    skipped = 0
    for key, entry in sorted(entries.items()):
        # Sanitize filename
        safe_key = re.sub(r'[<>:"/\\|?*]', '_', key)
        out_file = out_dir / f"{safe_key}.txt"

        if out_file.exists() and not overwrite:
            skipped += 1
            continue

        out_file.write_text(entry + "\n", encoding="utf-8")
        created += 1

    print(f"Extracted {len(entries)} entries from {bib_path.name}")
    print(f"  Created: {created} new files")
    print(f"  Skipped: {skipped} existing files")
    print(f"  Output: {out_dir}/")


if __name__ == "__main__":
    main()
