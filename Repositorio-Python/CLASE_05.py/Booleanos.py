mi_booleano=(1+1==3)

print(f"mi booleano es: {mi_booleano}")

mi_otro_booleano= not mi_booleano
print(f"mi otro booleano es {mi_otro_booleano}")
print()

xx= 3>4
yy= 2<11
zz= 3< 9/2
print()
print(xx,yy,zz)
print()

#OR
xx= 3 > 4 or 1 == 1
yy=2 <11 or 1000 < 4
zz=3 < 9/2 or 1 == 1
ww= "b">"z" or "d"> "z"
print(xx,yy,zz)

#AND
xx= 3 > 4 and 1 == 1
yy=2 <11 and 1000 < 4
zz=3 < 9/2 and 1 == 1
ww= "b">"z" and "d"> "z"
print(xx,yy,zz)