import logging
import unittest
import numpy
import os.path
import quantum_wavepacket
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_calc_wavefun as pbc1d_calc_wavefun
import quantum_wavepacket.periodic_boundary_condition_1D.pbc1d_params as pbc1d_params
import quantum_wavepacket.graph_psi as gp
import quantum_wavepacket.wavepacket as wavepacket


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class TestGraphPsi(unittest.TestCase):
    def test_graph(self):
        my_params = pbc1d_params.Pbc1dParams(periodic_length=100.0, num_x=100, duration=2, num_t=1)

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[1], state_coefs=[1])
        psi = pbc1d_calc_wavefun.calc_in_position_space(my_wavepacket, my_params)
        gp.graph(psi, my_params.x, "title test_graph01", "test_graph01.png")
        self.assertTrue(os.path.exists("test_graph01.png"))

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[2], state_coefs=[1])
        psi = pbc1d_calc_wavefun.calc_in_position_space(my_wavepacket, my_params)
        gp.graph(psi, my_params.x, "title test_graph02", "test_graph02.png")
        self.assertTrue(os.path.exists("test_graph02.png"))

        my_wavepacket = wavepacket.Wavepacket(state_indexes=[1,2], 
            state_coefs=numpy.ones(2)/numpy.sqrt(2))
        psi = pbc1d_calc_wavefun.calc_in_position_space(my_wavepacket, my_params)
        gp.graph(psi, my_params.x, "title test_graph03", "test_graph03.png")
        self.assertTrue(os.path.exists("test_graph03.png"))
        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, 
        format=quantum_wavepacket.LOG_FORMAT)
    unittest.main()