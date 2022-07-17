doc={"Fruteria":
 [
  {"Fruta":
   [
    {"Nombre":"Manzana","Cantidad":10},
    {"Nombre":"Pera","Cantidad":20},
    {"Nombre":"Naranja","Cantidad":30}
   ]
  },
  {"Verdura":
   [
    {"Nombre":"Lechuga","Cantidad":80},
    {"Nombre":"Tomate","Cantidad":15},
    {"Nombre":"Pepino","Cantidad":50}
   ]
  }
 ]
}

itemFruver=[]
cantidadesFruver=[]
for tipo in doc["Fruteria"]: #doc(fruteria) es una lista//tipo es un diccionario
    for nombre, cosa in tipo.items(): #cosa es una lista
        for it in cosa: #item es un diccionario
            itemFruver.append(it["Nombre"])
            cantidadesFruver.append(it["Cantidad"])
a=list(zip(itemFruver,cantidadesFruver))

for items, cantidades in a:
    print("Los(as) "+str(items)+"s son: "+str(cantidades))