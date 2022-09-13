# %%
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

fontsize = 10


Ls = [22, 50, 110]
g0 = 0.3
Omega = 1
chi = 1000

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
Ussr1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
Ussr2 = np.arange(1.5, 4.1, 0.1)
Ussr= np.append(Ussr1, Ussr2)
Ussr = np.append(Ussr, np.logspace(np.log10(4), 2, 20))
fontsize = 10
nrow = 1
ncol = 1
fig = plt.figure(figsize=(3.2, 2.7), dpi = 800) 
colors = plt.cm.copper(np.linspace(0, 1, 5))
gs = gridspec.GridSpec(nrow, ncol,
         wspace=0.0, hspace=0.0, top=0.91, bottom=0.18, left=0.3, right=0.95) 
ax1 = plt.subplot(gs[0,0])

colors = plt.cm.copper(np.linspace(0, 1, 5))

Ls = [110]
chis = [1000]
for i in range(len(Ls)):
     final_ID = "L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
     yArr1 = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
     final_ID = "correlation_functions_jointedL_"+"{:.2f}".format(Ls[i])+"chi_"+str(chis[i])+"g_0.00omega_2.000"
     data_g0 = np.load(os.path.join("data", final_ID+".npy")).reshape(32)

     yArr1 = yArr1[0:32] - data_g0
     ax1.plot(Ussr[0:32], yArr1, color = colors[2], label= r"$\rm{DMRG}$", marker='D', markeredgecolor='black', markersize = 2, markeredgewidth=0.4)


final_ID = "renormalized_U_jointed_L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
renormU = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
final_ID = "correlation_functions_jointedL_"+"{:.2f}".format(Ls[i])+"chi_"+str(chis[i])+"g_0.00omega_2.000"
data_g0 = np.load(os.path.join("data", final_ID+".npy")).reshape(32)
renormU = renormU[0:32] - data_g0
ax1.plot(Ussr[0:32], renormU, color = 'lightgreen', label= r"$t_{eff}$")



MF = np.load(os.path.join("data", "mean_field_correlation_functions_jointedL_110.00chi_600g_0.30omega_1.000.npy"))
MF = MF.reshape(32)
MF = MF - data_g0
ax1.plot(Ussr[0:32], MF,label= r"$\rm{MF}$", ls = "--", color = "black")





ax1.set_xlabel(r"$U$", fontsize = fontsize)
ax1.set_ylabel(r"$C-C|_{g = 0}$", fontsize = fontsize)

#ax1.set_yticks([0, 0.025, 0.055])
#ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])


ax1.set_ylim(0, 0.002)

ax1.set_xlim(0, 4)

#ax4.set_yticks([0 , 0.09, 0.18])
#ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])

for axis in ['top','bottom','left','right']:
   ax1.spines[axis].set_linewidth(0.5)

ax1.set_xticks([0, 1, 2, 3, 4], )
ax1.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)
print(np.linspace(0, 0.0015, 5))
ax1.set_ylim(0, 0.0015)
ax1.set_yticks([0.  , 0.0005, 0.001,  0.0015,])
#ax1.set_yticks([0, 0.002, 0.004, 0.006])
ax1.set_yticklabels([r"$0$", r"$0.5$", r"$1$", r"$1.5$"] ,fontsize = fontsize)
ax1.text(0.05, 0.00152, r"$\cdot 10^{-3}$", fontsize = fontsize)
legend = ax1.legend(fontsize=6, loc='center left', bbox_to_anchor=(0, .2), edgecolor='black', ncol=1)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)
axins = ax1.inset_axes([0.125, 0.5, 0.45, 0.45])
inset_corr(axins)
plt.savefig(os.path.join("plots" ,"fig3b.png"))

    






# %%

# %%
