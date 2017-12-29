import sys
import numpy as np
from scipy import fftpack
import cProfile, pstats

n = 4800
m = 22000

s = np.random.random((n, m))
X = np.zeros((m, n))

pr = cProfile.Profile()
pr.enable()

for itr in xrange(0, n):
  X[:,itr] = s[itr]
  FFTX = fftpack.fft(X[:,itr])
  IFFTX = np.real(fftpack.ifft(FFTX))
  
pr.disable()
sortby = 'time'
ps = pstats.Stats(pr, stream=sys.stdout).sort_stats(sortby)
ps.print_stats()


