from astropy.io import fits
import matplotlib.pyplot as plt

def fits_preview(file_name,ext=1,normlise=True):
    data = fits.open(file_name)
    
def extract_header(file_name,ext=1,verbose=False):
    """
    Open a fits file and extract the header of a given extension

    Input:
    - file_name (str): file name to read
    - ext (int or str): Name or number of the extension. Default is 1.
    - verbose (bool): If true print the header. Default is False.

    Output:
    -header (dict): The header pf the extension.  
    """
    header = fits.open(file_name)[ext].header
    if verbose:
        print(header)
    return header
