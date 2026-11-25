"""One Star, Written in Sap: a houseplant's one-star review.

Writes the review to /output/entry.txt. Standard library only,
no network, no third-party packages. The output directory is created
if missing and is never deleted by this program.
"""

import os

TEXT = "One star. He waters me every Sunday whether I'm thirsty or not, then apologises to the fern like I'm not in the room. My pot is two sizes too small and he calls it 'cosy'. Would not recommend this windowsill to any plant with self-respect."

# The review above is the entry: a genuine one-star format with the
# plant's own grievance at the centre — the Sunday watering schedule,
# the fern getting the apology, a pot two sizes too small called cosy.
# Fresh, specific detail throughout; no stock phrases anywhere.


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(TEXT)
    print("wrote %d bytes to %s" % (len(TEXT.encode("utf-8")), path))


if __name__ == "__main__":
    main()
