import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np
import os
import json
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


fontsize = 10


Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
Us = np.append(Us1, Us2)
U_log = np.logspace(np.log10(4), 2, 20)
Us = np.append(Us, U_log)


L = 110
chi = 1000
U = 4
g0 = 0.5
g = 0.5
Omega = 10

def squeezing(U, T):
  return 1/(Omega*np.sqrt(1 + 2*(T/L)*g0**2/Omega))


final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)

ord_par = np.load("../XXZ/current_operator/J_sqd_jointed"+final_ID+".npy")
#ord_par = np.load("../XXZ/current_operator/current_fluctuations_jointed"+final_ID+".npy")
ord_par = ord_par/L
nph_left = np.load("../XXZ/photon_occupation/photon_occupation_jointed"+final_ID+".npy")
T_sq = np.load(os.path.join("../XXZ/kinetic_operator", "re_k_Jointed"+final_ID+".npy"))

#ord_par = ord_par / L**2

print(T_sq.shape)

print(ord_par)

def photNumFromT(T):
    return np.sinh(np.log(np.sqrt(1 + 2 * g**2 / Omega * T / L)))**2

nPhotT = np.zeros(len(T_sq))
for tInd in range(len(T_sq)):
    nPhotT[tInd] = photNumFromT(T_sq[tInd])

print(nPhotT)


ord_par = ord_par*((g**2)/(Omega**2))
ord_par = ord_par# + nph_left[0]

nph_right =nph_left

X = np.linspace(0, 100, 300)
def perturbation_theory(U):
    return  (g**2)/((U + Omega)**2)
Y = perturbation_theory(X)

def plot_im(array=None, ind=0):
    """A function to plot the image given a images matrix, type of the matrix: \
    either original or fool, and the order of images in the matrix"""
    img_reshaped = array[ind, :].reshape((28, 28))
    imgplot = plt.imshow(img_reshaped)

colors = plt.cm.bone(np.linspace(0, 1, 7))

nrow = 1
ncol = 3
fig = plt.figure(figsize=(3.2, 1.5), dpi = 800) 

gs = gridspec.GridSpec(nrow, ncol, width_ratios=[1, 0.1, 1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.25, left=0.18, right=0.96)

axSpace = plt.subplot(gs[0,1])
axSpace.axis('off')
# LEFT PANEL    
ax= plt.subplot(gs[0,0])

ax.plot(Us[1:], ord_par[1:], label = r"$\frac{<J^{2}>}{L}\,\frac{g^{2}}{\omega^{2}}$",color = "goldenrod", ls = "--" , linewidth=1.2)
#ax.plot(U_MF, nph_MF, ls = "--", color = "black", label = "MF")
ax.plot(X[1:], Y[1:], label = r"$\rm{PT}$", color = "darkseagreen", ls = "--", linewidth=1.2)

ax.plot(Us[1:], (nph_left[1:] - nPhotT[1:]), label = r"$\rm{DMRG}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral", )
#ax.set_xticklabels([])
#ax.set_yticklabels([])

ax.set_ylim(3 * 1.e-6, 2. * 1.e-2)

ax.set_xlim(0, 4)
ax.set_yscale("log")
ax.set_ylabel(r"$N_{\rm{phot}}$", fontsize = fontsize)
#ax.set_xlabel(r"$U$", loc = "right", fontsize = fontsize)
ax.set_xlabel(r"$U$", fontsize = fontsize, horizontalalignment='right', x=1.04)
for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(0.5)
for axis in ['right']:
    ax.spines[axis].set_linewidth(0.0)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)
ax.set_yticks([1e-4, 1e-2])
ax.set_yticklabels([r"$10^{-2}$", r"$10^{-4}$"], fontsize = fontsize)

#RIGHT PANEL
ax= plt.subplot(gs[0,2])
#ax.plot(Us, nph_MF, ls = "--", color = "black", label = r"$MF$")
ax.plot(Us, ord_par, label = r"$\frac{<J^{2}>}{L}\,\frac{g^{2}}{\omega^{2}}$", color = "goldenrod", ls = "--", linewidth=1.2)
ax.plot(Us, nph_right - nPhotT,  marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral",)
ax.plot(X, Y, label = r"$\rm{PT}$", color = "darkseagreen", ls = "--", zorder = 666, linewidth=1.2)
ax.plot(Us, nph_left - nPhotT , label = r"$\rm{DMRG}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral",)
ax.set_xticks([10, 100])
ax.set_xticklabels([r"$10^{1}$", r"$10^{2}$"] ,fontsize = fontsize)

ax.set_yscale("log")
ax.set_xscale("log")
ax.set_yticklabels([])
print(Us.shape)
ax.yaxis.tick_right()
X = np.log(Us[46:-1])
Y = np.log(nph_right[46:-1])

z = np.polyfit(X, Y, 1)


print(z)
z = [-1.88, -2]
p = np.poly1d(z)
X = np.log(Us[32:-1])
X = np.linspace(X[0], 100, 200)

ax.plot(np.exp(X), np.exp(p(X)), color = "red", lw = 0.8, label = r"$p1 = -2$")
ax.yaxis.tick_right()
ax.set_xlim(4, 100)

#ax.tick_params(left = False, which="both")
legend = ax.legend(fontsize=5, loc='upper left', bbox_to_anchor=(-0.95, 1.05), edgecolor='black', ncol=3)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)
ax.set_ylim(3 * 1.e-6, 2. * 1.e-2)


for axis in ['top','bottom','left','right']:
    ax.spines[axis].set_linewidth(0.5)
for axis in ['left']:
    ax.spines[axis].set_linewidth(0.0)

plt.savefig(os.path.join("plots", "fig2b.png"))
