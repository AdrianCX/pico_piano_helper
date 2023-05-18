To use converter:

example:
```
# source ./env.sh
python3 ./convert.py ~/Downloads/Beethoven_Fur_Elise.mid > ../pico/songs/elise_instrument1.txt
```

If you want just certain tracks, then use -i and number of track. (You might have tracks for right/left hand and other items)

Example:
```
python3 ./convert.py -i 0 ~/Downloads/Beethoven_Fur_Elise.mid > ../pico/songs/elise_instrument1.txt
```