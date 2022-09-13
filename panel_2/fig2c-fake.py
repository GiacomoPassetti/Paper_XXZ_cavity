import matplotlib.pyplot as plt
import numpy as np
import os
import json
from matplotlib import gridspec
#sns.set_theme()

Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
U_log = np.logspace(np.log10(4), 2, 20)
Us = np.append(Us, U_log)
L = 110
Nmax = 25
chi = 1000
Omega = 1
g0 = 0.1

def Entropy_perturbation_theory(g, U, omega):
    return -(g**2/((U+omega)**2))*(np.log(g**2/((U+omega)**2))-1)
X = np.linspace(0, 100, 300)
Y = Entropy_perturbation_theory(g0, X, Omega)
final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))






fontsize = 10


nrow = 1
ncol = 1
fig = plt.figure(figsize=(3.75, 2.5), dpi = 800) 

gs = gridspec.GridSpec(nrow, ncol, 
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.21, left=0.15, right=0.95) 


# LEFT PANEL    
ax1= plt.subplot(gs[0,0])


#plt.title("L = "+str(L)+r"$g = $"+str(g0)+r"$\omega = $"+str(Omega))


#ax1.set_xlabel(r"$U$", loc = "right")
ax1.set_xlabel(r"$U$")
#ax.set_ylabel(r"$\frac{<J^{4}>}{L^{2}}-\frac{<J^{2}>^{2}}{L^{2}}$")

#ax2 = ax.twinx()
for Omega in [1, 2, 4, 8, 12]:
    g0 = 0.1*Omega
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
    ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))
    delta_J_sq = np.load(os.path.join("../XXZ/current_operator", "current_fluctuations_jointed"+final_ID+".npy"))
    ax1.plot(Us, ent/delta_J_sq, label = r"$\Omega = $"+str(Omega), ls = "",marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6)

#ax2.set_ylabel(r"$N_{ph} \frac{g^2}{\omega}$")
#ax2.plot(Us, entanglement2)
#ax2.plot(Us, entanglement3)
#ax1.plot(X, Y, label = r"$PT$",ls = "--", color = "grey")
ax1.set_ylabel(r"$S_{e-ph}/\delta J^{2}$")
ax1.set_xlim(0, 4)
ax1.legend()

#ax2.plot(X, Y,ls = "--", color = "grey")
plt.savefig(os.path.join("plots", "quotient_L_"+str(L)+"g_"+str(g0)+"Omega"+str(Omega)+".png"))