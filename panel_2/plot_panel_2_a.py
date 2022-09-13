import matplotlib.pyplot as plt
from matplotlib import gridspec
import seaborn as sns
import numpy as np
import os
import json
#sns.set_theme()

fontsize = 10


Us1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Us2 = np.arange(1.5, 4.1, 0.1)
US_left = np.append(Us1, Us2)
U_MF = np.append(US_left, np.logspace(np.log10(4.55), 2, 16))
nph_MF = []
for U in list(U_MF):
    nph_MF.append(np.load(os.path.join("mf_data","mean_field_photon_occupationL_50.00chi_600U_"+"{:.2f}".format(U)+"g_0.1000omega_1.0000.npy")))
nph_MF = np.array(nph_MF)

L = 50
chi = 1000
U = 4
g0 = 0.1
g = 0.1
Omega = 1





final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
ord_par = np.load(os.path.join("datas","J_sqd_jointed"+final_ID+".npy"))/L
nph_left = np.load(os.path.join("datas", "photon_occupation_jointed"+final_ID+".npy"))

ord_par = ord_par*((g**2)/(Omega**2))
ord_par = ord_par + nph_left[0]

nph_right = np.load(os.path.join("datas", "nph_L_50g_0.1chi_1000.npy"))

US_right = np.logspace(0.3, 2, 20)

X = np.linspace(0, 100, 300)
def perturbation_theory(U):
    return  (g**2)/((U + 1)**2)
Y = perturbation_theory(X)

def plot_im(array=None, ind=0):
    """A function to plot the image given a images matrix, type of the matrix: \
    either original or fool, and the order of images in the matrix"""
    img_reshaped = array[ind, :].reshape((28, 28))
    imgplot = plt.imshow(img_reshaped)



nrow = 1
ncol = 2
fig = plt.figure(figsize=(3.75, 2.5), dpi = 800) 

gs = gridspec.GridSpec(nrow, ncol, width_ratios=[1, 1],
         wspace=0.0, hspace=0.0, top=0.95, bottom=0.18, left=0.17, right=0.96) 


# LEFT PANEL    
ax= plt.subplot(gs[0,0])
ax.plot(US_left, ord_par, label = r"$\frac{<J^{2}>}{L}\,\frac{g^{2}}{\omega^{2}}$", color = "darkseagreen", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6,)
ax.plot(U_MF, nph_MF, ls = "--", color = "black", label = "MF")
ax.plot(X, Y, label = r"$N_{PT}$", color = "grey", ls = "--")

ax.plot(US_left, nph_left , label = r"$N_{ph}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral")
#ax.set_xticklabels([])
#ax.set_yticklabels([])

ax.set_ylim(1.e-7, 1.e-2)
ax.set_xlim(0, 3.7)
ax.set_yscale("log")
ax.set_ylabel(r"$N_{ph}$", fontsize = fontsize)
ax.set_xlabel(r"$U$", loc = "right", fontsize = fontsize)


#RIGHT PANEL
ax= plt.subplot(gs[0,1])
ax.plot(U_MF, nph_MF, ls = "--", color = "black", label = r"$MF$")
ax.plot([], [], label = r"$\frac{<J^{2}>}{L}\,\frac{g^{2}}{\omega^{2}}$", color = "darkseagreen", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6,)
ax.plot(US_right, nph_right,  marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral")
ax.plot(X, Y, label = r"$N_{PT}$", color = "grey", ls = "--")
ax.plot(US_left, nph_left , label = r"$N_{ph}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, color = "lightcoral")
#ax.set_xticklabels([])
ax.set_yscale("log")
ax.set_xscale("log")
ax.set_yticklabels([])

ax.set_xlim(3.7, 100)
ax.spines['left'].set_visible(False)
ax.tick_params(left = False, which="both")
ax.legend(prop={'size': 8}, loc = "upper right")
ax.set_ylim(1.e-7, 1.e-2)





plt.savefig(os.path.join("plots", "plot_panel_2_a.png"))
