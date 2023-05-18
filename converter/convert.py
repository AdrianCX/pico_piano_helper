from sys import argv
import pretty_midi
import argparse

song={}

def printInstrument(instrument):
    for note in instrument.notes:
        key=note.pitch-36
        if note.start not in song:
            song[note.start] = [(key, 1, note.start, note.end)]
        else:
            song[note.start] += [(key, 1, note.start, note.end)]

        if note.end not in song:
            song[note.end] = [(key, 0, note.start, note.end)]
        else:
            song[note.end] += [(key, 0, note.start, note.end)]



parser = argparse.ArgumentParser(
                    prog='converter',
                    description='converts midi files to text for rp2040',
                    epilog='')

parser.add_argument('filename')
parser.add_argument('-i', '--instrument', required=False)

args = parser.parse_args()

midi_data = pretty_midi.PrettyMIDI(args.filename)

if args.instrument != None:
    printInstrument(midi_data.instruments[int(args.instrument)])
else:
    for instrument in midi_data.instruments:
        printInstrument(instrument)

song = dict(sorted(song.items()))
for k,v in song.items():
    for item in v:
        if item[0] >= 0 and item[0] <= 61:
            print(int(k*1000), end=" ")
            print(item[0], end=" ")
            print(item[1])
