import quantum_wavepacket
import logging
import numpy


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


class Pbc1dParams(object):
    def __init__(self, periodic_length=None, num_x=None, duration=None, num_t=None):
        self.periodic_length = float(periodic_length)
        self.num_x = int(num_x)
        self.dx = self.periodic_length / float(self.num_x)
        self.x = Pbc1dParams._build_axis(self.num_x, self.dx)

        self.duration = float(duration)
        self.num_t = int(num_t)
        self.dt = self.duration / float(self.num_t)
        self.t = Pbc1dParams._build_axis(self.num_t, self.dt)
        

    @staticmethod
    def _build_axis(num_x, dx):
        return numpy.array(range(num_x)) * dx
