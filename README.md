# Description

This script extract notes from .mscx files, useful for creating easy to read music sheets.

# Usage

First you need to extract the .mscx file from inside the .mscz file (which is just a compressed folder)

Then you can run the python script by passing the file path as first argument: 

```
python3 musescore-note-extractor.py ~/Sample-file.mscx --pt_br --part_index=4 --transpose=Bb
```

This will output all written notes, one compass by line:

```
Dó Fá
Lá# Sol
Sol# Lá#
Dó Dó Ré# Dó Ré# Dó
Sol Ré#
Fá Sol
Ré# Fá
Dó Dó Ré# Dó Ré# Dó
Sol Ré#
Fá Sol
Ré# Fá
Dó Dó Ré# Dó Ré# Dó
Dó Fá
Lá# Sol
Sol# Lá#
Dó
Dó Fá
Lá# Sol
Sol# Lá#
```

# Options

- pt_br (boolean) Use this if you want notes written in pt_br locale
- transpose (Bb/Eb) Use this if you need this for an specific transposed instrument
- part_index (number) If your musescore file contains multiple instruments, use this to get the right part
