
# TAREA DE CARRO DE COMPRA
# AUTOR:ROBERTO BORGES. CURSO DE PROGRAMACION C.E.L 7/2025

articulo=[]
precio=[]
i=0
while i==0:
    print("\ncarro de compra python\n*****Menú*****".upper())
    print("1. agregar".upper())
    print("2. mostrar".upper())
    print("3. eliminar".upper())
    print("4. calcular".upper())
    print("5. renunciar".upper())
    opcion=int(input())
    if opcion==1:
        print("<<<<<agregar>>>>>".upper())
        p=str(input("agregue producto:\n ".title()))
        v=float(input("introduzca precio:\n ".title()))
        articulo.append(p.lower())
        precio.append(v)
        print("producto agregado 👍".title())

    elif opcion==2:
        print("<<<<<mostrar>>>>>".upper())
        if len(articulo)==0:
            print("no tiene articulos".upper())
        else:
            j=0
            while j<len(articulo):
                print(f"{articulo[j]}".upper() , precio[j])
                j+=1

    elif opcion==3:
        print("<<<<<eliminar>>>>>".upper())
        if len(articulo)==0:
            print("no tiene articulos".upper())
        else:
            elim_art=str(input("cual articulo desea aliminar:?\n ".capitalize()))
            ind=articulo.index(elim_art.lower())
            del articulo[ind]
            del precio[ind]
            j = 0
            while j < len(articulo):
                print(f"{articulo[j]}".upper() , precio[j])
                j += 1

    elif opcion==4:
        print("<<<<<calcular>>>>>".upper())
        if len(articulo)==0:
            print("no tiene articulos".upper())
        else:
            calcular=sum(precio)
            print("el cálculo es:\n\t".capitalize(), calcular)

    elif opcion==5:
        print("renunciar".upper())
        exit()

    else:
        print("opcion no válida".capitalize())

