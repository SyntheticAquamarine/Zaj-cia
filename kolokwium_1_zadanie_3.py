class Produkt:
    def __init__(self, ID:int, nazwa: str, rozmiar:str, pochodzenie:str, kategoria:str):
        self.ID = ID
        self.nazwa = nazwa
        self.rozmiar = rozmiar
        self.pochodzenie = pochodzenie
        self.kategoria = kategoria
    def products(self):
        return self.ID
        return self.nazwa
        return self.rozmiar
        return self.pochodzenie
        return self.kategoria
    def __str__(self):
        return f"ID: {self.ID}, nazwa: {self.nazwa}, rozmiar: {self.rozmiar}, \
            pochodzenie: {self.pochodzenie}, kategoria: {self.kategoria}"


class Magazyn:
    def __init__(self, Kraj, Miasto, adres, numer_magazynu, nr_tel):
        self.Kraj = Kraj
        self.Miasto = Miasto
        self.adres = adres
        self.Numer_Magazynu = numer_magazynu
        self.nr_tel - nr_tel
    def mag(self):
        return self.Kraj
        return self.Miasto
        return self.adres
        return self.Numer_Magazynu
        return self.nr_tel
    def __str__(self):
        return f"Kraj {self.Kraj}, Miasto {self.Miasto}, adres {self.adres}, mumer magazynu {self.Numer_Magazynu}, numer telefonu {self.nr_tel}"

class KlientDetaliczny:
    def __init__(self, Imie, Nazwisko, adres, Nr_tel, E_mail):
        self.Imie = Imie
        self.Nazwisko = Nazwisko
        self.adres = adres
        self.Nr_tel = Nr_tel
        self.E_mail = E_mail
    def customer(self):
        return self.Imie
        return self.Nazwisko
        return self.adres
        return self.Nr_tel
        return self.E_mail

    def __str__(self):
        return f"Imie: {self.Imie}, Nazwisko {self.Nazwisko}, adres {self.adres}, nr_tel {self.Nr_tel}, e-mail {self.E_mail}"


class Zamowienie(KlientDetaliczny):
    def __init__(self, Imie, Nazwisko, adres, Nr_tel, E_mail, ID:int, nazwa: str, rozmiar:str, pochodzenie:str, kategoria:str, cena: int, klient):
        super().__init__(Imie, Nazwisko, adres, Nr_tel, E_mail)
        self.ID = None
        self.nazwa = None
        self.rozmiar = None
        self.pochodzenie = None
        self.kategoria = None
        self.cena = None
        self.klient = None
    def Zam(self):
        return self.ID
        return self.nazwa
        return self.rozmiar
        return self.pochodzenie
        return self.kategoria
        return self.cena
        return self.klient

    def setter(self, val1, val2, val3, val4, val5, val6, val7):
        self.ID = val1
        self.nazwa = val2
        self.rozmiar = val3
        self.pochodzenie = val4
        self.kategoria = val5
        self.cena = val6
        self.klient = val7

    def wyliczenie(self):
        wartosc = 0
        wartosc+=self.cena


    def adres(self):
        return super().self.adres

    
    def __str__(self):
        return f"ID: {self.ID}, nazwa: {self.nazwa}, rozmiar: {self.rozmiar}, \
            pochodzenie: {self.pochodzenie}, kategoria: {self.kategoria}, klient: {self.klient}"

class KlientBiznesowy:
    def __init__(self, Nazwa, Adres, NIP, nr_tele, e_mail):
        self.Nazwa = Nazwa
        self.Adres = Adres
        self.Nip = NIP
        self.nr_tele = nr_tele
        self.e_mail = e_mail

    def biz(self):
        return self.Nazwa
        return self.Adres
        return self.Nip
        return self.nr_tele
        return self.e_mail

    def __str__(self):
        return f"Nazwa {self.Nazwa}, Adres {self.Adres}, NIP {self.Nip}, Nr telefonu {self.nr_tele}, e-mail {self.e_mail}"


        