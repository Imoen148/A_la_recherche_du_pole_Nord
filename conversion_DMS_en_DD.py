def conv_DMS_DD(degLa, minLa, secLa, degLo, minLo, secLo):
    DdLa = degLa + (minLa/60) + (secLa/3600)
    DdLo = degLo + (minLo/60) + (secLo/3600)
    return DdLa, DdLo

a = 60
b = 20
c = 28
d = 180
e = 15
f = 35

print(conv_DMS_DD(a,b,c,d,e,f))