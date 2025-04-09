import math
#zmienne - dane
srednicaRurociagu = 0.1
gestoscCieczy = 1200.0
roznicaCisnien = 350.0

def WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien):
    polePrzekroju = math.pi*(math.pow(srednicaRurociagu,2)/4)
    sredniaPredkosc = math.sqrt((2*roznicaCisnien)/gestoscCieczy)
    wyn = polePrzekroju*sredniaPredkosc
    return wyn

def WyznaczenieStrumienMasy(gestoscCieczy, strumienObjetosci):
    wyn = gestoscCieczy * strumienObjetosci
    return wyn
print("Grupa I Zadanie 1. Rurociagiem o srednicy ",srednicaRurociagu,"m transportowano sok o gestosci ",gestoscCieczy,"kg/m^3. Wskazywana przez cisnieniomierz roznica cisnien pomiedzy kroccami rurki Prandtla zamontowanej na rurociagu wynosila ", roznicaCisnien," Pa. Obliczyc strumien objetosci i masy przeplywajacego soku.")
print("Wyniki:")
print('Strumien objetosci (V): ',round(WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien),6),"m^3/s")
print('Strumien masy (m): ',round(WyznaczenieStrumienMasy(gestoscCieczy, WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien)),6),"kg/s")