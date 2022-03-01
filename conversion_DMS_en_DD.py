import math

def conv_DMS_DD(deg_la, min_la, sec_la, deg_lo, min_lo, sec_lo):
    dd_la = deg_la + (min_la/60) + (sec_la/3600)
    dd_lo = deg_lo + (min_lo/60) + (sec_lo/3600)
    return dd_la, dd_lo

def distance_pole_nord (lat_1, long_1, lat_2, long_2):
 # racine carré de ((x2-x1)2 + (y2-y1)2)  
    distance = math.sqrt(((lat_2 - lat_1)**2 + (long_2 - long_1)**2))
    return distance

# Coordonée du pole nord, Lat : 86  Long : 172
LAT_POLE_N = 86
LONG_POLE_N = 172

# Coordonnée de l'utilisateur
deg_lat_u = 48
min_lat_u = 51
sec_lat_u = 23.81
deg_long_u = 2
min_long_u = 21
sec_long_u = 7.9999

lat_u, long_u = conv_DMS_DD(deg_lat_u, min_lat_u, sec_lat_u, deg_long_u, min_long_u, sec_long_u)

print(lat_u)
print(long_u)
print(distance_pole_nord(LAT_POLE_N, LONG_POLE_N, lat_u, long_u))