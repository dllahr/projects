import logging
import unittest
import quantum_wavepacket
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_params as pp


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestModuleTemplate(unittest.TestCase):
    def test__build_axis(self):
        r = pp.Pbc1dParams._build_axis(3, 0.1)
        logger.debug("r:  {}".format(r))
        self.assertAlmostEqual(0.0, r[0])
        self.assertAlmostEqual(0.1, r[1])

    def test___str__(self):
        t = pp.Pbc1dParams(1, 200, 3, 5)
        r = t.__str__()
        logger.debug("len(r):  {}".format(len(r)))
        logger.debug("r:  {}".format(r))
        self.assertGreater(200, len(r))
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
        format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()