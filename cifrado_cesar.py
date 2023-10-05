# Recibe el número k que recorre el abecedario a la izquierda
# el mensaje a cifrar, el abecedario e idioma que se utiliza
def cifrado_cesar_k(k, mensaje,abc):
    cifrado = ""
    for i in mensaje:
        # Obtiene la posición de la letra cifrada en el abecedario y lo añade al array de mensaje cifrado
        index_abc = (abc.index(i)+k) % len(abc)
        cifrado += abc[index_abc]
    return cifrado


# Recibe una clave para cifrar el abecedario el mensaje a cifrar, el abecedario e idioma que se utiliza
# cifrar es un booleano que indica cuando hay que cifrar(1) o descifrar(0) el mensaje recibido 
def cifrado_cesar_clave_uno(clave,mensaje,abc,cifrar):
    cifrado = ""
    abc_cifrado = []
    # Crea el nuevo abecedario con clave
    for i in clave:
        if i not in abc_cifrado:
            abc_cifrado.append(i)
    # Añade el resto del abecedario
    for i in abc:
        if i not in clave: 
            abc_cifrado.append(i)
    
    # Condición para cifrado o descifrado
    for i in mensaje:
        if(cifrar):
        # Cifra el mensjae
            indice = abc.index(i)
            cifrado += (abc_cifrado[indice])
        else:
        # Descifra el mensaje
            indice = abc_cifrado.index(i)
            cifrado +=abc[indice]

    return cifrado

# Recibe una clave para cifrar , el mensaje a cifrar, el abecedario e idioma que se utiliza
# cifrar es un booleano que indica cuando hay que cifrar(1) o descifrar(0) el mensaje recibido 
def cifrado_cesar_clave_dos(clave,mensaje,abc,cifrar):
    cifrado = ""
    indices = []
    # Cifrado
    if (cifrar):
        for i in range (len(mensaje)):
            # crea el índice del mensaje cifrado sumando los índices del mensaje y la clave letra por letra
            indice = int(abc.index(mensaje[i])) + int(abc.index(clave[i]))
            # aseguramos que sea del tamaño del abecedario español
            if (indice > len(abc)):
                indice -= len(abc)
            # obtiene la letra de acuerdo a la suma de índices
            cifrado += abc[indice]
    else:
        # Descifrar
        for i in range (len(mensaje)):
            # crea el del mensaje cifrado restando los índices del mensaje cifrado y la clave letra por letra
            indice = int(abc.index(mensaje[i])) - int(abc.index(clave[i]))
            # aseguramos que la resta sea positiva, en caso contrario, se suma las letras del abecesario para obtener positivos
            if (indice<0):
                indice += len(abc)
            cifrado += abc[indice]
    
    return cifrado


esp = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
ingl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
k = 7

op=0
while(op!=7):
    print("\n\t\t***** Menú *****")
    print("1. Cifrar con César (k=3)\n",
                "2. Descrifrar César (k=3)\n",
                "3. Cifrar con César (clave)\n",
                "4. Descrifrar César (clave)\n",
                "5. Cifrar con César (clave y mensaje del mismo tamaño)\n",
                "6. Descrifrar César (clave y mensaje del mismo tamaño)\n",
                "7. Salir")

    op = int(input("Elija una opción: "))
    if(op==1):
        print("***** Algoritmo de Cifrado César (k=3) *****")
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        print("Su mensaje cifrado es: ",cifrado_cesar_k(k, mensaje.lower(),esp))
    if(op==2):
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        print("***** Algoritmo de Descrifrado César (k=3) *****")
        print("Su mensaje descifrado es: ",cifrado_cesar_k(-k, mensaje.lower(),esp))
    if(op==3):
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        clave = str(input("Ingrese la clave para cifrar: "))
        print("***** Algoritmo de Descrifrado César (clave) *****")
        print("Su mensaje cifrado es: ",cifrado_cesar_clave_uno(clave.lower(),mensaje.lower(),esp,1))
    if(op==4):
        print("***** Algoritmo de Descrifrado César (clave) *****")
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        clave = str(input("Ingrese la clave para descifrar: "))
        print("Su mensaje descifrado es: ",cifrado_cesar_clave_uno(clave.lower(),mensaje.lower(),esp,0))
    if(op==5):
        print("***** Algoritmo de Descrifrado César (clave) *****")
        mensaje = str(input("Ingrese el mensaje a cifrar: "))
        clave = str(input("Ingrese la clave para cifrar: "))
        print("Su mensaje descifrado es: ",cifrado_cesar_clave_dos(clave.lower(),mensaje.lower(),esp,1))
    if(op==6):    
        print("***** Algoritmo de Descrifrado César (clave) *****")
        mensaje = str(input("Ingrese el mensaje a descifrar: "))
        clave = str(input("Ingrese la clave para descifrar: "))
        print("Su mensaje descifrado es: ",cifrado_cesar_clave_dos(clave.lower(),mensaje.lower(),esp,0))    
    if(op>7):
        print("Opción no válida\n")

