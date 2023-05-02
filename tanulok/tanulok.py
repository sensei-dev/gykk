ki = open("tanulok.txt", "w")



for x in range(5):
    nev = input("Kérem a nevet: ")
    kor = int(input("Kérem a kort: "))

    ki.write(nev + " " + kor + "\n")

ki.close