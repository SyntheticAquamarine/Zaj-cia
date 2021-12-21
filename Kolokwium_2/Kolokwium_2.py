from Klasy.Dieta import Dieta
from Klasy.Pacjent import Pacjent
from Klasy.Zamowienie import Zamowienie
from Klasy.Dietetyk import Dietetyk


dieta = Dieta(980917704487, ['bulka tarta', 'kalafior','ogorek'], "3 razy dziennie", "14,99")
pacjent = Pacjent("Jan","Kowalski",980917704487,"Piekary śląskie Jaworowa 12", "zapalenie stawow", "oddzial 4 pokoj 516")
lekarz = Dietetyk("Jan", "Tracz", 760912204401,"katowice aleje Jerozolimskie","Brak wolnych miejsc","Uniwersytet medyczny we Wrocławiu")


zam = Zamowienie()
zam.pacjent = pacjent
zam.dieta = dieta
zam.order_id = 8
zam.status = "wyslane"