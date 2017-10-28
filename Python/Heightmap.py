import png, sys, requests
from datetime import datetime
from noise import pnoise2, snoise2
import random as rnd

# For a world, octave at 8, freq at 256 * octave seems good,
# but its fun to play with these
octaves = rnd.randint(1,8)
size = 2**rnd.randint(8,12)
print(sys.argv)

if len(sys.argv) > 2:
    octaves = int(sys.argv[2])
    size = int(sys.argv[1])
elif len(sys.argv) == 2:
    size = sys.argv[1]

freq = 256.0 * octaves
rows = []

now = datetime.now().isoformat().replace(":","").replace(".","")+"-"+str(freq)+"-frequency-"+str(octaves)+"-Octaves-snoise-Image.png"

num = rnd.random() * rnd.randint(0,999)

print("The snoise function")
for i in range(size):
    row = []
    for j in range(size):
        row.append(int(snoise2(j / freq, i / freq, octaves, base=num) * 32767.0 + 32768.0))
    rows.append(row)

print(now)

with open(now,'wb') as file:
    w = png.Writer(size,size,greyscale=True, bitdepth=16)
    w.write(file,rows)
