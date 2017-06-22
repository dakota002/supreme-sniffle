import png, sys
from datetime import datetime
from noise import pnoise2, snoise2


# For a world, octave at 8, freq at 256 * octave seems good,
# but its fun to play with these settings
octaves = 8
freq = 256.0 * octaves
rows = []

now = datetime.now().isoformat().replace(":","").replace(".","")+"-"+str(freq)+"-frequency"+"-"+str(octaves)+"-Octaves"+"-Image.png"



for i in range(4096):
    row = []
    for j in range(4096):
        row.append(int(snoise2(j / freq, i / freq, octaves) * 32767.0 + 32768.0))
    rows.append(row)

print(now)

with open(now,'wb') as file:
    w = png.Writer(4096,4096,greyscale=True, bitdepth=16)
    w.write(file,rows)
    
