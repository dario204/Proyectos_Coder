xx= int(input("Ingresar año de nacimiento:"))

if xx >= 1920 and xx<= 1940:
    print()
    print("-- Generacion Silenciosa")
    print()
else:
    if xx >= 1946 and xx <= 1964:
        print("-- Boomer")
    else:
        if xx >= 1965 and xx <=1979:
            print("Generacion X")    
    
