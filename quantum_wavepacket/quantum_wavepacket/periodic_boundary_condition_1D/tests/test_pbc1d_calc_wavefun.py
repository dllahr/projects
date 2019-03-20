import logging
import unittest
import quantum_wavepacket
import numpy
import quantum_wavepacket.wavepacket as wp
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_calc_wavefun as cwf
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_params as pbc1d_params


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestPbc1dCalcWavefun(unittest.TestCase):
    def test_calc_in_position_space(self):
        logger.debug("test_calc_in_position_space")

        my_params = pbc1d_params.Pbc1dParams(periodic_length=100.0, num_x=100, duration=2, num_t=1)

        wavepacket = [wp.wavepacket_state_entry(1, 1)]
        psi = cwf.calc_in_position_space(wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = numpy.vdot(psi, psi.T) * my_params.dx
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)

        wavepacket = [wp.wavepacket_state_entry(2, 1)]
        psi = cwf.calc_in_position_space(wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = numpy.vdot(psi, psi.T) * my_params.dx
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)

        wavepacket = [wp.wavepacket_state_entry(1, 1.0/numpy.sqrt(2)),
                    wp.wavepacket_state_entry(2, 1.0/numpy.sqrt(2))]
        psi = cwf.calc_in_position_space(wavepacket, my_params)
        logger.debug("psi[:10]:\n{}".format(psi[:10]))
        test_integral = numpy.vdot(psi, psi.T) * my_params.dx
        logger.debug("test_integral:  {}".format(test_integral))
        self.assertAlmostEqual(1.0, test_integral)


        # psi = calculate_wavefunction(numpy.array([2]), numpy.array([1]), L, x)
        # all_psi.append(psi)
        # print "psi[:10]:\n{}".format(psi[:10])
        # test_integral = numpy.vdot(psi, psi.T) * dx
        # print "test_integral:  {}".format(test_integral)
        # pyplot.figure(102)
        # pyplot.plot(x, numpy.real(psi))
        # pyplot.plot(x, numpy.imag(psi))
        # pyplot.title("test_calculate_wavefunction02")
        # pyplot.savefig("test_calculate_wavefunction02.png")

        # psi = calculate_wavefunction(numpy.array([1, 2]), numpy.array([0.70710678, 0.70710678]), L, x)
        # all_psi.append(psi)
        # print "psi[:10]:\n{}".format(psi[:10])
        # test_integral = numpy.vdot(psi, psi.T) * dx
        # print "test_integral:  {}".format(test_integral)
        # pyplot.figure(103)
        # pyplot.plot(x, numpy.real(psi))
        # pyplot.plot(x, numpy.imag(psi))
        # pyplot.title("test_calculate_wavefunction03")
        # pyplot.savefig("test_calculate_wavefunction03.png")

        # pyplot.figure(104)
        # for psi in all_psi:
        #     pyplot.plot(x, numpy.real(psi))
        # pyplot.title("test_calculate_wavefunction04")
        # pyplot.savefig("test_calculate_wavefunction04.png")
        # pyplot.figure(105)
        # for psi in all_psi:
        #     pyplot.plot(x, numpy.imag(psi))
        # pyplot.title("test_calculate_wavefunction05")
        # pyplot.savefig("test_calculate_wavefunction05.png")



if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
        format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()