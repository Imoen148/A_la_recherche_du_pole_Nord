import math

def conv_DMS_DD(degLa, minLa, secLa, degLo, minLo, secLo):
    DdLa = degLa + (minLa/60) + (secLa/3600)
    DdLo = degLo + (minLo/60) + (secLo/3600)
    return DdLa, DdLo

def distance_pole_nord (lat1, long1, lat2, long2):
 # racine carré de ((x2-x1)2 + (y2-y1)2)  
    distance = math.sqrt(((lat2 - lat1)**2 + (long2 - long1)**2))
    return distance

# Coordonée du pole nord, Lat : 81.3  Long : 110.8


LATPOLEN = 81.3
LONGPOLEN = 110.8
degLa = 60
minLa = 20
secLa = 28
degLo = 180
minLo = 15
secLo = 35

latU, longU = conv_DMS_DD(degLa, minLa, secLa, degLo, minLo, secLo)

print(latU)
print(longU)
print(distance_pole_nord(LATPOLEN, LONGPOLEN, latU, longU))