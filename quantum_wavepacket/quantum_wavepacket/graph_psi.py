import logging
import quantum_wavepacket
import numpy
import matplotlib.pyplot as pyplot
import seaborn as sns
sns.set(color_codes=True)


logger = logging.getLogger(quantum_wavepacket.LOGGER_NAME)


def graph(psi, x, fig_title, filename=None):
    fig = pyplot.figure(fig_title)

    pyplot.plot(x, numpy.real(psi))
    pyplot.plot(x, numpy.imag(psi))
    pyplot.xlabel("x")
    pyplot.ylabel("probability amplitude")
    pyplot.title(fig_title)
    if filename is not None:
        logger.debug("writing graph to image filename:  {}".format(filename))
        pyplot.savefig(filename)

    return fig
