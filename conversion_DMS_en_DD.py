import math

def conv_DMS_DD(lattitude_dms, longitude_dms):
    # conversion latitude DMS en DD
    deg_la, min_la, sec_la = lattitude_dms
    dd_la = deg_la + (min_la/60) + (sec_la/3600)

    # conversion longitude DMS en DD
    deg_lo, min_lo, sec_lo = longitude_dms
    dd_lo = deg_lo + (min_lo/60) + (sec_lo/3600)

    return dd_la, dd_lo

def distance_pole_nord (lat_1, long_1, lat_2, long_2):
    # calcul distance entre 2 coordonée = racine carré de ((x2-x1)2 + (y2-y1)2)  
    distance = math.sqrt(((lat_2 - lat_1)**2 + (long_2 - long_1)**2))
    return distance

LAT_POLE_N = 86
LONG_POLE_N = 172
lattitude_dms_user = 48, 51, 23.81
longitude_dms_user = 2, 21, 7.9999

lat_u, long_u = conv_DMS_DD(lattitude_dms_user, longitude_dms_user)

print(lat_u)
print(long_u)
print(distance_pole_nord(LAT_POLE_N, LONG_POLE_N, lat_u, long_u))