import numpy as np


def pe_cfhtlens(params={}, numinc=10000):

    default_params = {'emax':0.804,
                    'a':0.2539,
                    'e0':0.0256}

    for i in params.keys():
        if i not in default_params.keys():
            print('%s is not a parameter for CFHTLenS p(e)' %i)
        else:
            default_params[i] = params[i]

    e = np.linspace(0, default_params['emax'], num=numinc)
    pe = (e*(1.0 - np.exp((e - default_params['emax'])/default_params['a']))/
          ((1.0 + e) * np.sqrt(e**2.0 + default_params['e0']**2.0)))
    
    return e, pe / np.trapz(pe, e)


def sample_dists(dist='cfhtlens', params={}, numsamp=1, numinc=10000):

    if dist=='cfhtlens':
        e, pe = pe_cfhtlens(params, numinc)
    else:
        print('%s is not a recognised distribution' %dist)

    F = [np.trapz(pe[:i+1], e[:i+1]) for i in range(len(pe))]
    
    u_samples = np.random.uniform(0, 1, size=numsamp)
    e_samples = np.interp(u_samples, F, e)

    return e_samples
