
def verificarnumero(numero):
    """ESTA FUNCION VERIFICA NUMERO
    :param numero:
    numero=int
    """
    if (numero % 2) == 0:
       print ("par")
    else:
       print ("impar")

def bienvenido():
    """
    la funcion bienvenido imprime
    un mensaje de bienvenida
    """
    print('HOLA...')
    """saludo """
    print('escribe un numero')

if __name__=="__main__":

    reinicio=True
    """ reinicio del programa"""
    while reinicio:
        print('\n\n')
        bienvenido()
        """ejecucion de la funcion"""


        numero=int(input('numero: \n'))
        reinicio=False
        verificarnumero(numero)



