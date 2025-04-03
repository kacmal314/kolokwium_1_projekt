
# ile miejsc po przecinku

dokladnosc = 4

# zmienne - dane

poziomCieczyWZbiorniku = 8.0
cisnienieNadCieczaWZbiorniku = 445000.0
srednicaRury = 0.05
gestoscCieczy = 1000.0
cisnienieNaZewnatrzZbiornika = 100000.0
strataCisnienaNaOporachPrzeplywu = 410000.0

wysokoscDoLiniiNiwelujacej = poziomCieczyWZbiorniku - (srednicaRury / 2.0)
przyspieszenieGrawitacyjne = 9.81

PI = 3.141592

def PredkoscWyplywu():

  # przeksztalcenie rownania Bernouliego dla cieczy burzliwej
  # zakladam cisnienie dynamiczne 1. = 0 ∵ staly poz. A-A
  # zakladam alpha = 1
  
  # v2 = sqrt(2 * (p1 - p2 - dp + z1 * rho * g) / rho)
  
  cisnienia = cisnienieNadCieczaWZbiorniku - cisnienieNaZewnatrzZbiornika - strataCisnienaNaOporachPrzeplywu
  
  cisnienieZEnergiiPotencjalnej = wysokoscDoLiniiNiwelujacej * gestoscCieczy * przyspieszenieGrawitacyjne
  
  predkosc = (2 * (cisnienia + cisnienieZEnergiiPotencjalnej) / gestoscCieczy) ** (0.5)
  
  return predkosc

def StrumienObjetosci():
  
  polePowierzchniRury = (PI * (srednicaRury ** 2)) / 4.0
  
  strumien = polePowierzchniRury * PredkoscWyplywu()

  return strumien

print(f'Predkosc wyplywu v = {PredkoscWyplywu():{0}.{dokladnosc}}')
print(f'Strumien objetosci V = {StrumienObjetosci():{0}.{dokladnosc}}')
