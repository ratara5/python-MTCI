while True:
    num=int(input("Por favor ingrese un número: "))
    s=[1,num] #Cualquier número es divisible por la unidad y por sí mismo. Así que la lista inicia con esos dos elementos
    for i in range(2,num):
        if num%i==0: #Verificar el módulo de la división entre el número y cualquier natural menos el número mismo...
            s.append(i) #si es 0, entonces el número se agrega a la lista
    if len(s)==2: #Si la lista solo tiene los dos elementos iniciales, entonces el número es primo
        print("El número "+str(num)+" es primo")
    else: #Si la lista tiene más elementos aparte de los dos iniciales, entonces el número no es primo
        print("El número "+str(num)+" NO es primo y es divisible por: "+str(s))
    if str(num)[0]=="-":
        print("El número "+str(num)+" es negativo")