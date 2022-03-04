import math

def conv_DMS_DD(lattitude_dms, longitude_dms):
    # conversion latitude DMS en DD
    deg_lat, min_lat, sec_lat = lattitude_dms
    dd_lat = deg_lat + (min_lat/60) + (sec_lat/3600)

    # conversion longitude DMS en DD
    deg_lon, min_lon, sec_lon = longitude_dms
    dd_lon = deg_lon + (min_lon/60) + (sec_lon/3600)

    return dd_lat, dd_lon

def distance_pole_nord (coordonnee_1, coordonnée_2):
    # calcul distance entre 2 coordonée = racine carré de ((x2-x1)2 + (y2-y1)2)  
    lat_1, long_1 = coordonnee_1
    lat_2, long_2 = coordonnée_2
    distance = math.sqrt(((lat_2 - lat_1)**2 + (long_2 - long_1)**2))
    return distance

COORDONNEE_POLE_NORD = 86, 172
lattitude_dms_user = 48, 51, 23.81
longitude_dms_user = 2, 21, 7.9999
coordonee_user = conv_DMS_DD(lattitude_dms_user, longitude_dms_user)

print(coordonee_user)
print(distance_pole_nord(COORDONNEE_POLE_NORD, coordonee_user))

# La ligne 18 contient une parenthèse supplémentaire inutile.
# La ligne 19 pourrait avoir directement le calcul sans utiliser la variable distance