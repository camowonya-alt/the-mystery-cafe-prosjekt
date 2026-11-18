import random

class Karakter: #superklasse for alle personer i kafeen
    def __init__(self, navn):
        self.__navn = navn #privat attributt

    def hent_navn(self):
        return self.__navn 


class Ansatt(Karakter): #spilleren, arver fra Karakter klassen
    poeng_per_niva = 20 #hvor mange poeng som trengs for å gå opp ett nivå
    
    def __init__(self, navn):
        super().__init__(navn)
        self.__liv = 3
        self.__poeng = 0
        self.__stjerner = 0
        self.__niva = 1

    #get metoder
    def hent_liv(self):
        return self.__liv

    def hent_poeng(self):
        return self.__poeng

    def hent_stjerner(self):
        return self.__stjerner

    def hent_niva(self):
        return self.__niva


    def legg_til_poeng(self, mengde):
        self.__poeng += mengde

    def legg_til_stjerne(self):
        self.__stjerner += 1
        
    def mist_liv(self):
        self.__liv -= 1

    def ga_opp_i_niva(self): #går opp ett nivå hvis nok poeng, retunerer true hvis nivået økte
        if self.__poeng >= self.poeng_per_niva:
            self.__niva += 1
            self.__poeng -= self.poeng_per_niva
            return True
        return False

    def server(self, kunde): #serverer opskriften kunden har valgt lol
        oppskrift = kunde.hent_valg()
        print(f"{self.hent_navn()} serves {oppskrift.hent_navn()} to {kunde.hent_navn()}.")


class Kunde(Karakter): #en kunde i kafee. arver fra Karakter og kan kun velge en oppskrift

    def __init__(self, navn):
        super().__init__(navn)
        self.__valgt_oppskrift = None 

    def velg_oppskrift(self, oppskrift):
        self.__valgt_oppskrift = oppskrift

    def hent_valg(self):
        return self.__valgt_oppskrift


class Sporsmal:
    def __init__(self, sporsmalstekst, riktig_svar):
        self.sporsmalstekst = sporsmalstekst
        self.riktig_svar = riktig_svar

    def sjekk_svar(self, svar):
        return svar.lower() == self.riktig_svar.lower()


class Oppskrift:
    def __init__(self, navn, krevd_niva):
        self.navn = navn
        self.krevd_niva = krevd_niva
        self.last = False

    def las_opp(self, spiller):
        if spiller.niva >= self.krevd_niva:
            self.last = True


def spill_quiz(spiller, sporsmal):
    print("\n" + sporsmal.sporsmalstekst)
    svar = input("Your answer: ")

    if sporsmal.sjekk_svar(svar):
        print("Correct! +10 points! ⭐")
        spiller.legg_til_poeng(10)
        spiller.stjerner += 1
    else:
        print("Wrong answer! You lost one life.")
        spiller.mist_liv()

    spiller.ga_opp_i_niva()

    print("Points:", spiller.poeng)
    print("Lives:", spiller.liv)
    print("Stars:", spiller.stjerner, "⭐")
    print("Level:", spiller.niva)

    if spiller.liv == 0:
        print("GAME OVER!")
        return False

    return True


def start_spill():
    print("Welcome to The Mystery Café! ☕")
    spiller = Spiller(input("Enter your name: "))

    sporsmal_liste = [
        Sporsmal("What is the main ingredient in bread?", "flour"),
        Sporsmal("What drink is made with espresso and steamed milk?", "latte"),
        Sporsmal("What ingredient makes cakes rise?", "baking powder"),
        Sporsmal("What is the main ingredient in cheesecake?", "cream cheese"),
        Sporsmal("Which country is famous for croissants?", "france"),
        Sporsmal("What do you call coffee with chocolate and milk?", "mocha"),
        Sporsmal("What sweet ingredient is made by bees?", "honey")
    ]

    for sporsmal in sporsmal_liste:
        if not spill_quiz(spiller, sporsmal):
            break

    print("\nThanks for playing The Mystery Café!")
    print("Final points:", spiller.poeng)
    print("Total stars:", spiller.stjerner, "⭐")
    print("Final level:", spiller.niva)

if __name__ == "__main__":
    start_spill() #hindrer at spillet startr når en annen fil henter noe fra det (test.py)