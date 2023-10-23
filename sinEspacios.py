def reemplazar(texto):
    texto = texto.lower()
    especiales = " .,\n"
    tildes = [("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u")]
    for i in especiales:
        texto = texto.replace(i, "")
    for i in tildes:
        texto = texto.replace(i[0], i[1])
    return texto


def contar(texto):
    dic = {}
    for i in texto:
        cont = 0
        for j in texto:
            if i == j:
                cont += 1
                dic[i] = cont
    return dic


def retornaTupla(dic):
    dicOrdenado = sorted(dic.items(), key=lambda x: x[1])
    return dicOrdenado


def devuelveTupla(listTupla):
    tuplaCortada = []
    tuplaOrdenada = sorted(listTupla, key=lambda x: x[1], reverse=True)
    aux = tuplaOrdenada[0][1]
    for i in tuplaOrdenada:
        if i[1] == aux:
            tuplaCortada.append(i)
        else:
            break
    return tuplaCortada


def lista(listaTuplaMsj):
    lista = []
    for i in listaTuplaMsj:
        lista.append(i[0].upper())
    return lista


def funcionMayor(grantexto):
    pass


texto = """ Si encuentras a una persona así, alguien a quien puedas abrazar y con la que
puedas cerrar los ojos a todo lo demás, puedes considerarte muy afortunado. 
Aunque solo dure un minuto, o un día.uuuuu """


texto2 = reemplazar(texto)
print(texto2)
print()
dic = contar(texto2)
print(dic)
print()
listTupla = retornaTupla(dic)
print(listTupla)
print()
listTuplaMayor = devuelveTupla(listTupla)
print(listTuplaMayor)
print()
listaMayores = lista(listTuplaMayor)
print(
f"Los caracateres que mas se repitieron con {listTuplaMayor[0][1]} repeticiones son:"
)
for i in listaMayores:
    print("-", i)
