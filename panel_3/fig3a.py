import matplotlib as mpl
import matplotlib.cm as cm
import matplotlib.colors
#import h5py
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patches
from matplotlib.colors import ListedColormap
import os
from matplotlib import gridspec
from fig3bInset import inset_corr
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

chi = 1000
L = 50
Omega = 1

X = list(np.arange(0, 4.05, 0.05))
Y = list(np.arange(0, 1.05, 0.05))


z = np.zeros((len(X)-1, len(Y)-1))
z0 = np.zeros((len(X)-1, len(Y)-1))
x = np.zeros((len(X), len(Y)))
y = np.zeros((len(X), len(Y)))

for i in range(len(X)):
    for j in range(len(Y)):
        x[i, j] = X[i]
for i in range(len(X)):
    for j in range(len(Y)):
        y[i, j] = Y[j]


def find_Us(cutoff):
    U_star = []

    for j in range(len(Y)):
        g0 = Y[j]

        final_ID = "new_U_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(
        g0) + "omega_" + "{:.3f}".format(Omega)
        correlation = np.load(os.path.join("../XXZ/", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"))
        for i in range(len(X)-1):
                    
                    if correlation[i] > cutoff :
 
                        
                        U_star.append(X[i])
                        print(U_star)
                        break
    return U_star


for j in range(len(Y)-1):
        g0 = Y[j]
        final_ID = "new_U_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(
        g0) + "omega_" + "{:.3f}".format(Omega)
        correlation = np.load(os.path.join("../XXZ/", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"))
        for i in range(len(X)-1):

             z[i, j ] = correlation[i]
#for j in range(len(Y)-1):
#        g0 = 0
#        final_ID = "new_U_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(
#        g0) + "omega_" + "{:.3f}".format(Omega)
#        correlation = np.load(os.path.join("../XXZ/", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"))
#        for i in range(len(X)-1):
#
#            if correlation[i] == 0:
#             z0[i, j ] = correlation[i+1]
#            else:
#             z0[i, j ] = correlation[i]
g0 = Y[j]

final_ID = "new_U_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "g_" + "{:.2f}".format(
g0) + "omega_" + "{:.3f}".format(Omega)
correlation = np.load(os.path.join("../XXZ/", "correlation_functions", "correlation_functions_jointed" + final_ID + ".npy"))
cutoff = correlation[9]

U_star = find_Us(0.009)
z_min, z_max = np.abs(z).min(), np.abs(z).max()



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

fig = plt.figure(figsize=(3.2, 2.7), dpi = 800) 
#ax.plot(U_star, Y, color = "black")

xs = [2]*100
ys = np.linspace(0, 1, 100)
fontsize = 10
nrow = 1
ncol = 1
gs = gridspec.GridSpec(nrow, ncol,
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.16, left=0.15, right=0.95) 
ax = plt.subplot(gs[0,0])
ax.plot(xs, ys, color = "black", ls = "--", lw = 0.6)
c = ax.pcolor(x,y , z, cmap='RdBu', vmin=z_min, vmax=z_max/5.5)
cbar = fig.colorbar(c, orientation = "horizontal", location = "top", shrink = 1, pad = 0.05,ax = ax)
cbar.outline.set_linewidth(0.5)
ax.set_xlabel(r"$U$", fontsize = fontsize)
ax.set_ylabel(r"$g$", fontsize = fontsize)
cbar.ax.set_xlabel(r"$C$", labelpad = 2.)
cbar.ax.xaxis.set_label_position("top")
ax.set_yticks([0, 0.2, 0.4, 0.6, 0.8, 1])
ax.set_yticklabels(["$0$", "$0.2$", "$0.4$", "$0.6$", "$0.8$", "$1$"], fontsize = fontsize)
ax.set_xticks([0, 1, 2, 3, 4])
ax.set_xticklabels(["$0$", "$1$", "$2$", "$3$", "$4$"], fontsize = fontsize)
#prop = dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
#        shrinkA=0,shrinkB=0, color = "gold")
#ax.annotate("", xy=(2.4,1), xytext=(2.6,0.2), arrowprops=prop)

plt.savefig(os.path.join("plots" ,"fig3a.png"))