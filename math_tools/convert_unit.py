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