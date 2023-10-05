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

# Cifrado
def afin_cifrado(mensaje,a,b,abc):
    cifrado = ""
    n = len(abc)
    if( modinv(a, n) != -1):
        for i in mensaje:
            # Cifrado Ci = (a * Mi + b) mod n
            ci = ((a*abc.index(i))+b) % n
            cifrado += abc[ci]
    return cifrado
 
 # Descifrado
def afin_descifrado(mensaje,a,b,abc):
    descifrado = ""
    n = len(abc)
    a_inv = modinv(a, n)
    for i in mensaje:
        mi = ((a_inv*abc.index(i))-b)%n
        descifrado += abc[mi]
    return descifrado
     
     
x = 1
b = 7
mensaje = "Por mi raza hablara el espiritu"

abc =  ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
mensaje_cifrado = afin_cifrado(mensaje.replace(" ", "").lower(),x,b,abc)
print("Mensaje original: ",mensaje, "\nCifrando... \nMensaje cifrado: ", mensaje_cifrado)

print("Descifrando... \nMensaje original:  ", afin_descifrado(mensaje_cifrado,x,b,abc))

