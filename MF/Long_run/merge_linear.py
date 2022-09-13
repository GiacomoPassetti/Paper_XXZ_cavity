# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:04:12 2021

@author: giaco
"""

import numpy as np
import sys


 
Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)


g = float(sys.argv[1])
L = int(sys.argv[2])
GAS = []
PHIS = []
KS = []
kais = []
nphs = []
ETOT = []
for U in Us:
  ID = "nphs__L"+"{:.2f}".format(L)+"{:.2f}".format(g)+"{:.2f}".format(U)

  nphs.append(np.load(ID + ".npy"))
nphs = np.array(nphs)
final_ID = "nphs__L"+"{:.2f}".format(L)+"{:.2f}".format(g)
np.save("mf_linear.npy"+final_ID, nphs)
    



