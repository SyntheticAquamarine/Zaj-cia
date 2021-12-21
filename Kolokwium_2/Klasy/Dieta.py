class Dieta():

    def __init__(self, pesel: int, produkty: str, dozowanie: str, cena: float) -> None:
        self._pesel = pesel
        self._produkty = produkty
        self._dozowanie = dozowanie
        self._cena = cena

    @property
    def pesel(self):
        return self._pesel

    @property
    def produkty(self):
        return self._produkty

    @property
    def dozowanie(self):
        return self._dozowanie

    @property
    def cena(self):
        return self._cena

    def __str__(self) -> str:
        return f'{self._pesel}, dieta: {self._produkty}\
             {self._dozowanie}, cena: {self._cena}'
    
