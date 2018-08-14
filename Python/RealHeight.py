import requests, ast, json, png, sys
from math import sqrt, floor


apiBaseUrl = "https://maps.googleapis.com/maps/api/elevation/json?locations="


class RealHeight:

    def __init__(self,apiKey,specificLng=None,specificLat=None,fileName=None):
        self.apiKey = apiKey
        self.geoUrl = "https://www.googleapis.com/geolocation/v1/geolocate?key={0}".format(self.apiKey)
        self.location = requests.post(self.geoUrl).json()
        self.rootLng = self.location['location']['lng']
        self.rootLat = self.location['location']['lat']
        self.specificLocationsRequestUrl = apiBaseUrl + "{0},{1}&key={2}".format(self.rootLng,self.rootLat,self.apiKey)
        self.manyLocationRequestUrl = apiBaseUrl + "{0}&key={1}"
        self.pathUrl = apiBaseUrl + "lat|long"
        print("Location is: ")
        print(self.location['location'])
        if (fileName!=None):
            self.fileName = fileName
        else:
            self.fileName = ""

    def getHeight(self,url):
        request=requests.get(url).json()
        return request

    def getGrid(self):
        grid = []
        result = []
        for i in range(-100,101):
            row = []
            coords = []
            for j in range(-100,101):
                coords.append(str(self.rootLat+2*i/69)+','+str(self.rootLng + (2*j/69)))
            grid.append("|".join(coords))
        print(grid[0])
        for i in grid:
            newUrl = self.manyLocationRequestUrl.format(str(i),self.apiKey)
            re = self.getHeight(newUrl)
            for j in re['results']:
                result.append(j['elevation'])
        self.heightGrid = result
        with open("elevation.txt", "w+") as file:
            file.write(json.dumps(result))

    def getPath(self, distanceRange):
        for i in range(distanceRange):
            startPoint = ""
            endPoint = ""
            pathUrl = self.pathUrl.replace("lat",startPoint).replace("long",endPoint)

    def loadGridFromFile(self,fileName):
        listVar = []
        with open(fileName,'r+') as file:
            listVar = file.readlines()
        self.fileName = fileName
        return ast.literal_eval(listVar[0])

    def WritePNG(self,listOfVals):
        minimum = min(min(listOfVals))
        sqrtSize = len(listOfVals)
        rows=[]
        print('fuck')
        print(sqrtSize)
        print('me')
        for i in range(sqrtSize):
            print(i)
            newThing = []
            #for j in range(sqrtSize):
            #    newThing.append(int(floor(listOfVals[i][j]-minimum)))
            #rows.append(newThing)
            rows.append(list(int(floor(val-minimum)) for val in listOfVals[i*sqrtSize:(i*sqrtSize)+sqrtSize]))
        if (len(rows)==sqrtSize):
            with open('myPng.png','wb') as file:
                w = png.Writer(sqrtSize,sqrtSize,greyscale=True,bitdepth=16)
                w.write(file,rows)
        else:
            print("Not right dim")

if __name__ == "__main__":
    rh = RealHeight("AIzaSyBrlQwg8zyGnho8rHSREWdeMUXNiE2b12E")
