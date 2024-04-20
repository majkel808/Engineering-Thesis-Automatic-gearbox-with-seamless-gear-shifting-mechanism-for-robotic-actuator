import numpy as np
import matplotlib.pyplot as plt

# Parametry krzywej cykloidalnej
R = 45
Rr = 2
E = .75
N = 51




#R = 45
#Rr = 2
#E = .75 

#N = 51

# Zakres zmiennej t od 0 do 360 stopni
t = np.linspace(0, 2 * np.pi, 7000)

#t = np.pi / 6
# Wzory na współrzędne X i Y
PSI =  np.arctan(np.sin((1 - N) * t) / ((R / (E * N)) - np.cos((1 - N) * t)))
Cx = (R * np.cos(t)) - (Rr * np.cos(t + np.arctan(np.sin((1 - N) * t) / ((R / (E * N)) - np.cos((1 - N) * t))))) - (E * np.cos(N * t))
Cy = (-R * np.sin(t)) + (Rr * np.sin(t + np.arctan(np.sin((1 - N) * t) / ((R / (E * N)) - np.cos((1 - N) * t))))) + (E * np.sin(N * t))


# Wykres
plt.figure(figsize=(8, 8))  
plt.plot(Cx, Cy, label="Krzywa cykloidalna", color='b')

#plt.plot(Cx, Cy, label="Krzywa cykloidalna", color='r')
plt.xlabel('X [mm]')
plt.ylabel('Y [mm]')
plt.title('Wyznaczona krzywa epicykloidalna')
plt.grid(True)
plt.legend()
plt.axis('equal')

formula = f"X = {R} * cos(t) - {Rr} * cos(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) - ({E} * cos({N} * t))"
formula += f"\nY = -{R} * sin(t) + {Rr} * sin(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) + ({E} * sin({N} * t))"
print("Wzór z podstawionymi wartościami parametrów:")
print(formula)
# Wyświetlenie wykresu
plt.show()

print(Cx)
print(Cy)
print(PSI)