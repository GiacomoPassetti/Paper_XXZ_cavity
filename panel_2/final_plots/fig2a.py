import matplotlib.pyplot as plt
import numpy as np
import os
from matplotlib import gridspec
import matplotlib as mpl
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
#sns.set_theme()

#mpl.rcParams['font.family'] = 'Helvetica'
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
#mpl.rc('text', usetex=True)


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



final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)

J_sqd = np.load(os.path.join("../../XXZ/current_operator" ,"J_sqd_jointed"+final_ID+".npy"))
J_sqd = J_sqd/L
coeffs = [ 0.8908731 -1.04733929e-14j, -4.76957831+1.06966579e-14j]# Coefficients exctracted from a polynomial fit 
poly = np.poly1d(coeffs)
fontsize = 10

from scipy.optimize import curve_fit
def func_powerlaw(x, m, c, c0):
    return c0 + x**m * c

target_func = func_powerlaw

fontsize = 10
nrow = 1
ncol = 3
fig = plt.figure(figsize=(3.2, 3.2), dpi = 800)
#fig = plt.figure(figsize=(3.2, 1.5), dpi = 800)

gs = gridspec.GridSpec(nrow, ncol, width_ratios=[1, 0.1 ,1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.24, left=0.18, right=0.95)

Omegas = [1, 2, 4, 8, 12]

colors = plt.cm.bone(np.linspace(0, 1, len(Omegas)+2))
# LEFT PANEL    
ax1 = plt.subplot(gs[0,0])
axSpace = plt.subplot(gs[0,1])
ax2 = plt.subplot(gs[0,2])
#plt.title("L = "+str(L)+r"$g = $"+str(g0)+r"$\omega = $"+str(Omega))
axSpace.axis('off')
#ax1.plot(Us[1:], J_sqd[1:], color = "tan", ls = "--", linewidth = 1.2)
ax1.set_xlabel(r"$U$", fontsize = 10, horizontalalignment='right', x=1.04)
#ax1.set_xlabel(r"$U$", loc = "right", fontsize = 10)
#ax.set_ylabel(r"$\frac{<J^{4}>}{L^{2}}-\frac{<J^{2}>^{2}}{L^{2}}$")

#ax2 = ax.twinx()
for Omega in [ 2,]:
    g0 = 0.1*Omega
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
    
    ent = np.load(os.path.join("../../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))

    yfit = 1/np.exp(poly(np.log(Omega)))
    Y = Entropy_perturbation_theory(g0, X, Omega)
    ax1.plot(Us[1:], ent[1:], label = r"$\rm{DMRG}$",marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6, color = colors[2])
    ax1.plot(X[1:], Y[1:] ,ls = "--", color = "darkkhaki", linewidth = 1.2, label = r"$\rm{PT}$", zorder = 666)
    ax1.plot(Us[1:], J_sqd[1:]*0.014785685216691914, color = "orange", ls = "--", linewidth = 1.2, label = r"$\frac{\langle \, J^{2} \rangle}{L}\bar{\alpha}$")

#ax2.set_ylabel(r"$N_{ph} \frac{g^2}{\omega}$")
#ax2.plot(Us, entanglement2)
#ax2.plot(Us, entanglement3)
#ax1.plot(X, Y, label = r"$PT$",ls = "--", color = "darkkhaki")
ax1.set_ylabel(r"$S_{e-ph}$")
ax1.set_xlim(0.0, 4)

for Omega in [2]:
    g0 = 0.1*Omega
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
    ent = np.load(os.path.join("../../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))
    yfit = 1/np.exp(poly(np.log(Omega)))
    Y = Entropy_perturbation_theory(g0, X, Omega)
    ax2.plot(X[1:], Y[1:], ls = "--", color = "darkkhaki", linewidth = 1.2, label = r"$S_{\rm{e}{-}\rm{ph}}-\rm{PT}$", zorder = 99)
    ax2.plot(Us[1:], ent[1:], label = r"$S_{\rm{e}{-}\rm{ph}}-\rm{DMRG}$",marker='D', markersize = 3, markeredgecolor='black', markeredgewidth=0.6, color = colors[2])


    ax2.plot(Us[1:], J_sqd[1:]*0.014785685216691914, color = "orange", ls = "--", linewidth = 1.2, label = r"$\bar{\alpha}\;\frac{J^{2}}{L}$")

#ax2.plot(Us, J_sqd, label = r"$\frac{J^{2}}{L}$",ls = "--", color = "tan", linewidth = 1.2)
ax1.plot([], [], color = "red", label = r"$p_{1} = -2 $")
X = np.log(Us[36:-1])
Y = np.log(ent[36:-1])

z = np.polyfit(X, Y, 1)

print(z)
z = [-1.7, -2]
p = np.poly1d(z)
print(z)
X = np.log(Us[32:-1])
X = np.linspace(X[0], np.log(100), 200)
ax2.set_xlim(4, 100)
ax2.plot(np.exp(X), np.exp(p(X)), color = "red", lw = 0.8)
legend = ax1.legend(fontsize=5.8, loc='upper left', bbox_to_anchor=(0., 1), edgecolor='black', ncol=1)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)
#ax2.legend(prop={'size': 7}, loc = "upper right")
ax2.set_xscale("log")
ax2.set_yticks([])
ax2.set_ylim(1.e-6, 2 * 1.e-2)
ax1.set_ylim(1.e-6, 2 * 1.e-2)


ax1.set_yscale("log")
ax2.set_yscale("log")
ax2.yaxis.tick_right()
ax2.tick_params(left = False, which="both")
ax2.set_yticks([])
ax1.set_xticks([0, 1, 2, 3, 4], )
ax1.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)
ax2.set_xticks([10, 100])
ax2.set_xticklabels([r"$10^{1}$", r"$10^{2}$"] ,fontsize = fontsize)
ax1.set_yticks([1.e-5, 1.e-3, 1.e-2])
ax1.set_yticklabels([r"$10^{-5}$", r"$10^{-3}$", r"$10{^{-2}}$"] ,fontsize = fontsize)
#ax2.plot(X, Y,ls = "--", color = "darkkhaki")
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(0.5)
    ax2.spines[axis].set_linewidth(0.5)
for axis in ['right']:
    ax1.spines[axis].set_linewidth(0.0)
    
for axis in ['left']:

    ax2.spines[axis].set_linewidth(0.0)
#plt.show()
#plt.savefig(os.path.join("plot_entropy_collapse_first_order_LARGER_U"+"L_"+str(L)+"g_"+str(g0)+"Omega"+str(Omega)+".png"))
plt.savefig(os.path.join("fig2a.png"))