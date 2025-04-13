import math
#zmienne - dane
poziomCieczyWZbiorniku = 8
cisnienieNadCieczaWZbiorniku = 445000
srednicaRury = 0.05
gestoscCieczy = 1000
cisnienieNaZewnatrzZbiornika = 100000
strataCcisnienaNaOporachPrzeplywu = 410000

def PredkoscWyplywu(poziomCieczyWZbiorniku, cisnienieNadCieczaWZbiorniku, gestoscCieczy, cisnienieNaZewnatrzZbiornika, strataCcisnienaNaOporachPrzeplywu):
 #  H + P/(Ro * g) + v1^2/2g = 0 + Pa/(Ro * g) + v^2/2g + strata
 #  H + (P - Pa)/(Ro * g) = v^2/2g + strata
 #  v^2/2g = H + (P - Pa)/(Ro * g) - strata
 #  v = pierwiastek(2 * g * (H + (P - Pa)/(Ro * g) - strata))
 
 przyspieszenieZiemskie=9.81
 
 ulamek1=(cisnienieNadCieczaWZbiorniku-cisnienieNaZewnatrzZbiornika)/(przyspieszenieZiemskie*gestoscCieczy)
 
 strata=strataCcisnienaNaOporachPrzeplywu/(przyspieszenieZiemskie*gestoscCieczy)
 
 #zakladam ze poziom niwelujacy jest w srodku tej rury
 wysokosc = poziomCieczyWZbiorniku - srednicaRury/2
 
 wyn = math.sqrt(2*przyspieszenieZiemskie*(wysokosc+ulamek1-strata))
 return wyn;

def StrumienObjetosci(srednicaRury, predkoscWyplywu):
 #  Q = v * A
 #  A = pi * d^2 / 4

 A = math.pi*srednicaRury**2 /4
 wyn = predkoscWyplywu * A
 return wyn;


print("Predkosc: ",PredkoscWyplywu(poziomCieczyWZbiorniku, cisnienieNadCieczaWZbiorniku, gestoscCieczy, cisnienieNaZewnatrzZbiornika, strataCcisnienaNaOporachPrzeplywu))
#5.144851795727454
print("Strumien objetosci: ",StrumienObjetosci(srednicaRury, PredkoscWyplywu(poziomCieczyWZbiorniku, cisnienieNadCieczaWZbiorniku, gestoscCieczy, cisnienieNaZewnatrzZbiornika, strataCcisnienaNaOporachPrzeplywu)))
#0.010101892878291016
