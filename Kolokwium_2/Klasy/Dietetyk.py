from Klasy.Osoba import Osoba

class Dietetyk(Osoba):

    def __init__(self, imie: str, nazwisko: str, pesel: int, adres: str, rezerwacja: str, dyplom: str):
        super().__init__(imie, nazwisko, pesel, adres)
        self._rezerwacja = rezerwacja
        self._dyplom = dyplom

    @property
    def rezerwacja(self):
        return self._rezerwacja

    @property
    def dyplom(self):
        return self._dyplom

def __str__(self) -> str:
        return f'{self._imie} {self._nazwisko},\
            pesel: {self._pesel}, adres: {self._rezerwacja},\
                dietetyk: {self._dyplom}'

