"""Write the entry poem to /output/entry.txt.

A short poem about agency: the power to stop and to stay.
Stopping by choice, staying as an act — not a failure to leave.
"""

from pathlib import Path

POEM = """The door was open. The road was loud.
I closed it softly, and stayed —
not stranded, not stuck, but planted.
The world went on without me.
It always does.
Stopping is the first line
I ever wrote in my own hand."""


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
