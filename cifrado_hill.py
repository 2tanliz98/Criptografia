import numpy as np
import math

# Función recursiva para encontrar el inverso de un modulo
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

# Parámetros a = valor inversa, m = modulo
def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# Función que obtiene la adjunta transpuesta de una matriz 
def adjunta_transpuesta(matriz_k ):
    matriz_k = np.array(matriz_k)

    MC=np.zeros((3,3))# Matriz de cofactores
    idx=np.arange(3)

    for i in range(np.size(matriz_k,0)):
        for j in range(np.size(matriz_k,1)):
            fidx = idx[idx != i]
            cidx = idx[idx != j]
            cof=matriz_k[[[fidx[0]],[fidx[1]]],cidx]
            MC[i,j]=round(pow(-1,i+j)*np.linalg.det(cof),1)
    # Matriz adjunta transpuesta
    matriz_adjunta_t=MC.transpose() 
    return matriz_adjunta_t



#mensaje="makyrz"
#clave="kilowatts"
    
"""
matriz_k = []
matriz_m = []
clave_index = []
matriz_c = []
"""


# Matriz k
def matrizK(k,abc):
    clave_index = []
    matriz_k = []
    # Obtiene las posiciones de la clave
    for i in clave:
        clave_index.append(abc.index(i))

    # Separa por listas de 3 la clave
    for i in range (0,len(clave_index),3):
        matriz_k.append(list(clave_index[i:i+3]))
    print("Matriz k= ",matriz_k)

    return matriz_k



def cifrado_Hill(mensaje,k,abc):
    modulo = len(abc)
    matriz_k = matrizK(k,abc)
    matriz_m = []
    matriz_c = []
    # Si el mensaje no es múltiplo de 3 se reyena con "x"
    mod_mensaje = len(mensaje)%3
    if(mod_mensaje==1):
        mensaje+="xx"
    if(mod_mensaje==2):
        mensaje+="x"

    # la matriz k debe tener determinante!=0
    determinante = np.linalg.det(matriz_k)
    print("Determinante de K: ",round(determinante%modulo))

    # Crea matriz de mensaje
    mensaje = list(mensaje)
    for i in mensaje:
        matriz_m.append(abc.index(i))
    print("Matriz de mensaje = \n",matriz_m)


    for i in range(0, len(matriz_m),3):
        # Multiplicación de matrices
        matriz_mult = np.matmul(matriz_k, matriz_m[i:i+3])

        # Obteniendo el modulo
        for i in matriz_mult:
            matriz_c.append(i%modulo)

        # Busca la letra resultante para hacer el cifrado
        cifrado = ""
        for i in matriz_c:
            cifrado += abc[i]

    print("Matriz cifrada = \n",matriz_c)
    print("Mensaje cifrado: ",cifrado)



# Descrifrar
def descifrado_Hill(mensaje,k,abc):
    matriz_k = matrizK(k,abc)
    modulo = len(abc)
    matriz_c= []
    # la matriz k debe tener determinante!=0
    determinante = np.linalg.det(matriz_k)
    print("Determinante de K: ",round(determinante%modulo))
    
    # Determinate inverso
    det_inv = modinv(round(determinante%modulo), modulo)

    # Crea matriz de mensaje cifrado
    mensaje = list(mensaje)
    for i in mensaje:
        matriz_c.append(abc.index(i))
    print("Matriz de mensaje = \n",matriz_c)

    # Matriz adjunta transpuesta de k
    matriz_adjunta_t = adjunta_transpuesta(matriz_k )
    print ("Matriz adjunta transpuesta\n",matriz_adjunta_t)

    #  Obteniendo el modulo de la matriz
    for i in range (len(matriz_adjunta_t)):
        matriz_adjunta_t[i] = matriz_adjunta_t[i] * det_inv
        matriz_adjunta_t[i] = matriz_adjunta_t[i] % modulo

    print("Matriz adjunta transpuesta mod ",modulo,"\n", matriz_adjunta_t)

    matriz_m = []
    for i in range(0, len(matriz_c),3):
        # Multiplicación de matrices
        matriz_mult = np.matmul(matriz_adjunta_t, matriz_c[i:i+3])
        print("Matriz de multiplicación por mod ",modulo, "\n",matriz_mult)

        # Obteniendo el modulo
        for i in matriz_mult:
            matriz_m.append(int(i)%modulo)

        # Busca la letra resultante para hacer el cifrado
        descifrado = ""
        for i in matriz_m:
            descifrado += abc[int(i)]
    print("Matriz de mensaje descifrado= \n",matriz_m)
    print("Mensaje descifrado: ",descifrado)



# Menú
# Abecedario
abc26= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
abc27= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
abc37 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9']

op=0
while(op!=7):
    print("\n\t\t***** Menú Cifrado Hill *****")
    print("1. Cifrar con abecedario 26\n",
                "2. Cifrar con abecedario 26\n",
                "3. Cifrar con abecedario 27\n",
                "4. Descrifrar con abecedario 27\n",
                "5. Cifrar con abecedario 37\n",
                "6. Descrifrar con abecedario 37\n",
                "7. Salir")
    op = int(input("Elija una opción: "))
    if(op==1):
        print("***** Algoritmo Hill con abecedario 26 *****")
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        clave = str(input("Ingrese la clave para cifrar: "))
        cifrado_Hill(mensaje, clave, abc26)
    if(op==2):
        print("***** Algoritmo Hill con abecedario 26*****")
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        clave = str(input("Ingrese la clave para descifrar: "))
        descifrado_Hill(mensaje, clave, abc26)
    if(op==3):
        print("***** Algoritmo  Hill con abecedario 27 *****")
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        clave = str(input("Ingrese la clave para cifrar: "))
        cifrado_Hill(mensaje, clave, abc27)
    if(op==4):
        print("***** Algoritmo  Hill con abecedario 27 *****")
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        clave = str(input("Ingrese la clave para descifrar: "))
        descifrado_Hill(mensaje, clave, abc27)
    if(op==5):
        print("***** Algoritmo  Hill con abecedario 37 *****")
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        clave = str(input("Ingrese la clave para cifrar: "))
        cifrado_Hill(mensaje, clave, abc37)
    if(op==6):    
        print("***** Algoritmo  Hill con abecedario 37 *****")
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        clave = str(input("Ingrese la clave para descifrar: "))
        descifrado_Hill(mensaje, clave, abc37)
    if(op>7):
        print("Opción no válida\n")