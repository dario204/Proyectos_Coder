import time
#Opcion 1
#for i in range(10):
#    print(xx,yy)

#Opcion 2
#print([xx]* 10)
#print([yy]* 10)
# 3. Modificar el ejercio anterior para que el valor de xx aumente hasta 9
# y el valor de yy disminuya hasta 1

xx = 0
yy = 10
for i in range(10):
    print(f"El valor de xx es: {xx}")
    xx += 1
    print(f"El valor de yy es {yy}")
    yy -= 1
    print()