import numpy as np
import aff
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import sys, os
import math, cmath
from numpy import linalg as LA
import stat_analysis as stat

def plot_ch_val(ME_list, ME_var_list, phys_ch, chi, real, other_data=None):
    label_list, tick_no_list = [] ,[]
    plot_series = len(other_data)+1
    plt.clf()
    if chi == 'LL':
        chi_list = ['LL','RR']
    elif chi == 'RL':
        chi_list = ['RL','LR']
    elif chi == 'LR':
        chi_list = ['RL','LR']
    elif chi == 'RR':
        chi_list = ['LL','RR']
    ch1 = phys_ch + '_' + chi_list[0]
    ch2 = phys_ch + '_' + chi_list[1]


    def plot_iter(ME_list, ME_var_list, color=0, pos=0., msg, patch_list):
        patchL = mpatches.Patch(color='C'+str(color%10), label=chi_list[0]+msg)
        patchR = mpatches.Patch(color='C'+str((color+1)%10), label=chi_list[0]+msg)
        patch_list.append(patchL)
        patch_list.append(patchR)
        for i, proj in enumerate(proj_list):
            plot_label = r'$\Gamma$('+ str(i) +')'
            for j, tsep in enumerate(['tsep8','tsep9','tsep10']):
                plt.errorbar(ME_list[proj][ch1][tsep], [(j+1)%3 + 3.*(i%len(proj_list))+pos ], 
                            xerr=np.sqrt(ME_var_list[proj][ch2][tsep]), color='C'+str(color%10),
                                 capsize=2, linestyle="None",markersize=2)
                plt.errorbar(ME_list[proj][ch2][tsep], [(j+1)%3 + 3.*(i%len(proj_list))-pos ], 
                            xerr=np.sqrt(ME_var_list[proj][ch2][tsep]), color='C'+str((color+1)%10),
                                capsize=2, linestyle="None",markersize=2)
                if (j+1)%3 == 1 and color == 0 and pos == 0.:
                    label_list.append(plot_label)
                    tick_no_list.append((j+1)%3 + 3.*(i%len(proj_list)))
        return patch_list
    patch_list = []
    patch_list = plot_iter(ME_list, ME_var_list, msg = '(80cfg/bin1)')
    for i in range(len(other_data)):
        patch_list = plot_iter(other_data[i]['ME_list'], other_data[i]['ME_var_list'], color= 2*i, pos=i*0.05, msg = other_data['msg'], patch_list)
    plt.axvline(0, ls='--')
    plt.yticks(tick_no_list, label_list)
    plt.title(phys_ch+'('+ chi_list[0] + '/'+ chi_list[1] +')' + real )
    plt.legend(handles=patch_list)

    plt.savefig(phys_ch+ '_allproj_'+ chi + '_'+ real +'bin_2.pdf')
    
def plot_all(ME_list, ME_var_list, real, other_data=None)
    ch_list = ['S1','S2','S3','S4','U1']
    chi_list = ['LL','LR']
    for chnl in ch_list:
        for chiral in chi_list:
            plot_ch_val(ME_list, ME_var_list, chnl, chiral, real, other_data)


