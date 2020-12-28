# Spell It For Me
A simple command line tool to display a spelling for any phrase using a phonetic alphabet.

Can use NATO (`-a nato`, active by default) or law enforcement (`-a police`) phonetic alphabets.

More alphabets might be supported in the future.

## Installation

Run the following to install:

```bash
$ pip install spell-it-for-me
```

## Usage

By default `spell` will print every letter spelled on a separate line using the NATO phonetic alphabet:  
```bash
$ spell Louis 
Líma
Óscar
Úniform
Índia
Siérra
```

Spelling phrases of several words is supported:
```bash
$ spell Worcester, MA
Whísky
Óscar
Rómeo
Chárlie
Écho
Siérra
Tángo
Écho
Rómeo
,
 
Mike
Álfa
```

Law enforcement alphabet is available (use `-a police` or `--alphabet police`):
```bash
$ spell -a police Louis
Lincoln
Oscar
Union
Ida
Sam
```

Use `-v` (or `--verbose`) to print each letter used for spelling:
```bash
spell.py -v Louis
L: Líma
o: Óscar
u: Úniform
i: Índia
s: Siérra
```
