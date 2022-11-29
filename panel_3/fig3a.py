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
from fig3aInset import plotPtGSWithCoh
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
L = 110
Nmax = 16
chi = 1000
Omega = 1
g0 = 0.3



phot_distr_MF = np.load(os.path.join("data", "mean_field_Phot_projectionL_110.00chi_600U_3.00g_0.3000omega_1.0000.npy"))
phot_distr_MF = phot_distr_MF.flatten()[:17]


U = 3
final_ID = "Fast_L_" + "{:.2f}".format(L) + "chi_" + str(chi) + "U_" + "{:.2f}".format(U) + "g_" + "{:.4f}".format(
        g0) + "omega_" + "{:.4f}".format(Omega)

phot_distr_DMRG = np.load(os.path.join("../XXZ/Phot_Projection", "Phot_projection_"+final_ID+".npy"))
phot_distr_DMRG = phot_distr_DMRG.flatten()


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

    fig = plt.figure(figsize=(3.6, 2.5), dpi = 800)

    gs = gridspec.GridSpec(nrow, ncol,height_ratios = [1.1, 0.15, 0.6],
             wspace=0.0, hspace=0.0, top=0.87, bottom=0.16, left=0.16, right=0.95)


    ax1 = plt.subplot(gs[0,0])
    axSpace = plt.subplot(gs[1,0])
    ax = plt.subplot(gs[2,0])

    axSpace.axis('off')

    colors = plt.cm.bone(np.linspace(0, 1, 7))

    #ax2.set_xscale("log")

    xArr = np.linspace(0, 10., 100)
    xDiscreteArr = np.logspace(0.7, 2, 10)
    final_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)


    yArr1 = np.load(os.path.join("../XXZ/photon_occupation", "photon_occupation_jointed"+final_ID+".npy"))

    
    MF_ID = "L_"+"{:.2f}".format(L)+"chi_"+str(600)+"g_"+"{:.2f}".format(g0)
    yArr2 = np.load(os.path.join("MF_data" ,"mean_field_photon_occupation_jointed"+MF_ID+".npy"))




    length = len(xArr)
    mu = 10
    cdashing = np.zeros((int(length)))
    for i in range(int(length/2)):
        #cdashing[i+int(length/4)] = np.exp(-abs(i-int(length/4))/19)
        cdashing[i+int(length/4)] = 1/(np.exp((abs(i-int(length/4))- mu)*0.5)+1)



    plot_dmrg, = ax1.plot(Ussr, yArr1, color = "#525E75", label= "DMRG", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    
    plot_MF, = ax1.plot(Ussr, yArr2 ,color = 'red', ls = "--", linewidth = 0.8, label = r"$\rm{MF}$", zorder = 666666666666)
    ax1.plot([3], yArr2[21], marker = "o", markersize=7,markeredgewidth= 0.8, markeredgecolor = "black", zorder = 1000, markerfacecolor="None")
    ax1.plot([3], yArr1[21], marker = "o", markersize=7, markeredgewidth= 0.8,markeredgecolor = "black", zorder = 1000, markerfacecolor="None")
    #ax1.plot(Ussr, nPhotT ,color = 'green', ls = "-", linewidth = 0.8, label = r"$\rm{MF}$")
    ax1.plot([], [],color = '#E6BB7F', label = r"$S_{\rm{e{-}ph}}$", marker='D', markeredgecolor='black', markersize = 3, markeredgewidth=0.6)
    
    ax1.set_xlabel(r"$U\left[t_{\rm h}\right]$", fontsize = fontsize, loc = "center")

    #ax1.set_xlabel(r"$U$", fontsize = fontsize, loc = "right")
    ax1.set_ylabel(r"$N_{\rm{phot}}$", fontsize = fontsize)

    #ax1.set_yticks([0, 0.025, 0.055])
    #ax1.set_yticklabels([r"$0$", r"$0.025$", r"$0.055$"])
    

    
    ax1.set_ylim(0, 0.006)


    ax1.set_xlim(0, 20)

    #ax4.set_yticks([0 , 0.09, 0.18])
    #ax4.set_yticklabels([r"$0$", r"$0.09$", r"$0.18$"])
   
    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(0.5)



    ax1.set_xticks([0, 5, 10, 15, 20])
    ax1.set_xticklabels([r"$0$", "$5$", "$10$", "$15$", "$20$"] ,fontsize = fontsize)
    #ax2.set_xticks([10, 100])
    #ax2.set_xticklabels([r"$10^{1}$", r"$10^{2}$"] ,fontsize = fontsize)
    

    ax1.set_yticks([])
    ax1.set_yticks([0, 0.002, 0.004, 0.006])
    ax1.set_yticklabels([r"$0$", r"$0.002$", r"$0.004$", r"$0.006$"] ,fontsize = fontsize)


    ax1.text(2.2, 0.0053, "BKT", color = "silver")
    ax1.axvline(2, 0, 1, zorder = 0, ls = "dashdot", color = "silver", linewidth = 0.85)
    #legend = ax1.legend(fontsize=6, loc='upper left', bbox_to_anchor=(0, .99), edgecolor='black', ncol=1)
    #legend.get_frame().set_alpha(0.)
    #legend.get_frame().set_boxstyle('Square', pad=0.1)
    #legend.get_frame().set_linewidth(0.0)
    axins = inset_axes(ax1, width=1, height=0.6, loc = "upper right")
    for axis in ['top', 'bottom', 'left', 'right']:
        axins.spines[axis].set_linewidth(0.5)


# Add the patch to the Axes


    plotPtGSWithCoh(axins, chi, g0, Omega)
    ax1.xaxis.tick_top()
    ax1.xaxis.set_label_position('top') 
    plt.text(0.16, 0.94, r"$\rm{a)}$", fontsize=10, transform=plt.gcf().transFigure)

    from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
    legend = ax1.legend( [plot_dmrg, plot_MF], ['DMRG', 'MF'],fontsize=6, loc='upper center', edgecolor='black', ncol=1, bbox_to_anchor=(0.4, 1.01), numpoints=1,
              handler_map={tuple: HandlerTuple(ndivide=None)})
    legend.get_frame().set_alpha(0.)
    legend.get_frame().set_boxstyle('Square', pad=0.1)
    legend.get_frame().set_linewidth(0.0)

### Plotting The photon probability distribution
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(0.5)
        
    for axis in ['top', 'right']:
        ax.spines[axis].set_linewidth(0.0)
       
    #ax1p5.set_yticks([])
    #ax1p5.set_xticks([])
    myblue5 = '#406080'
    myyellow4 = '#E6BB65'
    cmap = plt.cm.get_cmap('pink')
    frontBarColor = myblue5
    backBarColor = myyellow4
    crossColor = 'black'
    bins = np.arange(len(phot_distr_DMRG)) 
    
    print(phot_distr_DMRG.shape, phot_distr_MF.shape)
    ax.bar(bins + 0.12, np.abs(phot_distr_DMRG), log=True, fc="#525E75", width = 0.2, edgecolor ='black', linewidth = 0.25)
    ax.bar(bins - 0.12, np.abs(phot_distr_MF), log=True, fc = 'red', width = .2, edgecolor ='black', linewidth = 0.25)
    
    #ax.bar(bins, np.abs(ptGSL), log=True, fc=frontBarColor, label ="$L = 510$", width = 0.8, edgecolor ='black', linewidth = 0.25)
    #ax1.plot(bins[:42], np.abs(cohState)[:42], linestyle = '', marker = 'x', label = "Squeezed state", markersize = 3., markeredgecolor = crosscolor, markeredgewidth = .9)
    #ax.plot(bins[:26], np.abs(cohState)[:26], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 5., markeredgecolor = crossColor, markeredgewidth = 1.)
    #ax.hlines(1., -2., 30, linestyles='--', colors='gray')
    
    #axIn1.bar(bins, np.abs(ptGSL), log=False, fc=frontBarColor, label ="$L = 510$", width = 0.8, edgecolor ='black', linewidth = 0.25)
    #ax2.plot(bins[:11], np.abs(cohState)[:11], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 3., markeredgewidth = 1., clip_on = False, zorder = 100)
    #axIn1.plot(bins[:8], np.abs(cohState)[:8], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 5., markeredgewidth = 1., clip_on = False, zorder = 100)
    #ax3.hlines(1e-15, -1, 45, color = 'black', linestyle = '--', linewidth = .5)
    ax.set_ylabel(r'$P(n_{\mathrm{phot}})$', fontsize = 8)
    ax.set_xlabel(r'$n_{\mathrm{phot}}$', fontsize = 8)
    ax.set_xlim(-1, 5.5)
    #axIn1.set_xlim(-1, 43)
    ax.set_xticks([0, 1,2,3, 4,5,])
    #ax.set_xticklabels(['$0$', '$8$', '$20$', '$30$', '$40$'], fontsize = fontsize)
    ax.set_xticklabels(['0', '1','2', '3','4', '5'], fontsize = 8)
    ax.set_ylim(.5 * 1e-10, 2. * 1e0)
    ax.set_yticks([1e0, 1e-3, 1e-6, 1e-9])
    ax.set_yticklabels(['$10^{0}$', '$10^{-3}$', '$10^{-6}$', '$10^{-9}$'], fontsize = 8)
    ax.text(2, 0.001,r"$U\left[t_{\rm h}\right] = 3t_{\rm h}$", fontsize = 8)
    ax.tick_params(bottom = False)





    plt.savefig(os.path.join("plots" ,"fig3a.png"))

    
L = 110
g0 = 0.3
Omega = 1
chi = 1000
plot_occ(L ,g0, Omega, chi )