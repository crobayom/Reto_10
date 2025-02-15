def suma_fila (fila_elegida, columnas, a):
    #inicio de la variable necesaria en 0
    suma:int=0
    #for que recorreara en vertical la matriz
    for i in range(columnas):
        #aumento edl valor a medida que pase por los valores correspondientes
        suma+=a[fila_elegida-1][i]
    #refrso de valores
    return suma

def entrada_matrices (filasa, columnasa, a):
    #for que recorre el tamaño m de la matriz (vertical) especificado por el usuario
    for i in range(filasa): 
        #definicion de la matriz que se le agregara por cada fila iniciada en vacio para 
        # que lo este cada vez que comienze una nueva fila
        entrada=[]
        #for que recorrera el tamaño n (horizontal) de la matriz especificado por el usuario
        for j in range(columnasa):
            #entrada de cada valor del usuario a la fila que luego le sera añadida a la matriz
            entrada.append(int(input(
                #saltos de linea en ingreso de mensaje para mantener "orden"
                "Ingrese el valor que quiera ingresar a la matriz A en la posicion ("
                +str(i+1)+", "+str(j+1)+"): ")))
        #entrada de cada fila a la matriz
        a.append(entrada)
    #impresion de un salto de linea para mas entendimiento
    print("")
    for i in range(filas):
        print(a[i])
    print("")

if __name__=="__main__":

    #definicion de matriz con inicio vacio para evitar problemas
    a=[]
    #definicion de variables en negativo para asegurar la ocurrencia de la comprobacion
    filas:int=-1
    columnas:int=-1

    #comrpobacion de rangos con while's
    while filas<1:
        filas=int(input("Ingrese la cantidad de filas de la matriz: "))
        if filas<1: print("El valor ingresado no es viable, intente con algo mayor i igual a 1")
    
    while columnas<1:
        columnas=int(input("Ingrese la cantidad de columnas de la matriz: "))
        if columnas<1: print("El valor ingresado no es viable, intente con algo mayor o igual a 1")

    fila_elegida:int=-1

    while fila_elegida<1 or fila_elegida>filas:
        fila_elegida=int(input("Ingrese la fila que le gustaria sumar (entre 1 y "+str(filas)+"): "))
        if fila_elegida<1  or fila_elegida>columnas: print("El valor ingresado no es viable,"+
        " intentelo con algo mayor o igual a 1 y menor o igual al valor de filas")
    
    #llamada de funciones

    entrada_matrices(filas, columnas, a)

    print(str(suma_fila(fila_elegida, columnas, a)))
