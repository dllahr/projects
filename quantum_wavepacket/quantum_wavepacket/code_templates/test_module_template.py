import logging
import unittest
import quantum_wavepacket


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestModuleTemplate(unittest.TestCase):
    def test_example_01(self):
        logger.debug("Hello world!")


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
        format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()