from astropy.io import fits

def extract_ext(file,ext):
    """
    Extract extension from multi extension fits file and write it on disk (same location as original file)
    
    Input:
    * file: file name
    * ext: extension name

    Output:
    None, write fits on disk
    """
    file_out = f'{file}_{ext}.fits'
    hdu = fits.open(file)
    fits.writeto(file_out, hdu['SCI'].data, hdu['SCI'].header, overwrite=True)
    return

if __name__ == "__main__" :
    import argparse

    parser = argparse.ArgumentParser(description='Extract SCI image')
    parser.add_argument('--file', type=str, help='File name')
    parser.add_argument('--ext', type=str, help='Extension name name')
    args = parser.parse_args()

    file = args.file
    ext = args.ext

    extract_ext(file,ext)

