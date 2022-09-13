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


def xxz(L, chi, Jxx, Jz, gamma):
   model_params = dict(L=L, Jxx = gamma*Jxx, Jz=Jz,h = 0,  bc_MPS='finite', conserve='Sz', verbose=0)
   dmrg_params = {
        'trunc_params': {
            'chi_max': chi,
            'svd_min': 1.e-10,
            'trunc_cut': 1.e-10,
            'update_env': 20,
            'start_env': 20,
             'max_E_err': 0.0001,
             'max_S_err': 0.0001,
             'verbose': 1,
             'mixer': True
        },
        'update_env': 20,
        'start_env': 20,
        'max_E_err': 0.0001,
        'max_S_err': 0.0001,
        'verbose': 1,
        'mixer': True
    }


   M = XXZChain(model_params)
   psi = MPS.from_product_state(M.lat.mps_sites(), (["up", "down"] * L)[:L], M.lat.bc_MPS)
   KR = npc.outer(psi.sites[0].Sp.replace_labels(['p', 'p*'], ['p0', 'p0*']),psi.sites[1].Sm.replace_labels(['p', 'p*'], ['p1', 'p1*'])).itranspose([0,2,1,3])
   engine = dmrg.TwoSiteDMRGEngine(psi, M, dmrg_params)
   E = engine.run()[0]
   k = abs(sum(psi.expectation_value(KR)))
   return k


def XXZ_PERIODIC(L, chi, U, gamma, imp):
    
    dmrg_params = {
        'trunc_params': {
            'chi_max': chi,
            'svd_min': 1.e-10,
            'trunc_cut': 1.e-10,
            'update_env': 20,
            'start_env': 20,
             'max_E_err': 0.0001,
             'max_S_err': 0.0001,
             'verbose': 1,
             'mixer': True
        },
        'update_env': 20,
        'start_env': 20,
        'max_E_err': 0.0001,
        'max_S_err': 0.0001,
        'verbose': 1,
        'mixer': True
    }
    options = {'compression_method' : 'SVD'}
    def sites(L):  #Define the sites of the MPS
      FSite=FermionSite('N', filling=0.5)
      sites=[]
      for i in range(L):
        sites.append(FSite)
      return sites

    def product_state(L):# Creates a list where you define every single state of the chain, in this empty full staggered
       ps = []
       for i in range(int(L/2)):
          ps.append('empty')
          ps.append('full')
       return ps
    def trial_state(L):# Creates a list where you define every single state of the chain, in this empty full staggered
       ps = ['empty']*(L)
       
          
       ps[L-1] = 'full'
       
       return ps

    def ansatz_wf( L): #Builds the MPS (The MPS class is very rich of functions that i use everywhere)
       ps= product_state(L)
       site= sites(L)
       psi=MPS.from_product_state(site, ps)
       return psi
    def try_wf( L): #Builds the MPS (The MPS class is very rich of functions that i use everywhere)
       ps= trial_state(L)
       site= sites(L)
       psi=MPS.from_product_state(site, ps)
       return psi

    def calc_MPO(gamma, U):
      siti = sites(L)
      reg_lat = Lattice([L], unit_cell=[siti[1]])
      psi = ansatz_wf(L)
      MyMod = CouplingModel(reg_lat)
      for i in range(L-1):
        MyMod.add_multi_coupling_term(strength = -gamma, ijkl = [i,i+1], ops_ijkl = ['Cd', 'C'], op_string = [ 'Id'], plus_hc=False)
        MyMod.add_multi_coupling_term(strength = -np.conj(gamma), ijkl = [i,i+1], ops_ijkl = ['C', 'Cd'], op_string = ['Id'], plus_hc=False)
        MyMod.add_coupling_term(strength = U, i = i,j = i+1, op_i ='dN', op_j ='dN', op_string = 'Id', plus_hc=False)
      MyMod.add_onsite_term(strength = imp, i = int(L/2), op = 'N')
      MyMod.add_multi_coupling_term(strength = -np.conj(gamma), ijkl = [0,L-1], ops_ijkl = ['Cd', 'C'], op_string = [ 'JW'], plus_hc=False)
      MyMod.add_multi_coupling_term(strength = -gamma, ijkl = [0,L-1], ops_ijkl = ['C', 'Cd'], op_string = ['JW'], plus_hc=False)
      MyMod.add_coupling_term(strength = U, i = 0,j = L-1, op_i ='dN', op_j ='dN', op_string = 'Id', plus_hc=False)         
      mpo = MyMod.calc_H_MPO()
      
      M = MPOModel(reg_lat, mpo)
      return mpo, M, reg_lat
    siti = sites(L)
    psi = ansatz_wf(L)


    H, M, Mylat = calc_MPO(gamma , U)
    engine = dmrg.TwoSiteDMRGEngine(psi, M, dmrg_params)
    
    E = engine.run()[0]
    KR = 0
    
    for i in range(L-1):
      KR += psi.correlation_function('Cd','C', [i], [i+1], autoJW=True)[0][0]
      #KL += psi.correlation_function('Cd','C', [i+1], [i], autoJW=True)[0][0]
    KR += psi.correlation_function('Cd','C', [L-1], [0], autoJW=True)[0][0]
    #KL += psi.correlation_function('Cd','C', [0], [L-1], autoJW=True)[0][0]
    CORR = psi.correlation_function('dN','dN', sites1=[0], sites2=[int(L/2)-1])
    return E, abs(KR), np.angle(KR), CORR

def Boson(k, phi, omega, g, t, Nmax):
    
    B, Bd, Nb, Idb = BosonSite(Nmax=Nmax,conserve=None, filling=0 ).B.to_ndarray(), BosonSite(Nmax=Nmax,conserve=None, filling=0 ).Bd.to_ndarray(), BosonSite(Nmax=Nmax,conserve=None, filling=0 ).N.to_ndarray(), BosonSite(Nmax=Nmax,conserve=None, filling=0 ).Id.to_ndarray()
    X= B+Bd
    Y= 1j*(Bd-B)
    BB = B.dot(B)
    BdBd= Bd.dot(Bd)
    H = omega*Nb - 2*(t)*k*(cosm((g*X) + (phi*Idb))).dot(Idb)
    w, v = eigsh(H, k = 1, which = 'SA')
    E = w[0]
    v = v[:, 0]
    exp = v.conj().T.dot(expm(1j*g*X).dot(v))
    n_phot = v.conj().T.dot(Nb.dot(v))
    gamma, Phi = abs(exp), np.angle(exp)
    return E, gamma, Phi, exp, n_phot




def Iterator_MF(g, U, L, its, chi, imp):
 gamma = 1   
 Efer, K, kai, CORR = XXZ_PERIODIC(L, chi, U, gamma, imp)   
 for i in range(its):
     print("Initiate gamma :", 1)
     Efer, K, kai, CORR = XXZ_PERIODIC(L, chi, U, gamma, imp)
     print(Efer, K, kai)
     Ebos, GA, PHI, gamma, nph = Boson(K, kai, 1, g/np.sqrt(L), 1, 30)
     print("After sweep", i, "Gamma is :", gamma)
 Etot = Efer + Ebos + (2 * K *gamma *np.cos(kai + np.angle(gamma)))
 return Etot,  GA, PHI, K, kai, nph, CORR

g = float(sys.argv[1])
L = int(sys.argv[2])
imp = float(sys.argv[3])
Us1 = [0.0, 0.25, 0.5,0.75, 1, 1.25]
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
GAS = []
PHIS =[]
KS = []
kais = []
nphs = []
CORRS = []
for U in Us:
   Etot,  GA, PHI, K, kai, nph, CORR = Iterator_MF(g, U, L, 6, 500, imp)
   GAS.append(GA)
   PHIS.append(PHI)
   KS.append(K)
   kais.append(kai)
   nphs.append(nph)
   CORRS.append(CORR)


ID = "_L"+"{:.2f}".format(L)+"{:.2f}".format(g)+"imp_"+"{:.2f}".format(imp)
np.save("GAS_"+ID+".npy", GAS)
np.save("PHIS_"+ID+".npy", PHIS)
np.save("KS_"+ID+".npy", KS)
np.save("kais_"+ID+".npy", kais)
np.save("nphs_"+ID+".npy", nphs)
np.save("CORRS_"+ID+".npy", CORRS)
print(CORRS)
    



