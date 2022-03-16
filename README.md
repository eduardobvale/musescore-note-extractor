# Description

This script extract notes from .mscx files, useful for creating easy to read music sheets.

# Usage

First you need to get your desired .mscz file

Then you can run the python script by passing the file path as first argument: 

```
python3 musescore-note-extractor.py ~/Sample-file.mscz --pt_br --part_index=1
```

This will output all written notes, one compass by line:

```
# Choose instruments from the list below:
0 - B♭ Trumpet 1
1 - B♭ Trumpet 2
2 - Alto Saxophone
3 - Tenor Saxophone 1
4 - Tenor Saxophone 2
5 - Trombone 1
6 - Trombone 2
7 - Tuba
8 - Cowbell



# Notes by compass for B♭ Trumpet 2:


Dó# Fá# Mi
Ré
Si Si Si Si
Si Si Si Si
Si Si Si Si
Si Si Si Lá#
Sol Sol Sol Sol
Si Si Si Si Si
Lá# Lá# Lá# Lá# Lá#
Si
Fá# Fá# Fá# Fá#
Si Si Si Si
Fá# Fá# Fá# Fá#
Si Si Si Lá# Sol

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


