# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:28:06 2023

@author: 1mich
"""
R = 45. 
N = 51.
r = 1.5

import numpy as np
import matplotlib.pyplot as plt
m_min = (N - 2) / (2 * (N - 1))
print(f" m_min = {m_min}")
m = np.linspace(m_min, 1, 1000)

r_max = R * np.sin(np.pi / N)

e = r  * m / (N * np.sin(np.pi / N))

print(f" r_max = {r_max}")
# Wykres
plt.figure(figsize=(8, 8))
plt.plot(m,e , label="zakres e", color='b')
plt.yscale('y', "linear")

plt.grid(True)
plt.legend()
plt.axis('equal')
#mienne = f" m = {m} ; Xi = {Xi} ; Psi1 = {Psi1} ; mi_vo_1 = {mi_vo_1} ; V_epsilon = {V_epsilon} ; P_vk = {P_vk} ; Psi2 = {Psi2} ; Psi3 = {Psi3}"
 
#ormula = f"X = {R} * cos(t) - {Rr} * cos(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) - ({E} * cos({N} * t))"
#formula += f"\nY = -{R} * sin(t) + {Rr} * sin(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) + ({E} * sin({N} * t))"
#print("Wzór z podstawionymi wartościami parametrów:")
#print(formula)

print(" ")
#print(f" effi = {effi} warunek_1 = {warunek_1} warunek_2 = {warunek_2} warunek_3 = {warunek_3}")

# Wyświetlenie wykresu
plt.show()