import numpy as np

# zmienne - dane

srednicaRurociagu = 0.1
gestoscCieczy = 1200

# cisnienie dynamiczne
# poniewaz rurka Prandtla
roznicaCisnien = 350

# stale

PI = 3.141592

def predkosc(rho, pd):
  predkosc2 = 2 * pd / rho
  return np.sqrt(predkosc2)

def WyznaczenieStrumienObjetosci(d, v):
  pole = PI * (d ** 2) / 4.0
  strumien = pole * v
  return strumien

def WyznaczenieStrumienMasy(rho, V):
  return rho * V

v = predkosc(gestoscCieczy, roznicaCisnien)
V = WyznaczenieStrumienObjetosci(srednicaRurociagu, v)
m = WyznaczenieStrumienMasy(gestoscCieczy, V)

print(f'Predkosc v = {v:.2} m/s')
print(f'Strumien objetosci V = {V:.2} m^3 / s')
print(f'Strumien masy m = {m:.2} kg / s')