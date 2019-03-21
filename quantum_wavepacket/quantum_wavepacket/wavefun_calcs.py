import logging
import quantum_wavepacket
import numpy


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


def integrate(psi, dx):
    """integrate the wavefunction psi assuming a spacing of dx

        params
            psi - 1D numpy array representing the numerical values of the wavefunction as a function of some axis
            dx - spacing between entries in psi
    """
    
    integral = numpy.vdot(psi, psi.T) * dx

    return integral

def calc_prob_dens(psi):
    return numpy.conj(psi) * psi
    