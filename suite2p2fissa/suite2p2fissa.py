# -*- coding: utf-8 -*-
"""
Created on Sat Oct 23 14:57:05 2021

@author: valer
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

    
# FISSA toolbox
import fissa
import os
# suite2p toolbox
# import suite2p

# For plotting our results, use numpy and matplotlib
# import matplotlib.pyplot as plt
import numpy as np
import scipy.io
# Plotting toolbox, with notebook embedding options

if __name__ == '__main__':

    # Extract the motion corrected tiffs (make sure that the reg_tif option is set to true, see above)
    cases = ['rbp6_3']
    pt = 'Z:\\Scanbox\\Data\\'
    
    for icase in cases:
        path = pt + icase
        col = -1
        Rois1 = scipy.io.loadmat(path +'\\matchedRoi\\4FISSA\\RoiMatch4Fissa.mat')
        for filename in os.listdir(path):    
            if filename != 'matchedRoi'and filename != 'hide':
                # images0 = path + '\\' + filename + '\\suite2p\\plane0\\reg_tif'  
                images1 = path + '\\' + filename + '\\suite2p\\plane1\\reg_tif'  
                
                col = col + 1
                print(path + '\\' + filename)
                
                # stat0 = np.load(path + '\\' + filename + '\\suite2p\\plane0\\stat.npy', allow_pickle=True)  # cell stats
                # ops0 = np.load(path + '\\' + filename + '\\suite2p\\plane0\\ops.npy', allow_pickle=True).item()
                # iscell0 = np.load(path + '\\' + filename + '\\suite2p\\plane0\\iscell.npy', allow_pickle=True)[:, 0]
                
                stat1 = np.load(path + '\\' + filename + '\\suite2p\\plane1\\stat.npy', allow_pickle=True)  # cell stats
                ops1 = np.load(path + '\\' + filename + '\\suite2p\\plane1\\ops.npy', allow_pickle=True).item()
                
                ix1 = Rois1['RoiMatch4Fissa'][:, col] - 1
                iscell1 = np.load(path + '\\' + filename + '\\suite2p\\plane1\\iscell.npy', allow_pickle=True)[:, 0]
                iscell1 = [not elem for elem in iscell1]
                for k in ix1: iscell1[k] = True
                    
                
                # Lx0 = ops0["Lx"]
                # Ly0 = ops0["Ly"]
                Lx1 = ops1["Lx"]
                Ly1 = ops1["Ly"]
                                
                # ncells0 = len(stat0)
                # cell_ids0 = np.arange(ncells0)  # assign each cell an ID, starting from 0.
                # # cell_ids = cell_ids[iscell == 1 or iscell == 0]  # only take the ROIs that are actually cells.
                # num_rois0 = len(cell_ids0)
                # # Generate ROI masks in a format usable by FISSA (in this case, a list of masks)
                # rois0 = [np.zeros((Ly0, Lx0), dtype=bool) for n in range(num_rois0)]
                
                ncells1 = len(stat1)
                cell_ids1 = np.arange(ncells1)  # assign each cell an ID, starting from 0.
                # cell_ids = cell_ids[iscell == 1 or iscell == 0]  # only take the ROIs that are actually cells.
                num_rois1 = len(cell_ids1)
                # Generate ROI masks in a format usable by FISSA (in this case, a list of masks)
                rois1 = [np.zeros((Ly1, Lx1), dtype=bool) for n in range(num_rois1)]
                        
                # for i, n in enumerate(cell_ids0):
                #     # i is the position in cell_ids, and n is the actual cell number
                #     ypix0 = stat0[n]["ypix"] #[~stat[n]["overlap"]]
                #     xpix0 = stat0[n]["xpix"] #[~stat[n]["overlap"]]
                #     rois0[i][ypix0, xpix0] = 1
            
                # output_folder0 = path + '\\' + filename + '\\suite2p\\plane0\\FISSA'
                # experiment0 = fissa.Experiment(images0, [rois0[:ncells0]], output_folder0, alpha = 0.1, lowmemory_mode=True)
                # experiment0.separate()
                # experiment0.save_to_matlab()
                
                
                for i, n in enumerate(cell_ids1):
                    # i is the position in cell_ids, and n is the actual cell number
                    ypix1 = stat1[n]["ypix"] #[~stat[n]["overlap"]]
                    xpix1 = stat1[n]["xpix"] #[~stat[n]["overlap"]]
                    rois1[i][ypix1, xpix1] = 1
            
                output_folder1 = path + '\\' + filename + '\\suite2p\\plane1\\FISSA'
                experiment1 = fissa.Experiment(images1, [rois1[:ncells1]], output_folder1, alpha = 0.1, lowmemory_mode=True)
                experiment1.separate()
                experiment1.save_to_matlab()
                
