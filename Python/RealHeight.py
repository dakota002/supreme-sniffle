import requests, ast, json, png
from math import sqrt, floor

apiKey=sys.argv[1]
geolocationKey = sys.argv[2]

geoUrl = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}"
location = requests.post(geoUrl.format(geolocationKey)).json()

print(location['location'])
rootLng = location['location']['lng']
rootLat = location['location']['lat']

singleRequestUrl = "https://maps.googleapis.com/maps/api/elevation/json?locations={0},{1}&key={2}".format(rootLng,rootLat,apiKey)
manyRequestUrl = "https://maps.googleapis.com/maps/api/elevation/json?locations={0}&key={1}"

def getHeight(url):
    request=requests.get(url).json()
    return request

def getGrid(unformattedUrl,lat,lng,apiKey):
    grid = []
    result = []
    for i in range(-100,101):
        row = []
        coords = []
        for j in range(-100,101):
            coords.append(str(lat+2*i/69)+','+str(lng + (2*j/69)))
        grid.append("|".join(coords))
    print(grid[0])
    for i in grid:
        newUrl = unformattedUrl.format(str(i),apiKey)
        re = getHeight(newUrl)
        for j in re['results']:
            result.append(j['elevation'])
    with open("elevation.txt", "w+") as file:
        file.write(json.dumps(result))

def loadGridFromFile(fileName):
    listVar = []
    with open(fileName,'r+') as file:
        listVar = file.readlines()
    return ast.literal_eval(listVar[0])

def WritePNG(listOfVals):
    minimum = min(listOfVals)
    print(minimum)
    sqrtSize = int(sqrt(len(listOfVals)))
    rows=[]
    for i in range(sqrtSize):
        rows.append(list(int(floor(val))-minimum for val in listOfVals[i*sqrtSize:(i*sqrtSize)+sqrtSize]))
    if (len(rows)==sqrtSize):
        with open('myPng.png','wb') as file:
            w = png.Writer(sqrtSize,sqrtSize,greyscale=True,bitdepth=16)
            w.write(file,rows)
    else:
        print("Not right dim")
