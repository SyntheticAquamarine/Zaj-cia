from Klasy.Osoba import Osoba

class Pacjent(Osoba):

    def __init__(self, imie: str, nazwisko: str, pesel: int, adres: str, choroba: str, oddzial: str):
        super().__init__(imie, nazwisko, pesel, adres)
        self._choroba = choroba
        self._oddzial = oddzial
    
    @property
    def choroba(self):
        return self._choroba

    @property
    def oddzial(self):
        return self._oddzial

def __str__(self) -> str:
    return f'imie {self._imie} nazwisko: {self._nazwisko},\
         pesel: {self._pesel}, choroba: {self._choroba}\
              polozenie w szpitalu: {self._oddzial}'