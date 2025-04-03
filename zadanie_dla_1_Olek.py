import math

# zmienne - dane
srednicaRurociagu = 0.1  # średnica w metrach
gestoscCieczy = 1200      # gęstość w kg/m³
roznicaCisnien = 350      # różnica ciśnień w Pa

def WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien):
    pole_przekroju = math.pi * (srednicaRurociagu ** 2) / 4
    predkosc = math.sqrt((2 * roznicaCisnien) / gestoscCieczy)
    wyn = predkosc * pole_przekroju
    return wyn

def WyznaczenieStrumienMasy(gestoscCieczy, strumienObjetosci):
    wyn = gestoscCieczy * strumienObjetosci
    return wyn

print("V objętości: ",WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien))
print("V masy: ",WyznaczenieStrumienMasy(gestoscCieczy, WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien)))
