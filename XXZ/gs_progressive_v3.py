import tenpy
import numpy as np
from tenpy.linalg.np_conserved import Array
from tenpy.networks.site import BosonSite, FermionSite
from scipy.linalg import expm
import copy
import sys
import numpy as np
import numpy.linalg as alg
from tenpy import models
from tenpy.models.lattice import Chain, Lattice, IrregularLattice 
import os
from tenpy.networks.mps import MPS
from tenpy.tools.params import get_parameter
from tenpy.linalg.charges import LegCharge, ChargeInfo
from tenpy.algorithms.truncation import truncate, svd_theta, TruncationError
import tenpy.linalg.np_conserved as npc
from scipy.linalg import expm
import pickle
import time
from tenpy.networks.mpo import MPO
from tenpy.algorithms.dmrg import TwoSiteDMRGEngine
from tenpy.models.model import MPOModel
from tenpy.algorithms import dmrg
from tenpy.models.model import CouplingModel
import pickle



L = int(sys.argv[1])
J = -1

Nmax = 10
g0 = float(sys.argv[2])
#g = g0/np.sqrt(L)

U = float(sys.argv[3])
Omega = float(sys.argv[4])
#g0 = np.sqrt(Omega)
g = g0/np.sqrt(L)


options = {'compression_method' : 'SVD'}

def Leg_b(Nmax):
 qflat=[[0]]*(Nmax+1)
 ch=ChargeInfo([1], names=None)
 leg = LegCharge.from_qflat(ch, qflat, qconj=1)
 return leg

def sites(L,Nmax, g):  #Define the sites of the MPS
 FSite=FermionSite('N', filling=0.5)

 BSite=BosonSite(Nmax=Nmax,conserve=None, filling=0 )
 BSite.change_charge(Leg_b(Nmax))
 KR = npc.expm(1j*g*(BSite.B+BSite.Bd))
 KL = npc.expm(-1j*g*(BSite.B+BSite.Bd))
 DY = 0.5*(KR + KL)
 BSite.add_op("KR", KR)
 BSite.add_op("KL", KL)
 BSite.add_op("DY", DY)
 
 sites=[]
 sites.append(BSite)
 for i in range(L):
     sites.append(FSite)
 return sites

def product_state(L):# Creates a list where you define every single state of the chain, in this empty full staggered
    ps=['vac']
    for i in range(int(L/2)):
        ps.append('empty')
        ps.append('full')
    return ps

def ansatz_wf(Nmax, L):
    ps= product_state(L)
    site= sites(L,Nmax, g)
    psi=MPS.from_product_state(site, ps)
    return psi

def MPO_current():
   siti = sites(L, Nmax, g)
   reg_lat = Lattice([L], unit_cell=[siti[1]])
   irr_lat = IrregularLattice(reg_lat, add=([[(L - 1)//2, 1]], [-1]), add_unit_cell=[siti[0]])

   MyMod = CouplingModel(irr_lat)
   for i in range(L-1):
        MyMod.add_multi_coupling_term(strength = 1j, ijkl = [1+i,i+2], ops_ijkl = ['Cd', 'C'], op_string = [ 'JW'], plus_hc=False)
        MyMod.add_multi_coupling_term(strength = -1j, ijkl = [1+i,i+2], ops_ijkl = ['C', 'Cd'], op_string = ['JW'], plus_hc=False)
   MyMod.add_multi_coupling_term(strength = -1j, ijkl = [1,L], ops_ijkl = ['Cd', 'C'], op_string = [ 'JW'], plus_hc=False)
   MyMod.add_multi_coupling_term(strength = 1j, ijkl = [1,L], ops_ijkl = ['C', 'Cd'], op_string = ['JW'], plus_hc=False)
   mpo = MyMod.calc_H_MPO()
   return mpo



def calc_MPO(J, Omega, Nmax, g, U, PBC):
    siti = sites(L, Nmax, g)
    reg_lat = Lattice([L], unit_cell=[siti[1]])
    irr_lat = IrregularLattice(reg_lat, add=([[(L - 1)//2, 1]], [-1]), add_unit_cell=[siti[0]])

    MyMod = CouplingModel(irr_lat)
    for i in range(L-1):
        MyMod.add_multi_coupling_term(strength = J, ijkl = [0,i+1,i+2], ops_ijkl = ['KR', 'Cd', 'C'], op_string = ['Id', 'Id'], plus_hc=False)
        MyMod.add_multi_coupling_term(strength = J, ijkl = [0,i+1,i+2], ops_ijkl = ['KL', 'C', 'Cd'], op_string = ['Id', 'Id'], plus_hc=False)
        MyMod.add_coupling_term(strength = U, i = i+1,j = i+2, op_i ='dN', op_j ='dN', op_string = 'Id', plus_hc=False)
    MyMod.add_onsite_term(strength = Omega, i = 0, op = 'N')
    if PBC == 1:
         MyMod.add_multi_coupling_term(strength = J, ijkl = [0,1,L], ops_ijkl = ['KL', 'Cd', 'C'], op_string = ['Id', 'JW'], plus_hc=False)
         MyMod.add_multi_coupling_term(strength = J, ijkl = [0,1,L], ops_ijkl = ['KR', 'C', 'Cd'], op_string = ['Id', 'JW'], plus_hc=False)
         MyMod.add_coupling_term(strength = U, i = 1,j = L, op_i ='dN', op_j ='dN', op_string = 'Id', plus_hc=False)         
    mpo = MyMod.calc_H_MPO()
    
    M = MPOModel(irr_lat, mpo)
    print(mpo.is_hermitian())
    return mpo, M, irr_lat







def proj(n, leg):
    prj = np.zeros((Nmax+1,Nmax+1))
    prj[n,n] = 1
    prj = npc.Array.from_ndarray(prj,leg, labels=['p', 'p*'])
    return prj



chis = [1000, 1200]
psi = ansatz_wf(Nmax, L)
for chi in chis:
     print("at chi: ", chi)
     ID = "Fast_L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"U_"+"{:.2f}".format(U)+"g_"+"{:.4f}".format(g0)+"omega_"+"{:.4f}".format(Omega)
     dmrg_params = {
             'trunc_params': {
                 'chi_max': chi,
                 'svd_min': 1.e-10,
                 'trunc_cut': 1.e-10,
                 'update_env': 20,
                 'start_env': 20,
                  'max_E_err': 0.000001,
                  'max_S_err': 0.000001,
                  'verbose': 1,
                  'mixer': True
             },
             'update_env': 20,
             'start_env': 20,
             'max_E_err': 0.000001,
             'max_S_err': 0.000001,
             'verbose': 1,
             'mixer': True
         }
     

     siti = sites(L, Nmax, g)
     t0 = time.time()
     H, M, Mylat = calc_MPO(J, Omega, Nmax, g, U, PBC = 1)
     engine = dmrg.TwoSiteDMRGEngine(psi, M, dmrg_params)
     engine.run()
     stats = engine.sweep_stats
     #with open(os.path.join("GS", ID+'.pkl'), 'wb') as f:
            #pickle.dump(psi, f)
     pns = []
     leg = [psi.sites[0].N.get_leg('p'), psi.sites[0].N.get_leg('p*')]
     for n in range(Nmax+1):
          pns.append(psi.expectation_value(proj(n, leg), 0))

     #if(chi==2000 or chi==1000):
     with open("/ptmp/ceckhardt/GS" + ID + '.pkl', 'wb') as f:
          pickle.dump(psi, f)
     f.close()

     np.save(os.path.join("Phot_Projection" ,"Phot_projection_"+ID), pns)

     a_file = open(os.path.join("stats" ,"stats_"+ID+".npy"), "wb")
     pickle.dump(stats, a_file)
     a_file.close()

     np.save(os.path.join("photon_occupation", "photon_occupation"+ID) ,psi.expectation_value("N", 0))
     np.save(os.path.join("entanglement_entropy", "entanglement_entropy"+ID) ,psi.entanglement_entropy())
     rho = psi.get_rho_segment([0]).to_ndarray().reshape((Nmax+1), (Nmax+1))
     np.save(os.path.join("rho", "rho"+ID), rho)
     np.save(os.path.join("correlation_functions", "correlation_functions"+ID) ,psi.correlation_function('dN','dN', sites1=[1], sites2=[int(L/2)]))
     np.save(os.path.join("correlation_functions", "dN_site_1"+ID) ,psi.expectation_value("dN", 1))
     np.save(os.path.join("correlation_functions", "dN_site_L_half"+ID) ,psi.expectation_value("dN", int(L/2)))
     np.save(os.path.join("time_chrono", "time_"+ID), time.time()-t0)

     # New stuff  

     # Current Fluctuations
     psi0 = copy.deepcopy(psi)    
     J_mpo = MPO_current()
     J_mpo.apply(psi, options)
     J_mpo.apply(psi, options)
     J_sqd = psi0.overlap(psi)
     np.save(os.path.join("current_operator", "J_sqd"+ID), J_sqd)
     J_mpo.apply(psi, options)
     J_mpo.apply(psi, options)
     J_fourth = psi0.overlap(psi)
     np.save(os.path.join("current_operator", "J_fourth"+ID), J_fourth)
     psi = psi0
     fluctuation_J_fourth = (J_fourth/(L**2)) - (J_sqd**2/(L**2))
     np.save(os.path.join("current_operator", "current_fluctuations"+ID), fluctuation_J_fourth)
     print(fluctuation_J_fourth)



     
     
