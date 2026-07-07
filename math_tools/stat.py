import numpy as np

def Pearson_skewness(data):
  '''
  Calculate the Karl Pearson’s measure of skewness, 
  i.e the divergence of mean from mode in a skewed distribution.

  3(mean - median) / standard deviation or (mean - mode)/standard deviation
  '''
  measure = 3*(np.mean(data) - np.median(data))/np.std(data)
  return measure
