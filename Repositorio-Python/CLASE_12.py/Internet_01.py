import requests

pais= input("Ingrese un pais:")
direccion_web= f"http://restcountries.com/v3.1/name/{pais}"
pedido_web= requests.get(direccion_web)
informacion = pedido_web.json()

print(informacion)