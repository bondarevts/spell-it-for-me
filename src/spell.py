#!/usr/bin/env python
from __future__ import print_function

import sys
import argparse
from typing import Dict

law_enforcement_spelling = {
    "a": "Adam",
    "b": "Boston",
    "c": "Charles",
    "d": "David",
    "e": "Edward",
    "f": "Frank",
    "g": "George",
    "h": "Henry",
    "i": "Ida",
    "j": "James",
    "k": "King",
    "l": "Lincoln",
    "m": "Mary",
    "n": "Nora",
    "o": "Oscar",
    "p": "Paul",
    "q": "Queen",
    "r": "Robert",
    "s": "Sam",
    "t": "Tom",
    "u": "Union",
    "v": "Victor",
    "w": "William",
    "x": "X-Ray",
    "y": "Young",
    "z": "Zebra",
}

nato_spelling = {
    "a": "Álfa",
    "b": "Brávo",
    "c": "Chárlie",
    "d": "Délta",
    "e": "Écho",
    "f": "Fóxtrot",
    "g": "Gólf",
    "h": "Hotél",
    "i": "Índia",
    "j": "Júliett",
    "k": "Kílo",
    "l": "Líma",
    "m": "Mike",
    "n": "Novémber",
    "o": "Óscar",
    "p": "Papá",
    "q": "Quebéc",
    "r": "Rómeo",
    "s": "Siérra",
    "t": "Tángo",
    "u": "Úniform",
    "v": "Víctor",
    "w": "Whísky",
    "x": "X-ray",
    "y": "Yánkee",
    "z": "Zúlu",
}

parser = argparse.ArgumentParser(
    description="A simple command line tool "
    "to display a spelling for any phrase "
    "using a phonetic alphabet."
)
parser.add_argument(
    "--alphabet",
    default="nato",
    choices=["nato", "law_enforcement"],
    dest="alphabet",

)
parser.add_argument(dest="phrase")


def print_spelling(args: argparse.ArgumentParser) -> None:
    if args.alphabet == "nato":
        spelling_map = nato_spelling
    elif args.alphabet == "law_enforcement":
        spelling_map = law_enforcement_spelling
    else:
        raise ValueError(f"Improper alphabet arg, must be {args['alphabet'].choices}")
    for letter in args.phrase:
        print(letter, ": ", sep="", end="")
        print(spelling_map.get(letter.lower(), letter))


def main() -> None:
    args = parser.parse_args()
    print_spelling(args)


if __name__ == "__main__":
    main()
