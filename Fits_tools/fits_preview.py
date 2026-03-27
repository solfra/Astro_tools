from astropy.io import fits
import matplotlib.pyplot as plt

def fits_preview(file_name,ext=1,normlise=True,show=False,save_name=None):
    """
    Open a fits file and show and/or save a preview

    Input:
    - file_name (str): file name to read
    - ext (int or str): Name or number of the extension. Default is 1.
    - show (bool): If True show the image
    - save_name (str): If not None, name of the file for save the image. If None (default), the image is not saved.

    Output:
    - None
    """
    data = fits.open(file_name)[ext].data
    plt.figure(figsize=(15,15))
    plt.imshow(data,origin='lower')
    if show:
        plt.show()
    if save_name is not None:
        plt.savefig(save_name)
    plt.close()
    return None
    
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

if __name__ == "__main__" :
    import argparse

    parser = argparse.ArgumentParser(description='Extract SCI image')
    parser.add_argument('--file', type=str, help='File name')
    parser.add_argument('--ext', type=str, help='Extension name name')
    args = parser.parse_args()
    
    file = args.file
    ext = args.ext

    extract_header(file,ext=ext)
    fits_preview(file,ext=ext)