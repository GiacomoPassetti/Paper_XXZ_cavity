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
Us = np.arange(0, 4.2, 0.2)
L = 210
Nmax = 16
chi = 1000
Omega = 1
g0 = 0.0

nphs = []
correlation = []
entanglement = []
current_fluctuations = []
J_sqd = []
J_fourth = []
A_sqd = []
K = []
for U in Us:
    ID = "Fast_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "U_" + "{:.2f}".format(U) + "g_" + "{:.4f}".format(
        g0) + "omega_" + "{:.4f}".format(Omega)
    try:
        
        
        correlation.append(np.array(
            np.load(os.path.join("XXZ", "correlation_functions", "correlation_functions" + ID + ".npy")).reshape(1)[0]))

    except:

        correlation.append(np.array(0))

        # K.append(0)
    # print("corr", correlation)
    # print("nphs", nphs)
    # print("entanglement", entanglement)
    final_ID = "new_U_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(
        g0) + "omega_" + "{:.3f}".format(Omega)

    np.save(os.path.join("XXZ", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"), correlation)
    # print(correlation)
