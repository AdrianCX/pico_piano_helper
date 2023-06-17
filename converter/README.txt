To use converter:

A. Create environment:

1. Create convert venv for python
```
python -m venv convert
```

2. Load the env
```
source ./convert/bin/activate
```

3. Install requirements
```
pip3 install -r ./requirements.txt
```

B. Every time you want to convert, from converter folder

1. Load environment created at point A:
```
source ./convert/bin/activate
```

2. Convert files as you wish:
```
python3 ./convert.py ~/Downloads/Beethoven_Fur_Elise.mid > ../pico/songs/elise_instrument1.txt
```

If you want just certain tracks, then use -i and number of track. (You might have tracks for right/left hand and other items)

Example:
```
python3 ./convert.py -i 0 ~/Downloads/Beethoven_Fur_Elise.mid > ../pico/songs/elise_instrument1.txt
```