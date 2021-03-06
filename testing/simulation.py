# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 20:42:29 2020

@author: Jacob
"""

from tweezerlyze.simulation.experiment import Experiment
from options import experiment_options
import numpy as np
import matplotlib.pyplot as plt

# change readout rate
rr = 30e6
experiment_options['imaging_options']['camera_options']['readout_rate'] = rr

# generate reference image
experiment_options['tweezer_options']['n_sites'] = (1,1)
experiment_options['tweezer_options']['avg_filling'] = 1
experiment_options['tweezer_options']['filling_distribution'] = 'poisson'
# experiment_options['tweezer_options']['filling_distribution_kwargs'] = {'scale': 1}

expt_reference = Experiment(**experiment_options)
expt_reference.load_atoms()
expt_reference.image_atoms(imaging_time=10000)

roi = {
    'xmin': 0,
    'xmax': 125,
    'ymin': 0,
    'ymax': 125,
    }
    
expt_reference.show_atoms(roi=roi)
reference_image = expt_reference.imaging.camera.image_cropped

np.save('atoms_reference.npy', reference_image)

# generate sparsely filled image
nx = 10
ny = 10
experiment_options['tweezer_options']['n_sites'] = (nx, ny)
x, y = np.meshgrid(np.arange(nx), np.arange(ny))
x = x/(nx-1)
y = y/(ny-1)

experiment_options['tweezer_options']['avg_filling'] = x**2+y**2

expt_sparse = Experiment(**experiment_options)
expt_sparse.load_atoms()

# times = 2**np.arange(0, 11)
times = [100000]

for t in times:
    expt_sparse.image_atoms(imaging_time=t)
    expt_sparse.show_atoms(roi=roi, colorbar=True, title=f'Readoute rate = {rr/1e6} MHz')

image = expt_sparse.imaging.camera.image_cropped

plt.savefig('simulation.jpg', bbox_inches='tight', dpi=300)

np.save('atoms_sparse.npy', image)