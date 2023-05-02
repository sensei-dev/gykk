#felhasznalo altal toltsunk fel egy listat 10db egesz szammal
#a.) statisztika.txt-be kiiras 
#b.) a lista legkisebb es legnagyobb eleme
#c.) atlagoljuk oket, es  2tizedes jeggyel irassuk ki.
#d.) elso eleme
#e.) utolso eleme
#f.) hany db paros szam van ebbe a listaban
#g.) van e benne 3-al oszthato szam



lista = []

for x in range(10): 
    szam = int(input("Kérlek add meg a számot : "))
    lista.append(szam)

mini =min(lista)

maxi = max(lista)

hosszu = len(lista)



ossz = 0 
for x in lista:
    ossz += x
atlag = ossz / hosszu

db = 0 
for x in lista: 
    if x %2 == 0:
        db += 1 

vanbenne = False

for x in lista: 
    if x %3 == 0 : 
        vanbenne = True

   
    

ki = open("statisztika.txt", "w")

ki.write("A lista legkisebb eleme:" + " " + str(mini) + "\n")
ki.write("A lista legkisebb eleme:" + " " + str(maxi) + "\n")
ki.write("A lista elemeinek átlaga::  {:.2f}".format(atlag) + "\n")
ki.write("A lista első eleme: " + " " + str(lista[0]) + "\n")
ki.write("A lista utolso eleme: " + " " + str(lista[-1]) + "\n")
ki.write("A listaban levo paros szamok db: " + " " + str(db) + "\n")

if vanbenne:
    ki.write("A listaban van 3-al oszthato szam")
else:
    ki.write("A listaban nincsen 3al oszthato szam")
    
    
ki.close()