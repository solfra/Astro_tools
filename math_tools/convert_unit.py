import numpy as np

def adu_to_mag(adu,zp,exptime):
    """
    Converting ADU into magnitude

    Input:
    - adu: value to convert
    - zp: zero point
    - exptime: exposure time duration

    Output:
    - magnitude
    """
    return -2.5*np.log10(adu) + 2.5*np.log10(exptime) + zp

def mag_to_adu(mag, zp, exptime):
    """
    Converting magnitude into ADU

    Input:
    - mag: magnitude to convert
    - zp: zero point
    - exptime: exposure time duration

    Output:
    - adu
    """
    return 10 ** ((zp - mag) / 2.5) * exptime