import numpy as np

def Pearson_skewness(data):
  '''
  Calculate the Karl Pearson’s measure of skewness, 
  i.e the divergence of mean from mode in a skewed distribution.

  3(mean - median) / standard deviation or (mean - mode)/standard deviation
  '''
  measure = 3*(np.mean(data) - np.median(data))/np.std(data)
  return measure

def median_by_bins(x,y,bins=10):
  '''
  Caluclate a median for y per x bins.
  '''

  _,hist_x_value = np.histogram(x,bins=bins)

  res = {'x_bin':[],
         'y_med':[],
         'y_mean':[],
         'y_std':[],
         'y_error_on_mean':[],
         'n_value':[]}

  max_iter = len(hist_x_value)-1

  for i in range(max_iter):
    min_lim = hist_x_value[i]
    max_lim = hist_x_value[i+1] 

    #increase max lim at last iter to include the max value
    if i == max_iter - 1:
      mask = (min_lim <= x) & (x <= max_lim)
    else:
      mask = (min_lim <= x) & (x < max_lim)

    y_bin = y[mask]
    n_val = y_bin.shape[0]

    if n_val >0:
      med = np.median(y_bin)
      mean = np.mean(y_bin)
      std = np.std(y_bin)
      error_mean = std/np.sqrt(n_val)

    else:
      med=np.nan
      mean=np.nan
      std = np.nan
      error_mean=np.nan

    res['x_bin'].append(np.mean([min_lim,max_lim]))
    res['y_med'].append(med)
    res['y_mean'].append(mean)
    res['y_std'].append(std)
    res['y_error_on_mean'].append(error_mean)
    res['n_value'].append(n_val)

  return res