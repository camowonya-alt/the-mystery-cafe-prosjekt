class Karakter:
    def __init__(self, navn):
        self.navn = navn

    def hent_navn(self):
        return self.navn


class Spiller(Karakter):
    def __init__(self, navn):
        super().__init__(navn)
        self.liv = 3
        self.poeng = 0
        self.stjerner = 0
        self.niva = 1

    def legg_til_poeng(self, mengde):
        self.poeng += mengde

    def mist_liv(self):
        self.liv -= 1

    def ga_opp_i_niva(self):
        if self.poeng >= 50:
            self.niva += 1
            self.poeng -= 50


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
    print("☕ Welcome to The Mystery Café! ☕")
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


start_spill()
