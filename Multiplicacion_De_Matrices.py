#definicio de una funcion que imprime ambas matrices con ciclos for y saltos de linea para mayor entendimiento (ya visto en clase)
def imprimir_matriz (filasa, filasb, a, b):
    for i in range(filasa):
        print(a[i])
    print("\n")
    for i in range(filasb):
        print(b[i])
    print("\n")

#definicion de una funcion que recibira las entradas a cada indice de ambas matrices
def entrada_matrices (filasa, columnasa, filasb, columnasb, a, b):
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
    #repeticion del proceso anteriormente explicado con la diferencia de la matriz
    #con la que se esta operando
    for i in range(filasb): 
        entrada=[]
        for j in range(columnasb):
            entrada.append(int(input(
                "Ingrese el valor que quiera ingresar a la matriz B en la posicion ("
                +str(i+1)+", "+str(j+1)+"): ")))
        b.append(entrada) 
    #impresion de informacion con el llamado de funcion
    imprimir_matriz(filasa, filasb, a, b)
                                         
def matriz_resultado_0 (c, columnasa, filasb):
    #Impresion de la matriz con el tamaño que tendra pero con valores 0's
    for i in range(filasb):
        entrada=[0]*columnasb                                          
        c.append(entrada)
    for i in range(filasb):
        print(c[i])

def multiplicacion_matrices (filasa, columnasa, filasb, columnasb, a, b, c):
    #tres for's que recorren 1. el tamaño de la matriz final, y 2. el tamaño 
    #que ambas matrices tienen en comun                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
    for i in range(filasa):
        for j in range(columnasb):
            #inicio del valor que entrara en la matriz como 0 para evitar 
            #problemas al pasarlo
            suma = 0
            for k in range(columnasa):
                #aumenta el valor de la variable que entrara en la matriz a 
                #razon de la mutiplicacion de los valores correspondientes
                suma += a[i][k] * b[k][j]
            #cuando finalize la suma de los valores respectivos se ponen en la matriz
            c[i][j] = suma
    #impresion de la matriz final
    print("Matriz resultante: ")
    for fila in range(columnasb):
        print(c[fila])
            
        

if __name__=="__main__":
    
    #Inicio de las matrices necesarias en vacio para evitar problemas
    a=[]
    b=[]
    c=[]
    
    #inicio de las variables necesarias en negativo 1 y columnas y 
    # filas siendo distintas para asegurar al menos una ocurrencia
    #de los whiles de comprobacion de rango
    filasa:int=-1
    columnasa:int=-1
    filasb:int=-2
    columnasb:int=-1

    #comprobaciones de rango con while's
    while filasa<1:
        filasa=int(input("Ingrese la cantidad de filas de la matriz A: "))
        if filasa<1: print("El valor no es valido, intente con algo mayor o igual a 1")

    while columnasa<1:
        columnasa=int(input("Ingrese la cantidad de columnas de la matriz A: "))
        if columnasa<1: print("El valor no es valido, intente con algo mayor o igual a 1")

    while filasb<1 or columnasa!=filasb:
        filasb=int(input("Ingrese la cantidad de filas de la matriz B: "))
        if columnasa!=filasb:
            print("El numero de columnas de la primera matriz debe ser igual "+
                  "al numero de filas de la segunda matriz, intentelo de nuevo")
        if filasb<1: print("El valor no es valido, intente con algo mayor o igual a 1")

    while columnasb<1:
        columnasb=int(input("Ingrese la cantidad de columnas de la matriz B: "))    
        if columnasb<1: print("El valor ingresado no es valido, intente con algo mayor o igual a 1")
    
    
    
    #llamdo de matrices
    entrada_matrices(filasa, filasb, columnasa, columnasb, a, b)

    matriz_resultado_0(c, columnasa, filasb)

    multiplicacion_matrices(filasa, columnasa, filasb, columnasb, a, b, c)
