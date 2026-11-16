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

        # Testing av klassene

spiller1 = Spiller("Camila")

print("Welcome to The Mystery Café!")
print("Player:", spiller1.hent_navn())
print("Lives:", spiller1.liv)
print("Points:", spiller1.poeng)
print("Stars:", spiller1.stjerner)
print("Level:", spiller1.niva)

spiller1.legg_til_poeng(10)
print("New points:", spiller1.poeng)

spiller1.mist_liv()
print("Remaining lives:", spiller1.liv)

spiller1.legg_til_poeng(50)
spiller1.ga_opp_i_niva()
print("New level:", spiller1.niva)