import logging
import unittest
import quantum_wavepacket
import numpy
import quantum_wavepacket.wavefun_calcs as wfc


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestWavefunCalcs(unittest.TestCase):
    def test_integrate(self):
        r = wfc.integrate(numpy.array([1.0, 1.0]), 1.0)
        logger.debug("r:  {}".format(r))
        self.assertAlmostEqual(2.0, r)

        r = wfc.integrate(numpy.array([2.0, 1.0]), 1.0)
        logger.debug("r:  {}".format(r))
        self.assertAlmostEqual(5.0, r)

        r = wfc.integrate(numpy.array([0.5, 0.3]), 1.0)
        logger.debug("r:  {}".format(r))
        self.assertAlmostEqual(.34, r)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()
