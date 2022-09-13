import matplotlib.pyplot as plt
import numpy as np
import os
import json
from matplotlib import gridspec
import matplotlib as mpl
#sns.set_theme()

#mpl.rcParams['font.family'] = 'Helvetica'
mpl.rcParams['lines.linewidth'] = 0.5
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
Y = Entropy_perturbation_theory(g0, X, Omega)
final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))





fontsize = 10
coeffs = [ 0.8908731 -1.04733929e-14j, -4.76957831+1.06966579e-14j]# Coefficients exctracted from a polynomial fit 
poly = np.poly1d(coeffs)
yfit = 1/np.exp(poly(np.log(Omega)))
nrow = 1
ncol = 1
fig = plt.figure(figsize=(3.2, 1.5), dpi = 800) 

gs = gridspec.GridSpec(nrow, ncol, 
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.24, left=0.22, right=0.95) 


# LEFT PANEL    
ax1= plt.subplot(gs[0,0])


#plt.title("L = "+str(L)+r"$g = $"+str(g0)+r"$\omega = $"+str(Omega))


ax1.set_xlabel(r"$U$", fontsize = fontsize)
#ax.set_ylabel(r"$\frac{<J^{4}>}{L^{2}}-\frac{<J^{2}>^{2}}{L^{2}}$")
Omegas = [1, 2, 4, 8, 12]

colors = plt.cm.bone(np.array([0.1, 0.3, 0.5, 0.7, 0.9]))
#ax2 = ax.twinx()
for i in range(len(Omegas)):
    Omega = Omegas[i]
    g0 = 0.1*Omega
    print(g0)
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
    ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))
    J_sqd = np.load(os.path.join("../XXZ/current_operator", "J_sqd_jointed"+final_ID+".npy"))
    J_sqd = J_sqd / L
    ax1.plot(Us[1:], ent[1:]/J_sqd[1:], label = r"$\Omega = $"+str(Omega),marker='D', markersize = 2, markeredgecolor='black', markeredgewidth=0.4, color = colors[i])

Omega = 2
g0 = 0.1*Omega
final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))
J_sqd = np.load(os.path.join("../XXZ/current_operator", "J_sqd_jointed"+final_ID+".npy"))
J_sqd = J_sqd / L
avg = np.mean(ent[1:11]/J_sqd[1:11])
print(avg)
X = np.linspace(0, 4, 30)
Y = [avg]*30
ax1.plot(X, Y, color = "orange", ls = "--", linewidth = 1.2, label = r"$\bar{\alpha}$")

X = np.linspace(0, 4, 30)
Y = [1/yfit]*30
#ax1.plot(X, Y, color = "tan", ls = "--")
print(yfit)
#ax2.set_ylabel(r"$N_{ph} \frac{g^2}{\omega}$")
#ax2.plot(Us, entanglement2)
#ax2.plot(Us, entanglement3)
#ax1.plot(X, Y, label = r"$PT$",ls = "--", color = "grey")
ax1.set_ylabel(r"$\frac{S_{\rm{e-ph}}\;L}{\langle \, J^{2} \rangle}$", fontsize = fontsize)
ax1.set_xlim(0, 4)
ax1.set_ylim(0, 0.07)
ax1.set_yticks([0, 0.02, 0.04, 0.06])
ax1.set_yticklabels(["$0$", "$0.02$", "$0.04$", "$0.06$"], fontsize = fontsize)


#ax1.legend()
legend = ax1.legend(fontsize=5, loc='upper right', bbox_to_anchor=(1., 1.01), edgecolor='black', ncol=2)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)
ax1.set_xticks([0,1 ,2, 3, 4,])
ax1.set_xticklabels(["$0$","$1$" ,"$2$", "$3$", "$4$",], fontsize = fontsize)
for axis in ['top','bottom','left','right']:
    ax1.spines[axis].set_linewidth(0.5)
#ax2.plot(X, Y,ls = "--", color = "grey")
plt.savefig(os.path.join("plots", "quotient_J_sqd_L_"+str(L)+"g_"+str(g0)+"Omega"+str(Omega)+".png"))