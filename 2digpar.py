while True:
    num=input("Por favor ingrese un número de dos dígitos: ")
    mod1=int(num[0])%2
    mod2=int(num[1])%2
    if mod1==0:
        print("El primer dígito de "+num+" es par")
    else:
        print("El primer dígito de " + num + " NO es par")
    if mod2 == 0:
        print("El segundo dígito de " + num + " es par")
    else:
        print("El segundo dígito de " + num + " NO es par")