A={1,2,3,4}
B={2,3}
C={1,2,3,4,5}
D={100,101}

#COPY
mi_conjunto= B.copy()

print(mi_conjunto)
mi_conjunto.add("7")
print(mi_conjunto)
print(B)

#ISDIJOINT
print(A.isdisjoint(B))
print(A.isdisjoint(D))
print()

#ISSUBET
print(B.issubset(A))
print(B.issubset(C))
print()

#ISSUPERSET
print(A.issuperset(B))
print(D.issuperset(B))
print()

#UNION
E= A.union(D)
print(E)
print()

#DIFERENCE
F= A.difference(B)
print(F)
print()

#DIFERENCE_UPDATE
A.difference_update(B)
print(A)
print()

#INTERSECTION
Interseccion= A.intersection(B)
print(Interseccion)
print()
