import collections
import numpy
import quantum_wavepacket.wavefun_calcs as wavefun_calcs


class Wavepacket(object):
    def __init__(self, state_indexes=None, state_coefs=None):
        self.state_indexes = numpy.array(state_indexes)
        self.state_coefs = numpy.array(state_coefs)

    def __str__(self):
        return """Wavepacket state_indexes.shape:  {} state_indexes[:3]:  {}  
            state_coefs.shape:  {}  state_coefs[:3]:  {}""".format(self.state_indexes.shape, self.state_indexes[:3],
            self.state_coefs.shape, self.state_coefs[:3])

    def calc_norm_coef(self):
        """Calculate the normalization coefficient for a set of coefficients of the states of the wavepack
            params
                state_coefs - numpy array of floats that represent coefficients of each state
        """
        norm = numpy.sqrt(wavefun_calcs.integrate(self.state_coefs, 1.0))

        return norm
    
    def normalize_state_coefs(self):
        norm = self.calc_norm_coef()
        self.state_coefs = self.state_coefs / norm
