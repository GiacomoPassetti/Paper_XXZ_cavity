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



def plot_occ(L ,g0, Omega, chi ):
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
    fontsize = 8
    nrow = 3
    ncol = 1

    #gs_dict = dict(width_ratios = [1., 0.1, 0.5], height_ratios=[1.], wspace=0.0, hspace=0.0, top=0.95, bottom=0.18, left=0.2, right=0.82)
    #fig, axd = plt.subplot_mosaic([['left', 'middle', 'right']], figsize = (3.2, 2.5), gridspec_kw=gs_dict)

    fig = plt.figure(figsize=(3.2, 2.5), dpi = 800)

    gs = gridspec.GridSpec(nrow, ncol,height_ratios = [1.1, 0.15, 0.6],
             wspace=0.0, hspace=0.0, top=0.87, bottom=0.16, left=0.22, right=0.82)


    ax1 = plt.subplot(gs[2,0])
    axSpace = plt.subplot(gs[1,0])
    ax2 = plt.subplot(gs[0,0])

    axSpace.axis('off')

    colors = plt.cm.bone(np.linspace(0, 1, 7))

    #ax2.set_xscale("log")

    xArr = np.linspace(0, 10., 100)
    xDiscreteArr = np.logspace(0.7, 2, 10)
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)


    yArr1 = np.load(os.path.join("../XXZ/photon_occupation", "photon_occupation_jointed"+final_ID+".npy"))

    
    MF_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(600)+"g_"+"{:.2f}".format(g0)
    yArr2 = np.load(os.path.join("MF_data" ,"mean_field_photon_occupation_jointed"+MF_ID+".npy"))


    yArr_ent = np.load(os.path.join("../XXZ/entanglement_entropy" ,"entanglement_jointed"+final_ID+".npy"))


    T_sq = np.load(os.path.join("../XXZ/kinetic_operator", "re_k_Jointed" + final_ID + ".npy"))

    def photNumFromT(T):
        return np.sinh(np.log(np.sqrt(1 + 2 * 0.3 **2 / Omega * T / L))) ** 2

    nPhotT = np.zeros(len(T_sq))
    for tInd in range(len(T_sq)):
        nPhotT[tInd] = photNumFromT(T_sq[tInd])

    print(nPhotT[0])
    print(yArr2[0])

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

    ax1.plot(Ussr, yArr1, color = colors[2], label= "DMRG", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    ax3.plot(Ussr, yArr_ent,color = '#E6BB7F', marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label = r"$S_{e-ph}$", lw = 0.8)
    ax1.plot(Ussr, yArr2 ,color = 'red', ls = "--", linewidth = 0.8, label = r"$\rm{MF}$", zorder = 666666666666)
    #ax1.plot(Ussr, nPhotT ,color = 'green', ls = "-", linewidth = 0.8, label = r"$\rm{MF}$")
    ax1.plot([], [],color = '#E6BB7F', label = r"$S_{\rm{e{-}ph}}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    

    plot_dmrg, = ax2.plot(Ussr, yArr1, color = colors[2],marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label= "DMRG")
    plot_MF, = ax2.plot(Ussr, yArr2,color = 'red', ls = "--", linewidth = 0.8, label = r"$\rm{MF}$")

    plot_S, = ax4.plot(Ussr, yArr_ent,color = '#E6BB7F', marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6, label = r"$S_{e-ph}$", lw = 0.8)
    

  

    ax1.set_xlabel(r"$U\left[t_{\rm h}\right]$", fontsize = fontsize, loc = "center")
    ax2.set_xlabel(r"$U\left[t_{\rm h}\right]$", fontsize = fontsize, loc = "center")
    #ax1.set_xlabel(r"$U$", fontsize = fontsize, loc = "right")
    ax1.set_ylabel(r"$N_{\rm{phot}}$", fontsize = fontsize)
    ax2.set_ylabel(r"$N_{\rm{phot}}$", fontsize = fontsize)
    ax3.set_ylabel(r"$S_{\rm{f{-}ph}}$", fontsize = fontsize)
    ax4.set_ylabel(r"$S_{\rm{f{-}ph}}$", fontsize = fontsize)



    #ax1.set_yticks([0, 0.025, 0.055])
    #ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])
    
    ax3.set_yticks([])
    
    ax1.set_ylim(0, 0.006)
    ax2.set_ylim(0, 0.006)
    ax3.set_ylim(0, 0.04)
    ax4.set_ylim(0, 0.04)
    ax2.set_xlim(-6, 100)
    ax4.set_xlim(0, 100)
    ax1.set_xlim(0, 6)
    ax3.set_xlim(0, 6)
    #ax4.set_yticks([0 , 0.09, 0.18])
    #ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])
   
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.5)
        ax2.spines[axis].set_linewidth(0.5)
    for axis in ['top','bottom','left','right']:
        ax3.spines[axis].set_linewidth(0.0)
        ax4.spines[axis].set_linewidth(0.0)

    ax1.set_xticks([0, 2, 4, 6, ])
    ax1.set_xticklabels([r"$0$", "$2$", "$4$", "$6$"] ,fontsize = fontsize)
    #ax2.set_xticks([10, 100])
    #ax2.set_xticklabels([r"$10^{1}$", r"$10^{2}$"] ,fontsize = fontsize)
    
    ax2.set_xticks([0,  50, 100])
    ax2.set_xticklabels([r"$0$", r"$50$", "$100$"] ,fontsize = fontsize)
    ax1.set_yticks([])
    ax1.set_yticks([0, 0.002, 0.004, 0.006])
    ax1.set_yticklabels([r"$0$", r"$0.002$", r"$0.004$", r"$0.006$"] ,fontsize = fontsize)
    ax2.set_yticks([0, 0.002, 0.004, 0.006])
    ax2.set_yticklabels([r"$0$", r"$0.002$", r"$0.004$", r"$0.006$"] ,fontsize = fontsize)
    prop = dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
            shrinkA=0,shrinkB=0, color = colors[2])

    ax1.annotate("", xy=(0.1,.003), xytext=(1.5,0.001), arrowprops=prop)
    prop2 = dict(arrowstyle="-|>,head_width=0.4,head_length=0.8",
            shrinkA=0,shrinkB=0, color = '#E6BB7F')

    ax1.annotate("", xy=(5.9,.004), xytext=(4.9,0.0035), arrowprops=prop2)
    ax3.set_yticks([0, 0.01, 0.02, 0.03, 0.04])
    ax3.set_yticklabels([r"$0$", r"$0.01$", r"$0.02$", r"$0.03$", r"$0.04$"] ,fontsize = fontsize)
    ax4.set_yticks([0, 0.01, 0.02, 0.03, 0.04])
    ax4.set_yticklabels([r"$0$", r"$0.01$", r"$0.02$", r"$0.03$", r"$0.04$"] ,fontsize = fontsize)
    
    
    ax1.text(1, 0.003, "BKT", color = "silver")
    ax1.axvline(2, 0, 1, zorder = 0, ls = "dashdot", color = "silver", linewidth = 0.85)
    #legend = ax1.legend(fontsize=6, loc='upper left', bbox_to_anchor=(0, .99), edgecolor='black', ncol=1)
    #legend.get_frame().set_alpha(0.)
    #legend.get_frame().set_boxstyle('Square', pad=0.1)
    #legend.get_frame().set_linewidth(0.0)
    axins = inset_axes(ax2, width=0.75, height=0.6, loc = "upper right")
    rect = patches.Rectangle((0, 0), 6, 0.0395, linewidth=0.5 , edgecolor='black', facecolor='none',zorder = 10000000)
    from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
    legend = ax2.legend( [(plot_dmrg, plot_S), plot_MF], ['DMRG', 'MF'],fontsize=6, loc='upper center', edgecolor='black', ncol=1, bbox_to_anchor=(0.3, 1.01), numpoints=1,
              handler_map={tuple: HandlerTuple(ndivide=None)})
    legend.get_frame().set_alpha(0.)
    legend.get_frame().set_boxstyle('Square', pad=0.1)
    legend.get_frame().set_linewidth(0.0)
# Add the patch to the Axes
    ax4.add_patch(rect)
    from matplotlib.patches import ConnectionPatch
    xy1 = (0,0)
    xy2 = (0, 0.006)
    con = ConnectionPatch(xyA=xy1, xyB=xy2, coordsA="data", coordsB="data",
                          axesA=ax2, axesB=ax1, color="black", lw = 0.5, zorder = -95)
    xy1 = (6,0)
    xy2 = (6, 0.006)
    conB = ConnectionPatch(xyA=xy1, xyB=xy2, coordsA="data", coordsB="data",
                      axesA=ax2, axesB=ax1, color="black", lw = 0.5, zorder = -95)
    ax2.add_artist(con)
    ax2.add_artist(conB)
    plotPtGSWithCoh(axins, chi, g0, Omega)
    ax2.xaxis.tick_top()
    ax2.xaxis.set_label_position('top') 
    plt.text(0.16, 0.94, r"$\rm{a)}$", fontsize=10, transform=plt.gcf().transFigure)
    plt.savefig(os.path.join("plots" ,"fig1a.png"))

    
L = 110
g0 = 0.3
Omega = 1
chi = 1000
plot_occ(L ,g0, Omega, chi )
