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
from fig1aInset import plotPtGSWithCoh
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

fontsize = 10

def plot_occ(L ,g ):
    Ussr1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
    Ussr2 = np.arange(1.5, 4.1, 0.1)
    Ussr= np.append(Ussr1, Ussr2)
    fontsize = 10
    nrow = 1
    ncol = 2
    fig = plt.figure(figsize=(3.75, 2.5), dpi = 800) 
    
    gs = gridspec.GridSpec(nrow, ncol,width_ratios = [1.3, 1],
             wspace=0.0, hspace=0.0, top=0.95, bottom=0.18, left=0.2, right=0.82) 




    ax1 = plt.subplot(gs[0,0])
    ax2 = plt.subplot(gs[0,1])


    for axis in ["top", "bottom", "left", "right"]:
        ax1.spines[axis].set_linewidth(0.5)
        ax2.spines[axis].set_linewidth(0.5)

    ax1.spines["top"].set_linewidth(0.)
    ax2.spines["top"].set_linewidth(0.)
    ax1.spines["right"].set_linewidth(0.)
    ax2.spines["left"].set_linewidth(0.)

    ax2.set_xscale("log")

    xArr = np.linspace(0, 10., 100)
    xDiscreteArr = np.logspace(0.7, 2, 10)


    dmrg_ID = "{:.2f}".format(g)+"L_"+"{:.2f}".format(L)+"chi_"+str(1000)+"g_"+"{:.2f}".format(g/np.sqrt(L))
    yArr1 = np.load(os.path.join("DMRG_data" ,"dmrg_linear_"+dmrg_ID+".npy"))
    yDiscreteArr1 = np.load(os.path.join("DMRG_data" ,"dmrg_log_"+dmrg_ID+".npy"))
    
    final_ID = "nphs__L"+"{:.2f}".format(L)+"{:.2f}".format(g)
    yArr2 = np.load(os.path.join("MF_data" ,"mf_linear.npy"+final_ID+".npy"))

    final_ID = "nphs_log_datas_L"+"{:.2f}".format(L)+"g_"+"{:.2f}".format(g)
    yDiscreteArr2 = np.load(os.path.join("MF_data", "mf_log.npy"+final_ID+".npy"))

    ent_ID = "{:.2f}".format(g)+"L_"+"{:.2f}".format(L)+"chi_"+str(1000)+"g_"+"{:.2f}".format(g/np.sqrt(L))
    yArr_ent = np.load(os.path.join("DMRG_data" ,"dmrg_linear_ent"+ent_ID+".npy"))
    yDiscreteArr_ent = np.load(os.path.join("DMRG_data" ,"dmrg_log_ent"+ent_ID+".npy"))


    critVal = 2.
    X = xArr
    Y = np.linspace(np.amin(yArr1), np.amax(yArr1), 100)
    length = len(xArr)
    mu = 10
    cdashing = np.zeros((int(length)))
    for i in range(int(length/2)):
        #cdashing[i+int(length/4)] = np.exp(-abs(i-int(length/4))/19)
        cdashing[i+int(length/4)] = 1/(np.exp((abs(i-int(length/4))- mu)*0.5)+1)

    ax3 = ax1.twinx()
    ax4 = ax2.twinx()

    ax1.plot(Ussr, yArr1, color = 'lightcoral', label= "DMRG", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    ax1.plot(Ussr, yArr2 ,color = 'black', ls = "--", linewidth = 0.8, label = r"$MF$")
    ax1.plot([], [],color = 'cornflowerblue', label = r"$S_{e-ph}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    ax3.plot(Ussr, yArr_ent,color = 'cornflowerblue', marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label = r"$S_{e-ph}$")

    ax2.plot(xDiscreteArr, yDiscreteArr1, color = 'lightcoral',marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label= "DMRG")
    ax2.plot(xDiscreteArr, yDiscreteArr2,color = 'black', ls = "--", linewidth = 0.8, label = r"$MF$")

    ax4.plot(xDiscreteArr, yDiscreteArr_ent,color = 'cornflowerblue', marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label = r"$S_{e-ph}$")

    ax2.yaxis.tick_right()
    ax2.yaxis.set_label_position("right")

    ax1.xaxis.set_label_coords(0.8, -0.10)

    ax1.set_xlabel(r"$U$", fontsize = fontsize, loc = "right")
    ax1.set_ylabel(r"$N_{\rm phot}$", fontsize = fontsize)

    ax4.set_ylabel(r"$S_{\rm e-ph}$", fontsize = fontsize)

    ax1.set_xticks([ 0., 2, ])
    ax1.set_xticklabels(["$0$", "$2$",])


    ax1.set_yticks([0, 0.025, 0.055])
    ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])
    ax3.set_ylim([0, 0.22])
    ax3.set_yticks([])
    ax2.set_yticks([])
    ax2.set_ylim(0, 0.055)
    ax4.set_ylim(0, 0.22)
    ax2.set_xlim(4, xDiscreteArr[-1])
    ax4.set_xlim(4, xDiscreteArr[-1])
    ax1.set_xlim(0, 4)
    ax3.set_xlim(0, 4)
    ax4.set_yticks([0 , 0.09, 0.18])
    ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])
   

    
    ax1.legend(loc='center left', prop={'size': 8})
    axins = inset_axes(ax2, width=0.7, height=0.7)
    plotPtGSWithCoh(axins)
    plt.savefig(os.path.join("plots" ,"final_plot_photon_versus_U.png"))

    
L = 50 
g = 1
plot_occ(L, g)




# %%

# %%
