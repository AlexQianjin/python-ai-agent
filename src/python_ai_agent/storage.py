"""Save completed agent responses as Markdown."""

import re
from datetime import date
from pathlib import Path


def save_result(result: str, slot: str) -> Path:
    """Write a response to ./data/YYYY-MM-DD-{slot}.md and return its path."""
    safe_slot = re.sub(r"[^\w-]+", "-", slot, flags=re.UNICODE).strip("-_")
    safe_slot = safe_slot[:80] or "result"
    directory = Path("data")
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / f"{date.today().isoformat()}-{safe_slot}.md"
    # Preserve earlier responses for repeated requests on the same day.
    suffix = 2
    while True:
        try:
            with path.open("x", encoding="utf-8") as output:
                output.write(result)
            return path
        except FileExistsError:
            path = directory / f"{date.today().isoformat()}-{safe_slot}-{suffix}.md"
            suffix += 1
