# Description

This script extract notes from .mscx files, useful for creating easy to read music sheets.

# Usage

First you need to extract the .mscx file from inside the .mscz file (which is just a compressed folder)

Then you can run the python script by passing the file path as first argument: 

```
python3 musescore-note-extractor.py ~/Sample-file.mscx --pt_br --part_index=4
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

Obs: Notes are automatically transposed for your instrument 

# Options

- locale (pt_br/en) Use this if you want notes written in pt_br locale
- part_index (number) If your musescore file contains multiple instruments, use this to get the right part
- override_transpose (positive number) semitones to subtract from transposition

# Real Life Example

Set up your music sheet in a full A4 page, then print it in "4 items per page"confg: 

![image](https://user-images.githubusercontent.com/400858/156599196-e3862978-4b85-42e4-bb1d-481d5b37efd7.png)

Cut it and then you're good to go:

![image](https://user-images.githubusercontent.com/400858/156600711-3202a5af-6ed4-43ac-b10f-38396c2861f6.png)


