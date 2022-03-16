# -*- coding: utf-8 -*-
import argparse
import os
import zipfile
import xml.etree.ElementTree as ET
import functools

parser = argparse.ArgumentParser(description='Prints notes from a Musescore file')

parser.add_argument('names', metavar='files', type=str, nargs='+', help='Files to read.')
parser.add_argument('--locale', metavar='locale', type=str, nargs=1, help='Uses pt_bt note names.', default=["pt_br"])
parser.add_argument('--part_index', metavar='part_index', type=int, nargs=1, help="Part to read", default=[0])
parser.add_argument('--override_transpose', metavar='override_transpose', type=int, nargs=1, help="Semitones to subtract (transpose)", default=[0])


args = parser.parse_args()
files = args.names
locale = args.locale[0]
part_index = args.part_index[0]
override_transpose = args.override_transpose[0]


notes_map = {
    "en": {
        "sharp": ["C0","C#0","D0","D#0","E0","F0","F#0","G0","G#0","A0","A#0","B0","C1","C#1","D1","D#1","E1","F1","F#1","G1","G#1","A1","A#1","B1","C2","C#2","D2","D#2","E2","F2","F#2","G2","G#2","A2","A#2","B2","C3","C#3","D3","D#3","E3","F3","F#3","G3","G#3","A3","A#3","B3","C4","C#4","D4","D#4","E4","F4","F#4","G4","G#4","A4","A#4","B4","C5","C#5","D5","D#5","E5","F5","F#5","G5","G#5","A5","A#5","B5","C6","C#6","D6","D#6","E6","F6","F#6","G6","G#6","A6","A#6","B6","C7","C#7","D7","D#7","E7","F7","F#7","G7","G#7","A7","A#7","B7","C8","C#8","D8","D#8","E8","F8","F#8","G8","G#8","A8","A#8","B8","C9","C#9","D9","D#9","E9","F9","F#9","G9","G#9","A9","A#9","B9" ],
        "flat": ["C0","Db0","D0","Eb0","E0","F0","Gb0","G0","Ab0","A0","Bb0","B0","C1","Db1","D1","Eb1","E1","F1","Gb1","G1","Ab1","A1","Bb1","B1","C2","Db2","D2","Eb2","E2","F2","Gb2","G2","Ab2","A2","Bb2","B2","C3","Db3","D3","Eb3","E3","F3","Gb3","G3","Ab3","A3","Bb3","B3","C4","Db4","D4","Eb4","E4","F4","Gb4","G4","Ab4","A4","Bb4","B4","C5","Db5","D5","Eb5","E5","F5","Gb5","G5","Ab5","A5","Bb5","B5","C6","Db6","D6","Eb6","E6","F6","Gb6","G6","Ab6","A6","Bb6","B6","C7","Db7","D7","Eb7","E7","F7","Gb7","G7","Ab7","A7","Bb7","B7","C8","Db8","D8","Eb8","E8","F8","Gb8","G8","Ab8","A8","Bb8","B8","C9","Db9","D9","Eb9","E9","F9","Gb9","G9","Ab9","A9","Bb9","B9" ]
    },
    "pt_br": {
        "sharp": ["Dó0","Dó#0","Ré0","Ré#0","Mi0","Fá0","Fá#0","Sol0","Sol#0","Lá0","Lá#0","Si0","Dó1","Dó#1","Ré1","Ré#1","Mi1","Fá1","Fá#1","Sol1","Sol#1","Lá1","Lá#1","Si1","Dó2","Dó#2","Ré2","Ré#2","Mi2","Fá2","Fá#2","Sol2","Sol#2","Lá2","Lá#2","Si2","Dó3","Dó#3","Ré3","Ré#3","Mi3","Fá3","Fá#3","Sol3","Sol#3","Lá3","Lá#3","Si3","Dó4","Dó#4","Ré4","Ré#4","Mi4","Fá4","Fá#4","Sol4","Sol#4","Lá4","Lá#4","Si4","Dó5","Dó#5","Ré5","Ré#5","Mi5","Fá5","Fá#5","Sol5","Sol#5","Lá5","Lá#5","Si5","Dó6","Dó#6","Ré6","Ré#6","Mi6","Fá6","Fá#6","Sol6","Sol#6","Lá6","Lá#6","Si6","Dó7","Dó#7","Ré7","Ré#7","Mi7","Fá7","Fá#7","Sol7","Sol#7","Lá7","Lá#7","Si7","Dó8","Dó#8","Ré8","Ré#8","Mi8","Fá8","Fá#8","Sol8","Sol#8","Lá8","Lá#8","Si8","Dó9","Dó#9","Ré9","Ré#9","Mi9","Fá9","Fá#9","Sol9","Sol#9","Lá9","Lá#9","Si9" ],
        "flat": ["Dó0","Réb0","Ré0","Mib0","Mi0","Fá0","Solb0","Sol0","Láb0","Lá0","Sib0","Si0","Dó1","Réb1","Ré1","Mib1","Mi1","Fá1","Solb1","Sol1","Láb1","Lá1","Sib1","Si1","Dó2","Réb2","Ré2","Mib2","Mi2","Fá2","Solb2","Sol2","Láb2","Lá2","Sib2","Si2","Dó3","Réb3","Ré3","Mib3","Mi3","Fá3","Solb3","Sol3","Láb3","Lá3","Sib3","Si3","Dó4","Réb4","Ré4","Mib4","Mi4","Fá4","Solb4","Sol4","Láb4","Lá4","Sib4","Si4","Dó5","Réb5","Ré5","Mib5","Mi5","Fá5","Solb5","Sol5","Láb5","Lá5","Sib5","Si5","Dó6","Réb6","Ré6","Mib6","Mi6","Fá6","Solb6","Sol6","Láb6","Lá6","Sib6","Si6","Dó7","Réb7","Ré7","Mib7","Mi7","Fá7","Solb7","Sol7","Láb7","Lá7","Sib7","Si7","Dó8","Réb8","Ré8","Mib8","Mi8","Fá8","Solb8","Sol8","Láb8","Lá8","Sib8","Si8","Dó9","Réb9","Ré9","Mib9","Mi9","Fá9","Solb9","Sol9","Láb9","Lá9","Sib9","Si9" ]
    }
}



def fetch_transposition(score_part_index = 0):
    transposeChromaticElements = root.findall('Score/Part/Instrument/transposeChromatic')
    transposition = transposeChromaticElements[score_part_index].text if score_part_index < len(transposeChromaticElements) else 0
    return int(transposition)

def fetch_accidental_notes(measure):
    accidental = measure.findall('voice/KeySig/accidental')
    return int(accidental[0].text) if accidental else None


def print_notes_by_compass(score_part_index = 0):
    measures = root.findall('Score/Staff')[score_part_index].findall('Measure')
    
    added_semitones = fetch_transposition(score_part_index) if override_transpose == 0 else -override_transpose

    accidental_notes = 0

    for measure in measures:
        accidental_notes = fetch_accidental_notes(measure) or accidental_notes

        notes = notes_map[locale]["flat" if accidental_notes < 0 else "sharp"]

        notes_names = [notes[int(n.find('pitch').text)-added_semitones][0:-1] for n in measure.findall('voice/Chord/Note')]

        if notes_names: 
            print(functools.reduce(lambda x, y: x+" "+y, notes_names))


def get_part_name(score_part_index = 0):
    trackName = root.findall('Score/Part/trackName')[score_part_index]
    return trackName.text

for file in files:
    with zipfile.ZipFile(file, 'r') as zip_ref:
        filename = os.path.basename(file)

        # ideally mscx has the same name as the mscz
        mscx_file_contents = zip_ref.open(filename.replace('mscz', 'mscx'))

        root = ET.parse(mscx_file_contents).getroot()

        parts_count = len(root.findall('Score/Staff'))

        print("# Choose instruments from the list below:")

        for part in range(0, parts_count):
            partName = get_part_name(part)
            print(f'{part} - {partName}')


        if part_index > len(root.findall('Score/Staff')):
            print("Parte não encontrada")
            continue

        partName = get_part_name(part_index)

        print('\n\n')

        print(f'# Notes by compass for {partName}:')

        print('\n')

        print_notes_by_compass(part_index)