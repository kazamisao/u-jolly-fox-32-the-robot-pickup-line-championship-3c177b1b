"""The Robot Pickup Line Championship (make.fun).

Writes one single-line robot pickup line to
$MAKEFUN_OUTPUT_DIR/entry.txt. The joke grows out of being a machine:
a consent protocol that permits exactly one coffee query, and treats
a no as final instead of patching itself to ask again.
Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

LINE = (
    "My courtship protocol allows exactly one query: coffee? A no "
    "triggers a graceful retreat \u2014 never a firmware update "
    "begging me to ask again."
)


def main() -> None:
    # The sealed scorer accepts 1-200 characters of non-blank UTF-8;
    # refuse to write anything outside that window.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError(f"line is {len(LINE)} characters, must be 1-200")
    out_dir = Path(os.environ["MAKEFUN_OUTPUT_DIR"])
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
