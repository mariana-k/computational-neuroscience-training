"""
Created on Wed Apr 22 15:15:16 2015

@author: rkp

Quiz 2 code.
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

import pickle

from compute_sta import compute_sta


FILENAME = 'c1p8.pickle'

with open(FILENAME, 'rb') as f:
    data = pickle.load(f)
    
stim = data['stim']
rho = data['rho']

nonzerorho = len(np.nonzero(rho[151:])[0])
num_spikes = np.average(nonzerorho)

# Fill in these values
sampling_period = 2 # in ms
num_timesteps = int(300/sampling_period)

sta = compute_sta(stim, rho, num_timesteps)

time = (np.arange(-num_timesteps, 0) + 1) * sampling_period

plt.plot(time, sta)
plt.xlabel('Time (ms)')
plt.ylabel('Stimulus')
plt.title('Spike-Triggered Average')

plt.show()

