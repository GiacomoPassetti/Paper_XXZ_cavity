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
g0 = 1
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

Ussr= np.arange(0, 4.2, 0.2)

fontsize = 10
nrow = 1
ncol = 1
fig = plt.figure(figsize=(3.2, 2.7), dpi = 800) 
colors = plt.cm.copper(np.linspace(0, 1, 5))
gs = gridspec.GridSpec(nrow, ncol,
         wspace=0.0, hspace=0.0, top=0.91, bottom=0.18, left=0.3, right=0.95) 
ax1 = plt.subplot(gs[0,0])

colors = plt.cm.copper(np.linspace(0, 1, 5))

Ls = [50]
chis = [1000]
for i in range(len(Ls)):
     final_ID = "new_U_L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
     yArr1 = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
     final_ID = "new_U_L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(0)+"omega_"+"{:.3f}".format(Omega)
     yArr2= np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))

     
for i in range(len(list(yArr1))):
    if yArr1[i] == 0:
        yArr1[i] = yArr1[i+1]
    else:
        print("okke")
yArr1 = yArr1 - yArr2
ax1.plot(Ussr, yArr1, color = colors[2], label= r"$L = $"+str(110)+r"$g = 1$", marker='D', markeredgecolor='black', markersize = 2, markeredgewidth=0.4)


#ax1.plot(Ussr, yArr2, color = colors[0], label= r"$L = $"+str(Ls[i])+r"$g = 0$", marker='D', markeredgecolor='black', markersize = 2, markeredgewidth=0.4)









ax1.set_xlabel(r"$U$", fontsize = fontsize)
ax1.set_ylabel(r"$C$", fontsize = fontsize)

#ax1.set_yticks([0, 0.025, 0.055])
#ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])




ax1.set_xlim(0, 4)

#ax4.set_yticks([0 , 0.09, 0.18])
#ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])

for axis in ['top','bottom','left','right']:
   ax1.spines[axis].set_linewidth(0.5)

ax1.set_xticks([0, 1, 2, 3, 4], )
ax1.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)





legend = ax1.legend(fontsize=6, loc='center left', bbox_to_anchor=(0, .2), edgecolor='black', ncol=1)
legend.get_frame().set_alpha(0.)
legend.get_frame().set_boxstyle('Square', pad=0.1)
legend.get_frame().set_linewidth(0.0)

plt.savefig(os.path.join("plots" ,"fig3_check.png"))

    






# %%

# %%
