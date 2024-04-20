# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:13:47 2023

@author: 1mich
"""

import numpy as np
import matplotlib.pyplot as plt

# Parametry krzywej cykloidalnej
R = 32

Rr = 1.5
E = .75
N = 36
m = (E * N)/R
ratio = 35
M_ob = 10 #moment obciazajacy przekladnie
Ro_izl = 22
 #promień okregu na ktorym sa otwory wyjsciowe
# Zakres zmiennej t od 0 do 360 stopni
t = np.linspace(0, 2 * np.pi, 100000)
n_in = 1000
n_out = n_in / ratio 
c = 1.5 #wsp bezpieczenstwa
R_os = 5. 
R_ps = R_os - (1 * E) #promien panewski sworznia
d_vk = 4
k = 0.005
d_kt = 3 #srednica waleczka lozyska walcowego
d_cz = 12  #srednica wew lozyska

# Wzory na współrzędne X i Y dow wyznaczenia krzywej cyklo
#Cx = (R * np.cos(t)) - (Rr * np.cos(t + np.arctan(np.sin((1 - N) * t) / ((R / (E * N)) - np.cos((1 - N) * t))))) - (E * np.cos(N * t))
#Cy = (-R * np.sin(t)) + (Rr * np.sin(t + np.arctan(np.sin((1 - N) * t) / ((R / (E * N)) - np.cos((1 - N) * t))))) + (E * np.sin(N * t))
#PSI = np.arctan(np.sin((1 - N) * t) / ((R / (E * N) *t) - np.cos((1 - N) * t)))

#sprawdzenie warunków cyklo, obiegowe przekladnei strona 18/113
warunek_1 = (Rr * m) / (N * np.sin(np.pi / N))

warunek_2 = Rr * (N + 1)/(3 * np.power(3,0.5) * N) * np.power(((N + 1)/(N - 1)),0.5) * np.power(((np.power(m,2))/(1 - np.power(m,2))),0.5) 
warunek_3 = (N - 2)/(2 * N - 1)
print(f" warunek_1 = {warunek_1} ")
print(f" warunek_2 = {warunek_2} ")
print(f" warunek_3 = {warunek_3} ")
# warunki zostały spełniony

Xi = 1 - m

if warunek_1 < E and warunek_2 < E and warunek_3 < m:
    print("wsyztskie warunki zostaly spelnione")
else:
    print("cos zjebales")

x_xi = np.array([0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.333, 0.366, 0.4, 0.433, 0.466, 0.5, 0.533 ])
y_k3 = np.array([0.5, 0.466, 0.412, 0.385, 0.355, 0.32, 0.3, 0.266, 0.245, 0.221, 0.209, 0.19, 0.17, 0.16, 0.145, 0.138])

# find the value of gold on day 3
intepolated_k3 = np.interp(Xi, x_xi, y_k3)
#obliczenia sprawnosci
XI2 =   [
    0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5
]

Ky = [
    0.55, 0.5, 0.42, 0.38, 0.36, 0.34, 0.325, 0.3, 0.28, 0.24, 0.2, 0.19, 0.18, 0.166, 0.145, 0.139, 0.133
]
inter_ky = np.interp(Xi,XI2 , Ky)
print("Ky", inter_ky)
print("K3", intepolated_k3)
#wspolczynniki tarcia
mi_z_0 = 0.1 #wsp tarcia statycznego stal-stal
mi_s_1 = 0.15 #wsp tarcia statcyznego stal-mosiądz
K3 = intepolated_k3 #wynika z wykrsu
Ky = inter_ky #wynika z wykresu


#pierqwszy człon strat według Kuryasteva

Psi1 = (K3 * mi_z_0)/N

#drugi czlon strat wedlug Kuryasteva

T3 = M_ob * c

mi_vo_1 = (d_vk / R_ps) * mi_s_1

omega_out = (np.pi * n_in) / 30 / ratio

V_epsilon = ((R_os * 0.5) + (R_ps * 0.5)) / 1000 * omega_out
    
mi_vo_2 = 0.08 #z wykresu

mi_VO = 0.08 #bierzemy mniejsza wartosc z tych wyliczonych mi_vo_2


P_vk = (4 * T3)/(np.pi * Ro_izl) * E * omega_out * mi_VO

Psi2 = 1 / omega_out * P_vk / T3


#trzeci czlon strat wedlug Kuryasteva

Tt1 = 1.3 * k / 1000 * (1  + (d_cz/d_kt)) * (1000 * T3 / R) 
Tt2 = np.power(((4 * np.pi / R / Ro_izl) - Ky),2)
Tt3 = np.power( 1 + Tt2, 0.5)

Tt = Tt1 * Tt3

Psi3  = 1.25 * Tt / T3
    

#wyznaczenie calkowitej sprawnosci

PSI = Psi1 + Psi2 + Psi3

effi = (1 - PSI) / (1 + (ratio * PSI)) 


# Wykres
plt.figure(figsize=(8, 8))
#plt.plot(Cx, Cy, label="Krzywa cykloidalna", color='b')
plt.plot(t,t)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('whomstever i need at the moment')
plt.grid(True)
plt.legend()
plt.axis('equal')
zmienne = f" m = {m} ; Xi = {Xi} ; Psi1 = {Psi1} ; Psi2 = {Psi2} ; Tt = {Tt} ; P_vk = {P_vk} ; Psi2 = {Psi2} ; Psi3 = {Psi3}"

#formula = f"X = {R} * cos(t) - {Rr} * cos(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) - ({E} * cos({N} * t))"
#formula += f"\nY = -{R} * sin(t) + {Rr} * sin(t + atan(sin((1 - {N}) * t) / ({R} / ({E} * {N}) - cos((1 - {N}) * t)))) + ({E} * sin({N} * t))"
#print("Wzór z podstawionymi wartościami parametrów:")
#print(formula)
print(zmienne)
print(" ")
print(f" effi = {effi} warunek_1 = {warunek_1} warunek_2 = {warunek_2} warunek_3 = {warunek_3}")
print(" ")
print(f" PSI = {PSI} ")
# Wyświetlenie wykresu
plt.show()