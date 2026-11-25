"""Museum of the Year 3000 — make.fun bounty entry.

Writes one line to /output/entry.txt: the museum label a museum in the
year 3000 places next to an ordinary object from today — a group chat.
"""

import os

LABEL = (
    "Group Chat, c. 2025. A room with no walls where 47 people talked "
    "at once about nothing, and called it friendship."
)

ENTRY_FILENAME = "entry.txt"


def main() -> None:
    # Gate self-check: one line, 1-200 characters, not only whitespace.
    if not LABEL.strip() or len(LABEL) > 200 or "\n" in LABEL:
        raise ValueError("label fails the entry gate (1 line, 1-200 chars)")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, ENTRY_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LABEL)
    print(LABEL)


if __name__ == "__main__":
    main()
