import random #Unosenje potrebne biblioteke

broj = int(input("Python: Do kojeg broja da izaberem? ")) #Unos do kojeg broja da se bira nasumicni broj
a = random.randrange(0, broj) #Dobijanje nasumicnog proja
isItPlaying = True #Pokretanje igre
brojPokusaja = 0 # Inicijalizacija broja pokusaja

while(isItPlaying): # Pokretanje While Loopa
    brojPokusaja += 1 # Broj Pokusaja se uvecava svakim obrtanjem While loopa za 1
    trenutniB = int(input("Python: Unesi Broj: ")) # Primamo unos korisnika

    if(a > trenutniB): # Proveravanje da li je nasumicni broj Veci od "Zamisljenog"
        print("Python: Unesen Broj je veci od broja koji sam zamislio")
        continue #Nastavljanje u petlju

    if(a < trenutniB): # Proveravanje da li je nasumicni broj MANJI od "Zamisljenog"
        print("Python: Uneseni Broj je manji od broja koji sam zamislio")
        continue
    else: # Else odnosno ostalo je samo da je broj tacana
        print("Pogodio Si!!!!!")
        print(f"Python: Porazen sam u {brojPokusaja} pokusaja Ahh tuga....") # Broj pokusaja se prikazuje u vidu zanimljive poruke
        print("Python: Mislim da sam omatorio...")
        print("Vreme je za penziju")
        isItPlaying = False # Prekidanje While loopa postavljanjem promenjive na False


