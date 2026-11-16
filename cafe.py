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


class Sporsmal:
    def __init__(self, sporsmalstekst, riktig_svar):
        self.sporsmalstekst = sporsmalstekst
        self.riktig_svar = riktig_svar


class Oppskrift:
    def __init__(self, navn, krevd_niva):
        self.navn = navn
        self.krevd_niva = krevd_niva
        self.last = False

        # Testing av klassene

spiller1 = Spiller("Camila")

print("Welcome to The Mystery Café!")
print("Player:", spiller1.hent_navn())
print("Lives:", spiller1.liv)
print("Points:", spiller1.poeng)
print("Stars:", spiller1.stjerner)
print("Level:", spiller1.niva)