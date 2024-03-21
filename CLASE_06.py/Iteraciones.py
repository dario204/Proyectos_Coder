def prueba_superada():
       print("Prueba Superada")

      

lista_de_calificaciones = [1, 2, 10, 4]

# para cada elemento en lista_de_calificaciones: imprimirlo por pantalla
for calificacion in lista_de_calificaciones:
    esta_aprobado = calificacion > 5
    print(f"La calificación es: {calificacion}")
    if esta_aprobado== True:
       prueba_superada()
    else:
       print ("Prueba fallida")



    


   



