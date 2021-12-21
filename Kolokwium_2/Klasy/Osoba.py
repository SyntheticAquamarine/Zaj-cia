class Osoba:

    def __init__(self, imie: str, nazwisko: str, pesel: int, adres: str) -> None:
        self._imie = imie
        self._nazwisko = nazwisko
        self._pesel = pesel
        self._adres = adres

    @property
    def imie(self):
        return self._imie

    @property
    def nazwisko(self):
        return self._nazwisko

    @property
    def pesel(self):
        return self._pesel   

    @property
    def adres(self):
        return self._adres

def __str__(self) -> str:
        return f'{self._imie} {self._nazwisko},\
            pesel: {self._pesel}, adres: {self._adres}'