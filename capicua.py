def sintilde(s):
    reemplazos = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
    )
    for a, b in reemplazos:
        s = s.replace(a, b).replace(a.upper(), b.upper())
    return s

ph=input("Por favor, ingrese la frase")
frase=sintilde(ph.replace(" ","").lower().rstrip("."))
frasenueva=""
for i in range(1,len(frase)+1):
    frasenueva+=frase[len(frase)-i]
print(frase+"\n"+frasenueva)
if frase==frasenueva:
    print("La frase: '"+ph+"' es palíndromo")


