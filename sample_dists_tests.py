import sample_dists
import numpy as np
import matplotlib.pyplot as plt


e, pe = sample_dists.pe_cfhtlens()

esamps = sample_dists.sample_dists(numsamp=1000000)

n, bins, _ = plt.hist(esamps, bins=100, density=True)
pe, _ = np.histogram(e, weights=pe, density=True, bins=bins)

x = 0.5*(bins[:-1] + bins[1:])
plt.plot(x, pe)

plt.show()



