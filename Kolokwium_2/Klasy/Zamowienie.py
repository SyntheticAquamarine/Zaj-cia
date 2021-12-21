from Klasy.Dieta import Dieta
from Klasy.Pacjent import Pacjent

class Zamowienie:

    _dieta: Dieta
    _pacjent: Pacjent
    _status: str
    _order_id: int

    def __init__(self):
        pass

    @property
    def dieta(self):
        return self._dieta

    @dieta.setter
    def pacjent(self, dieta: Dieta):
        self._dieta = dieta

    @property
    def pacjent(self):
        return self._pacjent

    @pacjent.setter
    def pacjent(self, pacjent: Pacjent):
        self._pacjent = pacjent
    
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: str):
        self._status = status

    @property
    def order_id(self):
        return self._order_id

    @order_id.setter
    def order_id(self, order_id: int):
        self._order_id = order_id

    def __str__(self) -> str:
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s' % vars(self)[item] for item in vars(self))
        )

    def wartosc_zam(self):
        suma = 0.0
        for i in self._dieta:
            suma += i.cena
        return round(suma, 2)

    def adres_pacjenta(self):
        return self._client.adres

