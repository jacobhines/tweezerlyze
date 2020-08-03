# -*- coding: utf-8 -*-
"""
Created on Mon May 25 17:34:34 2020

@author: Jacob
"""

import numpy as np
import scipy.constants as cnst

class Laser():
    def __init__(self, wavelength, power, waist):
        """
        Parameters
        ----------
        wavelength : float
            wavelength in m.
        power : float
            power in W.
        waist : TYPE
            beam waist in m.
        """
        
        self.wavelength = wavelength
        self.power = power
        self.waist = waist
        self.intensity = 2*power/(np.pi*waist**2) #W/m2
        self.frequency = cnst.c / (self.wavelength*1e-9) #Hz