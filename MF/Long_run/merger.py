# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:04:12 2021

@author: giaco
"""

import numpy as np
import tenpy
import tenpy.linalg.np_conserved as npc
from tenpy.models.xxz_chain import XXZChain
from tenpy.networks.mps import MPS
from tenpy.algorithms import dmrg
import sys
from tenpy.networks.site import BosonSite, FermionSite
from scipy.linalg import expm, sinm, cosm, eigh
from scipy.sparse.linalg import eigsh
from scipy.linalg import eigh
from tenpy.models.model import MPOModel
from tenpy.models.lattice import Chain, Lattice, IrregularLattice 
from tenpy.models.model import CouplingModel


 


Us = np.logspace(0.7, 2, 10)
g = float(sys.argv[1])
L = int(sys.argv[2])
GAS = []
PHIS = []
KS = []
kais = []
nphs = []
ETOT = []
for U in Us:
  ID = "log_datas_L"+"{:.2f}".format(L)+"g_"+"{:.2f}".format(g)+"U_"+"{:.2f}".format(U)

  nphs.append(np.load(ID + ".npy"))
nphs = np.array(nphs)
np.save("mf_log.npy", nphs)
    



