import numpy as np

from scipy.linalg import expm
import copy
import sys
import numpy as np
import numpy.linalg as alg

import math

from scipy.linalg import expm
import pickle
import numpy.polynomial.hermite as Herm
import time

import pickle
from scipy.integrate import quad
import os

Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
Us = np.append(Us, np.logspace(np.log10(4), 2, 20))
Us_log = [5 , 6.99, 9.75, 13.59, 18.96, 26.44, 36.87, 51.42, 71.71, 100]
#omegas = [ 0.01,0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 100]
omegas = [0.0100, 0.0162, 0.0264, 0.0428, 0.0695, 0.1129, 0.1833, 0.2976, 0.4833, 0.7848, 1.2743, 2.0691, 3.3598, 5.4556, 8.8587, 14.3845, 23.3572, 37.9269, 61.5848, 100.0000]
L = 110
Nmax = 16
chi = 600
Omega = 1
g0 = 0.3
g = g0/np.sqrt(L)

nphs = []
correlation = []
entanglement = []
A_sqd = []
for U in Us:
        




        
            ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"U_"+"{:.2f}".format(U)+"g_"+"{:.4f}".format(g0)+"omega_"+"{:.4f}".format(Omega)
            nphs.append(np.load(os.path.join("photon_occupation", "mean_field_photon_occupation"+ID+".npy")))
            correlation.append(np.load(os.path.join("correlations", "mean_field_correlation"+ID+".npy")))
            A_sqd.append(np.load(os.path.join("photon_occupation", "mean_field_A_sqd"+ID+".npy")))

            
final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)
np.save(os.path.join("photon_occupation", "mean_field_photon_occupation_jointed"+final_ID+".npy"), nphs)
np.save(os.path.join("correlations", "mean_field_correlation_functions_jointed"+final_ID+".npy"), correlation)
np.save(os.path.join("photon_occupation", "mean_field_A_sqd_jointed"+final_ID+".npy"), A_sqd)









