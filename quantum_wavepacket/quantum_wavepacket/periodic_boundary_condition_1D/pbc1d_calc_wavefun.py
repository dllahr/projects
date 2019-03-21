"""
spatial basis wavefunction is exp(ikx)*sqrt(1/L)
    k = 2*pi*n/L
    n is integer positive or negative
    https://en.wikipedia.org/wiki/Particle_in_a_one-dimensional_lattice
"""
import numpy


def calc_in_position_space(my_wavepacket, my_pbc1d_params):
    """params:
        wavepacket - objecct describing the state indexes and coefficients of the wavepacket
        my_pbc1d_params - pbc1d_params object
    """
    x = my_pbc1d_params.x
    periodic_L = my_pbc1d_params.periodic_length

    psi = numpy.zeros(x.shape)

    wavenumbers = calc_wavenumbers(my_wavepacket, periodic_L)

    for wavenum_k, state_coef in zip(wavenumbers, my_wavepacket.state_coefs):
        #calculate base function
        phi = numpy.exp(1j * wavenum_k * (x - periodic_L/2.0)) * numpy.sqrt(1.0 / periodic_L)

        psi = psi + state_coef * phi

    return psi


def calc_wavenumbers(my_wavepacket, periodic_L):
    k = 2.0 * numpy.pi * my_wavepacket.state_indexes / periodic_L

    return k


def calc_state_energies(my_wavepacket, periodic_L):
    k = calc_wavenumbers(my_wavepacket, periodic_L)

    energies = numpy.power(k, 2.0) / 2.0

    return energies


def calc_time_dependent_state_coef(my_wavepacket, periodic_L, t):
    state_energies = calc_state_energies(my_wavepacket, periodic_L)
    
    psi_t = numpy.exp(-1j * state_energies * t)

    return psi_t
