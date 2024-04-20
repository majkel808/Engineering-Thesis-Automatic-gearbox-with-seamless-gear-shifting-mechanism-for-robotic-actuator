# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 00:13:47 2023

@author: 1mich
"""

import numpy as np

import matplotlib.pyplot as plt

# Parametry krzywej cykloidalnej
R = 45.
Rr = 1.5
E = np.linspace(.45, .85, 10000)

N = 51
m = (E * N) / R
ratio = 50.
M_ob = 45 #moment obciazajacy przekladnie
Ro_izl = 30 #promień okregu na ktorym sa otwory wyjsciowe
# Zakres zmiennej t od 0 do 360 stopni
t = np.linspace(0, 2 * np.pi, 10000)
n_in = 1000.
n_out = 20. 
c = 1.5 #wsp bezpieczenstwa
R_os = 6
R_ps = R_os - (1 * E) #promien panewski sworznia
d_vk = 8
k = 0.005
d_kt = 5 #srednica waleczka lozyska walcowego
d_cz = 15.   #srednica wew lozyska

E_max = E[0]
print(f" E_max = {E_max} ")
for i in range(len(E)):
    temp = E[i]
    if(temp > E_max):
        E_max = temp
        ind = i
 
print(f" E_max = {E_max}, ind = {ind} ")

# warunki zostały spełniony

print('m =', m)

Xi = 1. - m
print(Xi)

#interpolacja grafu K3 od XI

x_xi = np.array([0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5
])
y_k3 = np.array([1.16, 1.18, 1.2, 1.25, 1.33, 1.4, 1.51, 1.62, 1.68, 1.75, 1.83, 1.92, 2.02, 2.15])

# find the value of gold on day 3
intepolated_k3 = np.interp(Xi, x_xi, y_k3)

#print("intepolated k3", intepolated_k3)


#intepolated KY

XI2 = np.array([
    0.1, 0.125, 0.15, 0.175, 0.2, 0.225, 0.25, 0.275, 0.3, 0.325, 0.35, 0.375, 0.4, 0.425, 0.45, 0.475, 0.5
])   

Ky = np.array([
    0.55, 0.5, 0.42, 0.38, 0.36, 0.34, 0.325, 0.3, 0.28, 0.24, 0.2, 0.19, 0.18, 0.166, 0.145, 0.139, 0.133
])
inter_ky = np.interp(Xi, XI2, Ky)
#print("Ky", inter_ky)

#obliczenia sprawnosci

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


P_vk = (4. * T3)/(np.pi * Ro_izl) * E * omega_out * mi_VO

Psi2 = 1. / omega_out * P_vk / T3


#trzeci czlon strat wedlug Kuryasteva

Tt1 = 1.3 * k / 1000. * (1  + (d_cz/d_kt)) * (1000. * T3 / R) 
Tt2 = np.power(((4 * np.pi / R / Ro_izl) - Ky),2)
Tt3 = np.power( 1. + Tt2, 0.5)

Tt = Tt1 * Tt3

Psi3  = 1.25 * Tt / T3


#wyznaczenie calkowitej sprawnosci

PSI = Psi1 + Psi2 + Psi3
xx = 1. * R

effi = (1 - PSI) / (1 + (ratio * PSI))

#print(effi)
effi_max = 0
_index  = 0
print(f" effi_max = {effi_max} ")
for index, i in enumerate(range(0 ,len(effi))):
    temp = effi[i]
    if(temp > effi_max):
        effi_max = temp

        _index = index

print(f" effi_max = {effi_max}, ind = {_index} ,  E_max[_index] = {E[_index]}")







# Wykres
plt.figure(figsize=(10, 10))

# Zmiana na wykres o osi Y ograniczonej od 0 do 1
plt.plot(E, effi, label="n(E)", color='b')
plt.xlim(0.44, .89)
plt.ylim(.75, .78)
plt.yscale(1, 'linear')
plt.xlabel('Mimośród [mm]')
plt.ylabel('Sprawność przekładni')
plt.title('Wykres spranowości od paramteru mimośrodu')
plt.grid(True)
plt.legend()
plt.axis('equal')
zmienne = f"m = {m};"

#print(zmienne)
print(" ")
#print(f"effi = {effi}")

plt.show()