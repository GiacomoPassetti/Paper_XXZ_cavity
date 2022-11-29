import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib import patches
fontsize = 10

def plotPtGSWithCoh(ax, chi, g0, Omega):
    #cohState = coherentState.getCoherentStateForN(N)
    #cohState = coherentState.getSqueezedState(eta, T) + 1e-32

    colors = plt.cm.bone(np.linspace(0, 1, 7))

    Ussr1 = np.array([0.0, 0.25, 0.5, 0.75, 1, 1.25])
    Ussr2 = np.arange(1.5, 4.1, 0.1)
    Ussr= np.append(Ussr1, Ussr2)
    Ussr = np.append(Ussr, np.logspace(np.log10(4), 2, 20))
    Nmax = 16
    dat = np.load(os.path.join("Merged_phot", "Merged_phot0.20chi_1500.00L_50.00cut_25.npy"))

    Ls = [22, 50, 110]
    for i in range(len(Ls)):
       final_ID = "L_"+"{:.2f}".format(Ls[i])+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
       dat = np.load(os.path.join("../XXZ/photon_occupation", "photon_occupation_jointed"+final_ID+".npy"))
       ax.plot(Ussr, dat, color = colors[-3-i],label=r"$L=$"+str(Ls[i]), lw = 1)
    L = 210
    new_U = np.arange(0, 4.2, 0.2)
    final_ID = "new_U_L_"+"{:.2f}".format(L)+"chi_"+str(chi)+"g_"+"{:.2f}".format(g0)+"omega_"+"{:.3f}".format(Omega)
    dat = np.load(os.path.join("../XXZ/photon_occupation", "photon_occupation_jointed"+final_ID+".npy"))
    ax.plot(new_U, dat, color = colors[1],label=r"$L=$"+str(L), lw = 1)

    #ax.vlines(2.5, 0, 0.0025, colors='red', ls='--', linewidth = 0.5)




    #ax1p5.set_yticks([])
    #ax1p5.set_xticks([])

    myblue5 = '#406080'

    myyellow4 = '#E6BB65'

    

    frontBarColor = myblue5
    backBarColor = myyellow4
    crossColor = 'black'


    ax.set_yticks([])
    ax.set_xticks([])

    ax.set_ylabel(r'$N_{\rm phot}$', fontsize = 8)
    ax.set_xlabel(r'$U\left[t_{\rm h}\right]$', fontsize = 8)
    legend = ax.legend(fontsize=4, loc='upper left', edgecolor='black', ncol=1)
    legend.get_frame().set_alpha(0.)
    legend.get_frame().set_boxstyle('Square', pad=0.1)
    legend.get_frame().set_linewidth(0.0)
    ax.set_xlim(0, 4)

