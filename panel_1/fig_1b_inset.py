import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import gridspec
import matplotlib as mpl
from matplotlib import patches
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



fontsize = 10
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



    #cohState = coherentState.getCoherentStateForN(N)
def inset_1b(ax):
    #fig = plt.figure()
    #fig.set_size_inches(3., 2.)

    #   ax1 = plt.subplot2grid((1, 36), (0, 0), fig = fig, colspan = 15)
    #   ax2 = plt.subplot2grid((1, 36), (0, 21), fig = fig, colspan = 15)
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
    ax.bar(bins + 0.15, np.abs(phot_distr_DMRG), log=True, fc='lightcoral', width = 0.2, edgecolor ='black', linewidth = 0.25)
    ax.bar(bins - 0.15, np.abs(phot_distr_MF), log=True, fc = 'cornflowerblue', width = .2, edgecolor ='black', linewidth = 0.25)
    
    #ax.bar(bins, np.abs(ptGSL), log=True, fc=frontBarColor, label ="$L = 510$", width = 0.8, edgecolor ='black', linewidth = 0.25)
    #ax1.plot(bins[:42], np.abs(cohState)[:42], linestyle = '', marker = 'x', label = "Squeezed state", markersize = 3., markeredgecolor = crosscolor, markeredgewidth = .9)
    #ax.plot(bins[:26], np.abs(cohState)[:26], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 5., markeredgecolor = crossColor, markeredgewidth = 1.)
    #ax.hlines(1., -2., 30, linestyles='--', colors='gray')
    
    #axIn1.bar(bins, np.abs(ptGSL), log=False, fc=frontBarColor, label ="$L = 510$", width = 0.8, edgecolor ='black', linewidth = 0.25)
    #ax2.plot(bins[:11], np.abs(cohState)[:11], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 3., markeredgewidth = 1., clip_on = False, zorder = 100)
    #axIn1.plot(bins[:8], np.abs(cohState)[:8], linestyle = '', marker = 'x', color = crossColor, label = "Squeezed state", markersize = 5., markeredgewidth = 1., clip_on = False, zorder = 100)
    #ax3.hlines(1e-15, -1, 45, color = 'black', linestyle = '--', linewidth = .5)
    ax.set_ylabel(r'$P(n_{\mathrm{phot}})$', fontsize = 6)
    ax.set_xlabel(r'$n_{\mathrm{phot}}$', fontsize = 6)
    ax.set_xlim(-1, 6)
    #axIn1.set_xlim(-1, 43)
    ax.set_xticks([0, 1,2,3, 4,5, 6,])
    #ax.set_xticklabels(['$0$', '$10$', '$20$', '$30$', '$40$'], fontsize = fontsize)
    ax.set_xticklabels(['0', '1','2', '3','4', '5','6'], fontsize = 6)
    ax.set_ylim(.5 * 1e-10, 2. * 1e0)
    ax.set_yticks([1e0, 1e-3, 1e-6, 1e-9])
    ax.set_yticklabels(['$10^{0}$', '$10^{-3}$', '$10^{-6}$', '$10^{-9}$'])
    #ax.set_yticklabels(['10^0', '10^-3', '10-6', '10^-9'])
    #axis arrow
    #axis arrow
    #tickPatch = patches.Rectangle((2, 1e-2), width = 0., height = 1e-2, linewidth = 0.7, clip_on = False)
    #ax.add_patch(tickPatch)
    #plt.show()
    #plt.savefig(os.path.join('plots','Fig1cN100.png'), format='png')
    

