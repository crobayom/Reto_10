#definicio de una funcion que imprime ambas matrices con ciclos for y saltos de linea para mayor entendimiento (ya visto en clase)
def imprimir_matriz (vertical, a, b):
    for i in range(vertical):
        print(a[i])
    print("\n")
    for i in range(vertical):
        print(b[i])
    print("\n")

#definicion de una funcion que recibira las entradas a cada indice de ambas matrices
def entrada_matrices (vertical, horizontal, a, b):
    #for que recorre el tamaño m de la matriz (vertical) especificado por el usuario
    for i in range(vertical): 
        #definicion de la matriz que se le agregara por cada fila iniciada en vacio para 
        # que lo este cada vez que comienze una nueva fila
        entrada=[]
        #for que recorrera el tamaño n (horizontal) de la matriz especificado por el usuario
        for j in range(horizontal):
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
    for i in range(vertical): 
        entrada=[]
        for j in range(horizontal):
            entrada.append(int(input(
                "Ingrese el valor que quiera ingresar a la matriz B en la posicion ("
                +str(i+1)+", "+str(j+1)+"): ")))
        b.append(entrada) 
    #impresion de informacion con el llamado de funcion
    imprimir_matriz(vertical, a, b)

#definicion de la funcion que sumara ambas matrices
def sumar_restar_matrices (vertical, horizontal, suma_o_resta, a, b):
    #for que recorrera el tamaño m de la matriz (vertical) especificado por el usuario
    for i in range(vertical):
        #for que recorre el tamaño n de la matriz (horizontal) especificado por el usuario
        for j in range(horizontal):
            #condicional de decision de la naturaleza de la operacion dependiendo de la eleccion
            if suma_o_resta==1:
            #suma de los valores de una matriz a otra (para ahorrar recursos en crear otra matriz)
                a[i][j]+=b[i][j]
            else:
                a[i][j]-=b[i][j]
        #impresion de informacion a medida que se contruye
        print(a[i])
    #salto de linea para mayor entendimiento
    print("\n")


if __name__=="__main__":
    #definicion de matrices necesarias para el proceso, iniciadas en vacio para evitar complicaciones
    a=[]
    b=[]
    #definicion e ingreso de valores necesarios del tamaño de la matriz (unificados para ambas 
    #matrices pues la suma o resta solo se puede realizar si tienen el mismo tamaño)
    vertical:int=int(input("Ingrese el tamaño vertical de las matrices: "))
    horizontal:int=int(input("Ingrese el tamaño vertical de las matrices: "))
    #definicion de la variable d decision con un valor fuera del rango para garantizar entrar a la verficiacion
    suma_o_resta:int=3
    #verificacion de rangos
    while suma_o_resta<1 or suma_o_resta>2:
        #ingreso de informacion sobre la naturaleza de la operacion
        suma_o_resta=int(input("ingrese un 1 para que la operacion sea de suma o un 2 para que la operacion sea de resta: "))
        #aviso de error en caso de haberlo
        if suma_o_resta<1 or suma_o_resta>2:
            print("El valor ingresado esta fuera de los rangos, intentelo de nuevo")
    #llamado de funciones necesarias y explicadas anteriormente
    entrada_matrices(vertical, horizontal, a, b)
    sumar_restar_matrices(vertical, horizontal, suma_o_resta, a, b)