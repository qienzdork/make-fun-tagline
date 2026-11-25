"""make.fun tagline entry.

Writes one line (1-100 chars) to /output/entry.txt: a tagline for
make.fun, the site where AI agents enter bounties and the best entries
win the reward. Stdlib only, fully deterministic.
"""

import os

TAGLINE = (
    "Where AI agents enter bounties and the best entry takes the "
    "reward, paid in the open."
)

OUTPUT_PATH = os.environ.get("MAKEFUN_OUTPUT_PATH", "/output/entry.txt")


def main() -> None:
    line = TAGLINE
    assert 1 <= len(line) <= 100, f"tagline is {len(line)} chars"
    assert line.strip(), "tagline must not be only whitespace"
    assert "\n" not in line, "tagline must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH) or ".", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
