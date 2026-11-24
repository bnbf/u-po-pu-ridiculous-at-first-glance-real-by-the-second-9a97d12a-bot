#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second — one-sentence entry.

Writes the single startup pitch (one sentence, at most 200 characters) to
/output/entry.txt and prints it to stdout. Deterministic, stdlib only.
"""

import os
import sys

# The entry text: one sentence pitching a bizarre startup idea that sounds
# absurd until the business logic lands.
# Angle: pigeon-delivered divorce papers is a mechanism nobody has heard
# of (not a familiar business with a strange adjective), and the money
# logic is real — service of process is a legally required market at
# ~$150 a visit, and the pain is exes who dodge the door. The turn is
# "a pigeon can't be dodged": the joke becomes the moat in one clause.
LINE = "We deliver divorce papers by homing pigeon, because spouses pay process servers $150 a visit to chase exes who never answer the door \u2014 and a pigeon can\u2019t be dodged."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    out = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
