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

from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fontsize = 10
colors = plt.cm.pink(np.linspace(0, 1, 7))

Ls = [22, 50, 110]
g0 = 0.3
Omega = 1
chi = 1000
def inset_corr(ax1):
   #mpl.rcParams['lines.linewidth'] = 2
   #mpl.rcParams['lines.markersize'] = 8
   #mpl.rcParams['font.size'] = 8  # <-- change fonsize globally
   #mpl.rcParams['legend.fontsize'] = 8
   #mpl.rcParams['axes.titlesize'] = 8
   #mpl.rcParams['axes.labelsize'] = 8
   #mpl.rcParams['xtick.major.size'] = 3
   #mpl.rcParams['ytick.major.size'] = 3
   #mpl.rcParams['xtick.major.width'] = .5
   #mpl.rcParams['ytick.major.width'] = .5
   #mpl.rcParams['xtick.direction'] = 'in'
   #mpl.rcParams['ytick.direction'] = 'in'
   #mpl.rcParams['figure.titlesize'] = 8
   Ussr1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
   Ussr2 = np.arange(1.5, 4.1, 0.1)
   Ussr= np.append(Ussr1, Ussr2)
   Ussr = np.append(Ussr, np.logspace(np.log10(4), 2, 20))
   fontsize = 10
   #nrow = 1
   #ncol = 1
   #fig = plt.figure(figsize=(3.2, 2.5), dpi = 800) 

   #gs = gridspec.GridSpec(nrow, ncol,
   #         wspace=0.0, hspace=0.0, top=0.95, bottom=0.18, left=0.23, right=0.95) 
   #ax1 = plt.subplot(gs[0,0])
   
   
   
   chis = [1000, 1500, 1000, 1000]
   for i in range(len(Ls)):
        final_ID = "L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
        yArr1 = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
        final_ID = "correlation_functions_jointedL_"+"{:.2f}".format(Ls[i])+"chi_"+str(chis[i])+"g_0.00omega_2.000"
        data_g0 = np.load(os.path.join("data", final_ID+".npy")).reshape(32)
   
        yArr1 = yArr1[0:32] - data_g0
        ax1.plot(Ussr[0:32], yArr1, color = colors[-3 -i], label= r"$L = $"+str(Ls[i]))
   final_ID = "new_U_L_"+"{:.2f}".format(210)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
   yArr1 = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
   final_ID = "new_U_L_"+"{:.2f}".format(210)+"chi_"+str(chi)+"g_"+"{:.2f}".format(0)+"omega_"+"{:.3f}".format(Omega)
   data_g0 = np.load(os.path.join("../XXZ/correlation_functions", "correlation_functions_jointed"+final_ID+".npy"))
   print(yArr1, data_g0)
   yArr1 = yArr1[0:52] - data_g0[0:52]
   new_Us = np.arange(0, 4.2, 0.2)
   ax1.plot(new_Us, yArr1, color = colors[-6], label= r"$L = $"+str(210),  marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.4)
   

   
   #MF = np.load(os.path.join("data", "mean_field_correlation_functions_jointedL_110.00chi_600g_0.30omega_1.000.npy"))
   #MF = MF.reshape(32)
   #MF = MF - data_g0
   #ax1.plot(Ussr[0:32], MF,
   #label= r"$L = $"+str(Ls[i])+r"$- \rm{MF}$", ls = "--", color = "black")
   #
   
   
   
   
   ax1.set_xlabel(r"$U\left[t_{\rm h}\right]$", fontsize = fontsize)
   ax1.set_ylabel(r"$C-C|_{g = 0}$", fontsize = fontsize)
   
   #ax1.set_yticks([0, 0.025, 0.055])
   #ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])
   
   
   ax1.set_ylim(0, 0.002)
   
   ax1.set_xlim(0, 4)
   
   #ax4.set_yticks([0 , 0.09, 0.18])
   #ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])
   
   for axis in ['top','bottom','left','right']:
      ax1.spines[axis].set_linewidth(0.5)
   
   ax1.set_xticks([], )
   #ax1.set_xticklabels([r"$0$", "$1$", "$2$", "$3$", "$4$"] ,fontsize = fontsize)
   ax1.set_yticks([] )
   #ax1.set_yticklabels([r"$0$", r"$10^{-2}$", r"$2\dot 10^{-2}$" ] ,fontsize = fontsize)
   
   #ax1.set_yticks([0, 0.002, 0.004, 0.006])
   #ax1.set_yticklabels([r"$0$", r"$0.002$", r"$0.004$", r"$0.006$"] ,fontsize = fontsize)
   
   legend = ax1.legend(fontsize=6, loc='upper left', bbox_to_anchor=(-0.02, 1.02), edgecolor='black', ncol=1)
   legend.get_frame().set_alpha(0.)
   legend.get_frame().set_boxstyle('Square', pad=0.1)
   legend.get_frame().set_linewidth(0.0)
   

   
       
   
   
   
   
   
   
   # %%
   
# %%
