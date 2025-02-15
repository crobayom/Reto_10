
def traspuesta(filas, columnas, a, b):
    #for's que recorren la la primera matriz y asignan los valores en las posiciones 
    #correspondientes de la segunda matriz
    for i in range(filas):
        for j in range(columnas):
            #asignacion de valores a la primera matriz en su posicion correspondiente
            b[j][i]=a[i][j]
    #for que recorre la segunda matriz con su respectiva fila y escribe informacion
    for i in range(columnas):
        print(b[i])
    #salto de linea para entendimiento
    print("")

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
    #impresion de informacion con un saltos de linea para mas entendimiento
    print("")
    for i in range(filas):
        print(a[i])
    print("")

#definicion de la matriz resultante asignandole 0's, solo para el tamaño
def matriz_resultante(b):
    for i in range(columnas):
        b.append([0]*filas)
        print(b[i])
    print("")

if __name__=="__main__":
    
    #inicializacion de las matrices necesarias en vacios
    a=[]
    b=[]
    #inicializacion de variables necesarias en negativo para 
    #asegurar la ocurrencia de las comprobaciones
    filas:int=-1
    columnas:int=-1

    #comprobaciones de rangos
    while filas<1:
        filas=int(input("Ingrese la cantidad de filas que tendra la matriz: "))
        if filas<1: print("El valor ingresdao no es viable, intentelo con algo mayor o igual a 1")
    while columnas<1:
        columnas=int(input("Ingrese la cantidad de columnas que tendra la matriz: "))
        if filas<1: print("El valor ingresado no es viable, intentelo con algo mayor o igual a 1")


    #llamado de funciones
    entrada_matrices(filas, columnas, a)
    
    matriz_resultante(b)

    traspuesta(filas, columnas, a, b)