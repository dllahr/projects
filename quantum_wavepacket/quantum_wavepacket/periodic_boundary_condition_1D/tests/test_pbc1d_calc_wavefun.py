import logging
import unittest
import quantum_wavepacket
import numpy
import quantum_wavepacket.wavepacket as wavepacket
import quantum_wavepacket.wavefun_calcs as wavefun_calcs
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_calc_wavefun as cwf
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_params as pbc1d_params


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestPbc1dCalcWavefun(unittest.TestCase):
    def test_calc_in_position_space(self):
        logger.debug("test_calc_in_position_space")

        my_params = pbc1d_params.Pbc1dParams(periodic_length=100.0, num_x=100, duration=2, num_t=1)

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[1], state_coefs=[1])
        psi = cwf.calc_in_position_space(my_wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = wavefun_calcs.integrate(psi, my_params.dx)
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[2], state_coefs=[1])
        psi = cwf.calc_in_position_space(my_wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = wavefun_calcs.integrate(psi, my_params.dx)
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[1,2], 
            state_coefs=numpy.ones(2)/numpy.sqrt(2))
        psi = cwf.calc_in_position_space(my_wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = wavefun_calcs.integrate(psi, my_params.dx)
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
        format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()