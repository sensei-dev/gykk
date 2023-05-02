lista = []

for x in range(5):
    gyumolcs = input("Kérem a gyümölcs nevét ")
    lista.append(gyumolcs)

db = lista.count("alma")


vanbenne = False

for x in lista:
    if x == "banán":
        vanbenne = True
    break


dba = 0
for x in lista: 
    if x[0] == "a":
        dba += 1 



ki = open("gyumolcsok.txt", "w", encoding = "utf-8")
ki.write("A listában lévő almák száma: " +str(db) + "\n" )


if vanbenne: 
    ki.write("A listaban van banan" + "\n")
else: 
    ki.write("A listaban nincs bánan" + "\n")

ki.write("A listában a betüvel kezdodok gyumolcsok szama: " + str(dba) )

ki.close()
