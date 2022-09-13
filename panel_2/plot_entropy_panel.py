import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os
import json
from matplotlib import gridspec
#sns.set_theme()

Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
U_log = [  4. ,          4.73844431 ,   6.64947505 ,  7.87704182,
   9.331231,    11.05387963,  13.09454827,  15.51194695,  18.37562421,
  21.76796801,  25.78657607,  30.5470637 ,  36.18639008 , 42.86679858,
  50.78048451 , 60.15512453 , 71.26042696 , 84.41589125, 100]
Us = np.append(Us, U_log)
L = 50
Nmax = 25
chi = 1000
Omega = 1
g0 = 0.1

def Entropy_perturbation_theory(g, U, omega):
    return -(g**2/((U+omega)**2))*(np.log(g**2/((U+omega)**2))-1)
X = np.linspace(0, 100, 300)
Y = Entropy_perturbation_theory(g0, X, Omega)
final_ID = "full_U_L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
J_sqd = np.load(os.path.join("data", "J_sqd_jointed"+final_ID+".npy"))
entropy = np.load(os.path.join("data", "entanglement_entropy_jointed"+final_ID+".npy"))
J_sqd = (J_sqd*(g0**2))/(L*Omega)



fontsize = 10


nrow = 1
ncol = 2
fig = plt.figure(figsize=(3.75, 2.5), dpi = 800) 

gs = gridspec.GridSpec(nrow, ncol, width_ratios=[1, 1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.21, left=0.15, right=0.95) 


# LEFT PANEL    
ax1= plt.subplot(gs[0,0])
ax2 =  plt.subplot(gs[0,1])

#plt.title("L = "+str(L)+r"$g = $"+str(g0)+r"$\omega = $"+str(Omega))

ax1.plot(Us, J_sqd, label = r"$ J^{2}\,\frac{g^{2}}{\omega}$", color = "darkseagreen", marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6)
ax1.set_xlabel(r"$U$", loc = "right")
#ax.set_ylabel(r"$\frac{<J^{4}>}{L^{2}}-\frac{<J^{2}>^{2}}{L^{2}}$")

#ax2 = ax.twinx()
ax1.plot(Us, entropy, label = r"$S_{e-ph}$", color = "cornflowerblue", marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6)
#ax2.set_ylabel(r"$N_{ph} \frac{g^2}{\omega}$")
#ax2.plot(Us, entanglement2)
#ax2.plot(Us, entanglement3)
ax1.plot(X, Y, label = r"$PT$",ls = "--", color = "grey")
ax1.set_ylabel(r"$S_{e-ph}$")
ax1.set_xlim(0, 4)
ax1.legend()
ax2.plot(Us, entropy, color = "cornflowerblue", marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6)
ax2.set_xlim(4, 100)
ax2.set_xscale("log")
ax2.set_yticks([])
ax2.set_ylim(0, 0.006)
ax1.set_ylim(0, 0.006)
ax2.plot(Us, J_sqd, label = r"$\delta J^{2}\,\frac{g^{2}}{\omega}$",ls = "--", color = "black")
ax2.plot(X, Y,ls = "--", color = "grey")
plt.savefig(os.path.join("plots", "plot_entropy_panel_2"+"L_"+str(L)+"g_"+str(g0)+"Omega"+str(Omega)+".png"))