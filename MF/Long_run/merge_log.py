# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:04:12 2021

@author: giaco
"""

import numpy as np
import sys


Us = np.logspace(0.7, 2, 10)



g = float(sys.argv[1])
L = int(sys.argv[2])
GAS = []
PHIS = []
KS = []
kais = []
nphs = []
ETOT = []
for U in list(Us):
  ID = "nphs_log_datas_L"+"{:.2f}".format(L)+"g_"+"{:.2f}".format(g)+"U_"+"{:.2f}".format(U)

  nphs.append(np.load(ID + ".npy"))
nphs = np.array(nphs)
final_ID = "nphs_log_datas_L"+"{:.2f}".format(L)+"g_"+"{:.2f}".format(g)
np.save("mf_log.npy"+final_ID, nphs)
    



