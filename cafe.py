class Karakter: #superklasse for alle personer i kafeen
    def __init__(self, navn):
        self.__navn = navn #privat attributt

    def hent_navn(self):
        return self.__navn 


class Kunde(Karakter): #spilleren, arver fra Karakter klassen
    
    def __init__(self, navn):
        super().__init__(navn)
        self.__liv = 3
        self.__poeng = 0
        self.__stjerner = 0
        self.__niva = 1
        self.__valgt_oppskrift = None

    #get metoder
    def hent_liv(self):
        return self.__liv

    def hent_poeng(self):
        return self.__poeng

    def hent_stjerner(self):
        return self.__stjerner

    def hent_niva(self):
        return self.__niva

    def hent_valg(self):
        return self.__valgt_oppskrift

    def velg_oppskrift(self, oppskrift):
        self.__valgt_oppskrift = oppskrift

    def legg_til_poeng(self, mengde):
        self.__poeng += mengde

    def legg_til_stjerne(self):
        self.__stjerner += 1
        
    def mist_liv(self):
        self.__liv -= 1

    def er_i_live(self):
        return self.__liv > 0

    def ga_opp_i_niva(self): #går opp ett nivå hvis nok poeng
        if self.__poeng >= self.__niva * 20:
            self.__niva += 1

class Ansatt(Karakter): #jobber i kafeen. arver fra karakter

    def __init__(self, navn, oppskrifter):
        super().__init__(navn)
        self.__oppskrifter = oppskrifter

    def hent_oppskrifter(self):
        return self.__oppskrifter

    def server(self, kunde):
        oppskrift = kunde.hent_valg()
        print (f"{self.hent_navn()} serves {oppskrift.hent_navn()} to {kunde.hent_navn()}.")


class Sporsmal: #en quiz med et riktig svar
    def __init__(self, sporsmalstekst, riktig_svar):
        self.__sporsmalstekst = sporsmalstekst
        self.__riktig_svar = riktig_svar

    def hent_tekst(self):
        return self.__sporsmalstekst

    def sjekk_svar(self, svar): #dette ignorerer store og små bojstaver og mellomrom rundt svaret
        return svar.strip().lower() == self.__riktig_svar.lower()


class Oppskrift: #en oppskrift, er låst til kunden har høyt nok nivå
    def __init__(self, navn, krevd_niva):
        self.__navn = navn
        self.__krevd_niva = krevd_niva
        self.__last = True #betyr at oppskriften er låst

    def hent_navn(self):
        return self.__navn

    def er_last(self):
        return self.__last

    def las_opp(self, kunde): 
        if kunde.hent_niva() >= self.__krevd_niva:
            self.__last = False


class Kafe: #styrer spillet har en ansatt, kunden er spilleren
    def __init__(self, kunde):
        self.__kunde = kunde

        self.__oppskrifter = [
           Oppskrift("Latte", 1),
           Oppskrift("Croissant", 2),
           Oppskrift("Cheesekake", 3)
        ]
        self.__ansatt = Ansatt("Sam", self.__oppskrifter)

        self.__spormsal_liste = [
            Sporsmal("What is the main ingredient in bread?", "flour"),
            Sporsmal("What drink is made with espresso and steamed milk?", "latte"),
            Sporsmal("What ingredient makes cakes rise?", "baking powder"),
            Sporsmal("What is the main ingredient in cheesecake?", "cream cheese"),
            Sporsmal("Which country is famous for croissants?", "france"),
            Sporsmal("What do you call coffee with chocolate and milk?", "mocha"),
            Sporsmal("What sweet ingredient is made by bees?", "honey")
        ]
        self.sjekk_lasopp()

    def sjekk_lasopp(self): #låser opp oppskrifter som kunden har høyt nok nivå til
        for oppskrift in self.__oppskrifter:
            if oppskrift.er_last():
                oppskrift.las_opp(self.__kunde)
                if not oppskrift.er_last():
                    print(f"New recipe unlocked: {oppskrift.hent_navn()}!!!")

    def gi_oppskrift(self): #kunden får ny låst opp oppskrift
        nyeste = None
        for oppskrift in self.__oppskrifter:
            if not oppskrift.er_last():
                nyeste = oppskrift
        self.__kunde.velg_oppskrift(nyeste)


    def still_sporsmal(self, sporsmal):
        oppskrift = self.__kunde.hent_valg()
        print(f"\nAnswer to get your {oppskrift.hent_navn()}!!")
        print(sporsmal.hent_tekst())
        svar = input ("Your answer: ")

        if sporsmal.sjekk_svar(svar):
            print("Correct! +10 points! ⭐")
            self.__ansatt.server(self.__kunde)
            self.__kunde.legg_til_poeng(10)
            self.__kunde.legg_til_stjerne()
            self.__kunde.ga_opp_i_niva()
            self.sjekk_lasopp()
        else:
            print("Wrong answer! You lost one life.")
            self.__kunde.mist_liv()


    def vis_status(self):
        print("Points:", self.__kunde.hent_poeng())
        print("Lives:", self.__kunde.hent_liv())
        print("Stars:", self.__kunde.hent_stjerner(), "⭐")
        print("Level:", self.__kunde.hent_niva())

    def start(self):
        for sporsmal in self.__spormsal_liste:
            self.gi_oppskrift()
            self.still_sporsmal(sporsmal)
            self.vis_status()
            if not self.__kunde.er_i_live():
                print ("GAME OVER!")
                break
        self.avslutt()

    def avslutt(self):
        print("\nThanks for playing The Mystery Cafe!")
        print("Final points:", self.__kunde.hent_poeng())
        print("Total stars:", self.__kunde.hent_niva(), "⭐")


def start_spill():
    print("Welcome to The Mystery Café! ☕")
    kunde = Kunde(input("Enter your name: "))
    kafe = Kafe(kunde)
    kafe.start()

if __name__ == "__main__":
    start_spill() #hindrer at spillet startr når en annen fil henter noe fra det (test.py)