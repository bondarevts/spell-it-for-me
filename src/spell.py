#!/usr/bin/env python
from __future__ import print_function

import sys
from typing import Dict

law_enforcement_spelling = {
    'a': 'Adam',
    'b': 'Boston',
    'c': 'Charles',
    'd': 'David',
    'e': 'Edward',
    'f': 'Frank',
    'g': 'George',
    'h': 'Henry',
    'i': 'Ida',
    'j': 'James',
    'k': 'King',
    'l': 'Lincoln',
    'm': 'Mary',
    'n': 'Nora',
    'o': 'Oscar',
    'p': 'Paul',
    'q': 'Queen',
    'r': 'Robert',
    's': 'Sam',
    't': 'Tom',
    'u': 'Union',
    'v': 'Victor',
    'w': 'William',
    'x': 'X-Ray',
    'y': 'Young',
    'z': 'Zebra',
}

nato_spelling = {
    'a': 'Álfa',
    'b': 'Brávo',
    'c': 'Chárlie',
    'd': 'Délta',
    'e': 'Écho',
    'f': 'Fóxtrot',
    'g': 'Gólf',
    'h': 'Hotél',
    'i': 'Índia',
    'j': 'Júliett',
    'k': 'Kílo',
    'l': 'Líma',
    'm': 'Mike',
    'n': 'Novémber',
    'o': 'Óscar',
    'p': 'Papá',
    'q': 'Quebéc',
    'r': 'Rómeo',
    's': 'Siérra',
    't': 'Tángo',
    'u': 'Úniform',
    'v': 'Víctor',
    'w': 'Whísky',
    'x': 'X-ray',
    'y': 'Yánkee',
    'z': 'Zúlu'
}


def print_spelling(word: str, spelling_map: Dict[str, str]) -> None:
    for letter in word:
        print(letter, ': ', sep='', end='')
        print(spelling_map.get(letter.lower(), letter))


def main() -> None:
    phrase = ' '.join(sys.argv[1:])
    print_spelling(phrase, nato_spelling)


if __name__ == '__main__':
    main()
