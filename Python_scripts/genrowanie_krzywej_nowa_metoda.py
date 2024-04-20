# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 18:02:53 2023

@author: 1mich
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametry krzywej cykloidalnej
R = 40
Rr = 1.5
E = 0.7
N = 51
n = N - 1
iH = N- 1

# Zakres zmiennej t od 0 do 360 stopni
t = np.linspace(0, 2 * np.pi, 7000)
Z = np.power(t,2)
# Wzory na współrzędne X i Y
K = (E * N)/R #to jest m
print(K)
S = 1 + np.power(K,2) - (2 * K * np.cos(t))
Spow = np.power(S, -0.5)
#obliczanie  coordinates of X axis
X1 = (R - Rr * Spow) * np.cos((1-iH) * t)
X2 = (E - K * Rr * Spow) * np.cos((1-iH) * t)
X = X1 - X2

Y1 = (R - Rr * Spow) *  np.sin((1-iH) * t)
Y2 = (E - K * Rr * Spow) * np.sin((1-iH) * t)
Y = Y1 + Y2




# Wykres
plt.figure(figsize=(8, 8))
plt.plot(X, Y, label="Krzywa cykloidalna", color='b')
#plt.plot(t, Spow)
#plt.plot(t, Spow)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Krzywa cykloidalna')
plt.grid(True)
plt.legend()
plt.axis('equal')


# Wyświetlenie wykresu
plt.show()