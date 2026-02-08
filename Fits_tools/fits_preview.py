from astropy.io import fits
import matplotlib.pyplot as plt

def fits_preview(file_name,ext=1,normlise=True):
    data = fits.open(file_name)
    
def extract_header(file_name):
    data = fits.open(file_name)