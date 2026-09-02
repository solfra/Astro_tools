import numpy as np

def Pearson_skewness(data):
  '''
  Calculate the Karl Pearson’s measure of skewness, 
  i.e the divergence of mean from mode in a skewed distribution.

  3(mean - median) / standard deviation or (mean - mode)/standard deviation
  '''
  measure = 3*(np.mean(data) - np.median(data))/np.std(data)
  return measure

def median_by_bins_2d(x,y,bins=10):
  '''
  Caluclate a median for y per x bins.
  '''

  hist_x = np.histogram(x,bins=bins)
  hist_x_value = hist_x[1]

  res = {'x_bin':[],'y_med':[]}

  for i in range(len(hist_x_value)-1):
    min_lim = hist_x_value[i]
    max_lim = hist_x_value[i+1]

    med = np.median(y[np.where((min_lim<=x) & (x<max_lim))])

    res['x_bin'].append(np.mean([min_lim,max_lim]))
    res['y_med'].append(med)

  return res