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
L = 110
Nmax = 16
chi = 1000
Omega = 1
g0 = 0.3

nphs = []
correlation = []
entanglement = []
current_fluctuations = []
J_sqd = []
J_fourth = []
A_sqd = []
K = []
for U in Us:
    ID = "Renormalized_U_L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"U_"+"{:.2f}".format(U)+"_original_g_"+"{:.4f}".format(g0)+"omega_"+"{:.4f}".format(Omega)
    try:
        #nphs.append(np.array(np.load(os.path.join("XXZ", "photon_occupation", "photon_occupation" + ID + ".npy"))[0]))
        correlation.append(np.array(
            np.load(os.path.join("XXZ", "correlation_functions", "correlation_functions" + ID + ".npy")).reshape(1)[0]))
        #entanglement.append(
            #np.array(np.load(os.path.join("XXZ", "entanglement_entropy", "entanglement_entropy" + ID + ".npy"))[0]))
        #current_fluctuations.append(
        #    np.array(np.load(os.path.join("XXZ", "current_operator", "current_fluctuations" + ID + ".npy"))))
        #J_sqd.append(np.array(np.load(os.path.join("XXZ", "current_operator", "J_sqd" + ID + ".npy"))))
        #J_fourth.append(np.array(np.load(os.path.join("XXZ", "current_operator", "J_fourth" + ID + ".npy"))))
        #A_sqd.append(np.array(np.load(os.path.join("XXZ", "photon_occupation", "a_squared" + ID + ".npy"))[0]))
        # K.append(np.array(np.load(os.path.join("kinetic_operator", "re_kr"+ID+".npy"))))
    except:
        print("fail at U = ", U)
        #nphs.append(np.array(0))
        correlation.append(np.array(0))
        #entanglement.append(np.array(0))
        #current_fluctuations.append(np.array(0))
        #J_sqd.append(np.array(0))
        #J_fourth.append(np.array(0))
        #A_sqd.append(np.array(0))
        # K.append(0)
    # print("corr", correlation)
    # print("nphs", nphs)
    # print("entanglement", entanglement)
    final_ID = "renormalized_U_jointed_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(g0) + "omega_" + "{:.3f}".format(
        Omega)
    np.save(os.path.join("XXZ", "photon_occupation", "photon_occupation_jointed" + final_ID + ".npy"), nphs)
    np.save(os.path.join("XXZ", "photon_occupation", "A_sqd_jointed" + final_ID + ".npy"), A_sqd)
    np.save(os.path.join("XXZ", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"), correlation)
    # print(correlation)
    np.save(os.path.join("XXZ", "entanglement_entropy", "entanglement_jointed" + final_ID + ".npy"), entanglement)
    np.save(os.path.join("XXZ", "current_operator", "current_fluctuations_jointed" + final_ID + ".npy"), current_fluctuations)
    np.save(os.path.join("XXZ", "current_operator", "J_sqd_jointed" + final_ID + ".npy"), J_sqd)
    np.save(os.path.join("XXZ", "current_operator", "J_fourth_jointed" + final_ID + ".npy"), J_fourth)
    np.save(os.path.join("XXZ", "kinetic_operator", "re_k_Jointed" + final_ID + ".npy"), K)