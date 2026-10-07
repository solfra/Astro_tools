from astropy.io import fits
import numpy as np
from tqdm import tqdm

def substract_fits(old_fits,new_fits,output_path):
    with fits.open(new_fits) as hdul_new, fits.open(old_fits) as hdul_old:
        output_hdul = fits.HDUList() # save diff
    
        for idx, hdu in enumerate(tqdm(hdul_new)):
            if hdu.data is None:
                new_hdu = fits.PrimaryHDU(header=hdu.header.copy())
                output_hdul.append(new_hdu)
                continue
    
            new = hdul_new[idx].data.astype(np.float32)
            old = hdul_old[idx].data.astype(np.float32)
            diff_data = new - old
    
            new_header = hdu.header.copy()
            if idx == 0:
                new_hdu = fits.PrimaryHDU(data=diff_data, header=new_header)
            else:
                new_hdu = fits.ImageHDU(data=diff_data, header=new_header)
    
            output_hdul.append(new_hdu)
    
        output_hdul.writeto(output_path, overwrite=True)

def divied_fits(old_fits,new_fits,output_path):
    with fits.open(new_fits) as hdul_new, fits.open(old_fits) as hdul_old:
        output_hdul = fits.HDUList() # save diff
    
        for idx, hdu in enumerate(tqdm(hdul_new)):
            if hdu.data is None:
                new_hdu = fits.PrimaryHDU(header=hdu.header.copy())
                output_hdul.append(new_hdu)
                continue
    
            new = hdul_new[idx].data.astype(np.float32)
            old = hdul_old[idx].data.astype(np.float32)
            diff_data = new / old
    
            new_header = hdu.header.copy()
            if idx == 0:
                new_hdu = fits.PrimaryHDU(data=diff_data, header=new_header)
            else:
                new_hdu = fits.ImageHDU(data=diff_data, header=new_header)
    
            output_hdul.append(new_hdu)
    
        output_hdul.writeto(output_path, overwrite=True)