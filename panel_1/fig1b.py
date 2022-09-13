import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import gridspec
import matplotlib as mpl




fontsize = 10
mpl.rcParams['lines.linewidth'] = 2
mpl.rcParams['lines.markersize'] = 8
mpl.rcParams['font.size'] = 8  # <-- change fonsize globally
mpl.rcParams['legend.fontsize'] = 8
mpl.rcParams['axes.titlesize'] = 8
mpl.rcParams['axes.labelsize'] = 8
mpl.rcParams['xtick.major.size'] = 3
mpl.rcParams['ytick.major.size'] = 3
mpl.rcParams['xtick.major.width'] = .5
mpl.rcParams['ytick.major.width'] = .5
mpl.rcParams['xtick.direction'] = 'in'
mpl.rcParams['ytick.direction'] = 'in'
mpl.rcParams['figure.titlesize'] = 8
Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
US_dmrg = np.append(Us, np.logspace(np.log10(4), 2, 20))

print(US_dmrg)

chi = 600
L = 110
#Ls = [110]
Omega = 1
g0 = 0.3

def squeezing(U, T):
  return 1/(Omega*np.sqrt(1 + 2*(T/L)*g0**2/Omega))

def PT_A(U, Omega, g0):
  PT_A = ((2*g0**2)/(U+Omega)**2)
  PT_A += (2*np.sqrt(2)*g0**2)/((U + Omega)*(U + (2*Omega)))
  return PT_A

PT = PT_A(US_dmrg, Omega, g0)


nphs =[]
fig = plt.figure(figsize=(3.2, 2.5), dpi = 800) 
nrow = 1
ncol = 2
gs = gridspec.GridSpec(nrow, ncol,width_ratios = [1, 1],
             wspace=0.0, hspace=0.0, top=0.95, bottom=0.16, left=0.2, right=0.95)
ax1 = plt.subplot(gs[0,0])
ax2 = plt.subplot(gs[0,1])


final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(1000)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
A_sqd = np.load(os.path.join("../XXZ/photon_occupation", "A_sqd_jointed"+final_ID+".npy"))
T_sq = np.load(os.path.join("../XXZ/kinetic_operator", "re_k_Jointed"+final_ID+".npy"))

print(T_sq.shape)

US_squeeze = np.arange(0, 4.0, 0.2)
US_squeeze = US_dmrg
US_squeeze_plot = []
ADD_sq = []
for i in range(52):
  print(US_squeeze[i], T_sq[i])
  if T_sq[i] == 0:
    print("fail")
  else:
    ADD_sq.append(squeezing(US_squeeze[i], 2*T_sq[i]))
    US_squeeze_plot.append(US_squeeze[i])


final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)
MF_A = np.load(os.path.join("MF_data", "mean_field_A_sqd_jointed"+final_ID+".npy"))
PT = PT + MF_A
ax1.plot(US_dmrg, A_sqd, color = 'lightcoral', label= "DMRG", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
ax1.plot(US_dmrg, MF_A, ls = "--", color = "black", label = "MF",  linewidth = 0.8)
#ax2.plot(US_dmrg, PT, ls = "--", color = "gray", label = "PT")
#ax1.plot(US_dmrg, PT, ls = "--", color = "gray", label = "PT")

ax1.set_xlim(0, 4)
#ax.legend()
ax1.plot(US_squeeze_plot, ADD_sq, zorder = -666, label = "Eq.~")
ax2.plot(US_squeeze_plot, ADD_sq, label = "Eq.~")
ax1.set_xlabel(r"$U$", fontsize = fontsize)
#ax1.set_xlabel(r"$U$", fontsize = fontsize, loc = "right")
ax1.set_ylabel(r"$<\left(a+a^{\dagger}\right)^{2}>$", fontsize = fontsize)
ax2.plot(US_dmrg, A_sqd, color = 'lightcoral', label= "DMRG", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
ax2.plot(US_dmrg, MF_A, ls = "--", color = "black", label = "MF",  linewidth = 0.8)
ax2.set_xscale("log")
ax2.set_xlim(4, 100)
ax2.set_yticks([])
ax2.set_xticks([10, 100])
ax2.text(4., 0.95, r"$<(a+a^{\dagger})> = 0$", fontsize = 10)
ax1.set_ylim(0.94, 1)
ax2.set_ylim(0.94, 1)
ax1.set_xticks([0, 1, 2, 3, 4], )
ax1.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)
ax1.set_yticks([0.94, 0.96, 0.98, 1], )
ax1.set_yticklabels([r"$0.94$", "$0.96$", "$0.98$", "$1$"] ,fontsize = fontsize)
for axis in ['top','bottom','left','right']:
   ax1.spines[axis].set_linewidth(0.5)
   ax2.spines[axis].set_linewidth(0.5)
#ax.set_xscale("log")
#ax.set_yscale("log")

legend = ax1.legend(fontsize=6, loc='upper left', edgecolor='black', ncol=1)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)
plt.savefig(os.path.join("plots","fig1b"+".png"))

#fig, ax = plt.subplots()
#plt.title(r"$\Omega$ = "+str(Omega))
#for L in Ls:
#     final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
#     nphs = np.load(os.path.join("photon_occupation", "photon_occupation_jointed"+final_ID+".npy"))
#     ax.plot(Us[0:5], nphs[0:5], label = r"L = "+str(L), marker = "D")
#ax.legend()
#ax.set_xlabel("U")
#ax.set_ylabel(r"$N_{ph}$")
#ax.set_xscale("log")
#ax.set_yscale("log")
#plt.savefig(os.path.join("plots","n_ph_omega_log_log_"+str(Omega)+".png"))