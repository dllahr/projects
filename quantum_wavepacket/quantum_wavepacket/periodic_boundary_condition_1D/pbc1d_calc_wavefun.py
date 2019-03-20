"""
spatial basis wavefunction is exp(ikx)*sqrt(1/L)
    k = 2*pi*n/L
    n is integer positive or negative
    https://en.wikipedia.org/wiki/Particle_in_a_one-dimensional_lattice
"""
import collections
import numpy


wavepacket_state_entry = collections.namedtuple("wavepacket_entry", ["state_index", "state_coef"])


def calc_in_position_space(wavepacket_states, my_pbc1d_params):
    """params:
        wavepacket_states - collection of wavepacket_state_entry's
        my_pbc1d_params - pbc1d_params object
    """
    x = my_pbc1d_params.x
    periodic_L = my_pbc1d_params.periodic_length

    psi = numpy.zeros(x.shape)

    for state_entry in wavepacket_states:
        #calculate wavevector
        k = 2.0 * numpy.pi * float(state_entry.state_index) / periodic_L

        #calculate base function
        phi = numpy.exp(1j * k * (x - periodic_L/2.0)) * numpy.sqrt(1.0 / periodic_L)

        psi = psi + state_entry.state_coef * phi

    return psi