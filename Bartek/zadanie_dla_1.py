import math
#zmienne - dane
srednicaRurociagu = 0.1
gestoscCieczy = 1200
roznicaCisnien = 350



def WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien):
 u2=2*roznicaCisnien/gestoscCieczy
 u=math.sqrt(u2)
 A=srednicaRurociagu*srednicaRurociagu*math.pi/4
 wyn = A*u
 return wyn;

def WyznaczenieStrumienMasy(gestoscCieczy, strumienObjetosci):
 wyn = gestoscCieczy*strumienObjetosci

 return wyn;


print("Strumien objetosci: ",WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien))
#0.005998577557413504
print("Strumien masy: ",WyznaczenieStrumienMasy(gestoscCieczy, WyznaczenieStrumienObjetosci(srednicaRurociagu, gestoscCieczy, roznicaCisnien)))
#7.198293068896205
