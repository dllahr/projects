import logging
import unittest
import quantum_wavepacket
import numpy
import quantum_wavepacket.wavepacket as wp


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestWavepacket(unittest.TestCase):
    def test_calc_norm_coef(self):
        my_wp = wp.Wavepacket(state_coefs=numpy.array([1.0, 2.0]))
        r = wp.Wavepacket.calc_norm_coef(my_wp)
        logger.debug("r:  {}".format(r))
        expected = numpy.sqrt(5.0)
        self.assertAlmostEqual(expected, r)

    def test_normalize_state_coefs(self):
        init_state_coefs = numpy.array([1.0, 2.0])
        my_wp = wp.Wavepacket(state_coefs=init_state_coefs)
        my_wp.normalize_state_coefs()
        logger.debug("my_wp.state_coefs:  {}".format(my_wp.state_coefs))
        expected = init_state_coefs / numpy.sqrt(5.0)
        self.assertTrue(numpy.allclose(expected, my_wp.state_coefs))

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()