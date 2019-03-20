import numpy
import matplotlib.pyplot as pyplot
import os
import shutil

animation_dir = "animation"

"""notes on things tried
* increased L to 200.0, Nx to 2000 - movement of wavepacket was slower
* increased L to 1000.0, Nx to 10000 - movement of wavepacket stopped
"""

#periodic unit size
L = 100.0
print "L:  {}".format(L)

Nx = 1000
print "Nx:  {}".format(Nx)
dx = L / float(Nx)
print "dx:  {}".format(dx)
x = numpy.array(range(Nx)) * dx
print "x[:10]:\n{}".format(x[:10])

duration = 1599*2
Nt = duration/2
dt = duration / float(Nt)
t = numpy.array(range(Nt)) * dt

#spatial wavefunction is exp(ikx)*sqrt(1/L)
#k = 2*pi*n/L
#n is integer positive or negative
#https://en.wikipedia.org/wiki/Particle_in_a_one-dimensional_lattice

#energy E = hbar^2 * k^2 / (2m)
#https://en.wikipedia.org/wiki/Particle_in_a_box
#in atomic units:  E = k^2 / 2
#(use mass of an electron)
#https://en.wikipedia.org/wiki/Atomic_units

#time wavefunction is exp(-iEt/hbar)
#atomic units:  exp(-iEt)
#http://hyperphysics.phy-astr.gsu.edu/hbase/quantum/Scheq.html

def calculate_wavefunction(state_indexes, state_coefs, periodic_length, x):
    psi = numpy.zeros(x.shape)
    for (i, si) in enumerate(state_indexes):
        k = 2 * numpy.pi * float(si) / periodic_length
        phi = numpy.exp(1j*k*(x - periodic_length/2.0)) * numpy.sqrt(1.0 / periodic_length)

        sc = state_coefs[i]
        psi = psi + sc*phi

    return psi

def test_calculate_wavefunction():
    print "test_calculate_wavefunction"

    all_psi = []

    psi = calculate_wavefunction(numpy.array([1]), numpy.array([1]), L, x)
    all_psi.append(psi)
    print "psi[:10]:\n{}".format(psi[:10])
    test_integral = numpy.vdot(psi, psi.T) * dx
    print "test_integral:  {}".format(test_integral)
    pyplot.figure(101)
    pyplot.plot(x, numpy.real(psi))
    pyplot.plot(x, numpy.imag(psi))
    pyplot.title("test_calculate_wavefunction01")
    pyplot.savefig("test_calculate_wavefunction01.png")

    psi = calculate_wavefunction(numpy.array([2]), numpy.array([1]), L, x)
    all_psi.append(psi)
    print "psi[:10]:\n{}".format(psi[:10])
    test_integral = numpy.vdot(psi, psi.T) * dx
    print "test_integral:  {}".format(test_integral)
    pyplot.figure(102)
    pyplot.plot(x, numpy.real(psi))
    pyplot.plot(x, numpy.imag(psi))
    pyplot.title("test_calculate_wavefunction02")
    pyplot.savefig("test_calculate_wavefunction02.png")

    psi = calculate_wavefunction(numpy.array([1, 2]), numpy.array([0.70710678, 0.70710678]), L, x)
    all_psi.append(psi)
    print "psi[:10]:\n{}".format(psi[:10])
    test_integral = numpy.vdot(psi, psi.T) * dx
    print "test_integral:  {}".format(test_integral)
    pyplot.figure(103)
    pyplot.plot(x, numpy.real(psi))
    pyplot.plot(x, numpy.imag(psi))
    pyplot.title("test_calculate_wavefunction03")
    pyplot.savefig("test_calculate_wavefunction03.png")

    pyplot.figure(104)
    for psi in all_psi:
        pyplot.plot(x, numpy.real(psi))
    pyplot.title("test_calculate_wavefunction04")
    pyplot.savefig("test_calculate_wavefunction04.png")
    pyplot.figure(105)
    for psi in all_psi:
        pyplot.plot(x, numpy.imag(psi))
    pyplot.title("test_calculate_wavefunction05")
    pyplot.savefig("test_calculate_wavefunction05.png")

state_indexes = numpy.array(range(1,21))

state_coefs = numpy.exp(-numpy.power(state_indexes - 10, 2) / 2.0)
norm = numpy.sqrt(numpy.sum(numpy.power(state_coefs, 2)))
print "normalization for state_coefs - norm:  {}".format(norm)
state_coefs = state_coefs / norm
print "check normalization of state_coefs:  {}".format(numpy.sum(numpy.power(state_coefs, 2)))
print "state_coefs:\n{}".format(state_coefs)

initial_psi = calculate_wavefunction(state_indexes, state_coefs, L, x)
initial_prob_dens = numpy.conj(initial_psi) * initial_psi

state_wavenumbers = 2.0 * numpy.pi * state_indexes / L
state_energies = numpy.power(state_wavenumbers, 2.0) / 2.0

time_psi = []
time_prob_dens = []
for cur_t in t[:]:
    time_modifiers = numpy.exp(-1j * state_energies * cur_t)
    # print "time_modifiers:\n{}".format(time_modifiers)
    # print numpy.vdot(time_modifiers, time_modifiers.T)

    cur_state_coefs = state_coefs * time_modifiers

    psi = calculate_wavefunction(state_indexes, cur_state_coefs, L, x)
    time_psi.append(psi)

    prob_dens = numpy.conj(psi) * psi
    # print "cur_t:  {}  prob_dens normalization check:  {}".format(cur_t, numpy.sum(prob_dens) * dx)
    time_prob_dens.append(prob_dens)


fig_ind=1
pyplot.figure(fig_ind)
pyplot.plot(state_indexes, state_coefs, marker=".")
pyplot.xlabel("state_indexes")
pyplot.ylabel("state_coefs")
pyplot.savefig("state_coefs.png")

if False:
    test_calculate_wavefunction()

fig_ind = fig_ind+1
pyplot.figure(fig_ind)
pyplot.plot(x, numpy.real(initial_psi))
pyplot.plot(x, numpy.imag(initial_psi))
pyplot.xlabel("x")
pyplot.ylabel("initial_psi")
pyplot.savefig("initial_psi.png")
fig_ind = fig_ind+1
pyplot.figure(fig_ind)
pyplot.plot(x, numpy.real(initial_prob_dens))
pyplot.plot(x, numpy.imag(initial_prob_dens))
pyplot.xlabel("x")
pyplot.ylabel("initial_prob_dens")
pyplot.savefig("initial_prob_dens.png")

if os.path.exists("animation"):
    shutil.rmtree("animation")
os.mkdir("animation")

initial_file_ind = 150
fig_ind = fig_ind+1

if True:
    for (i, psi) in enumerate(time_psi):
        file_index = "%05d" % (i + initial_file_ind)
        cur_t = t[i]

        if False:
            pyplot.figure(fig_ind)
            pyplot.plot(x, numpy.real(psi))
            pyplot.plot(x, numpy.imag(psi))
            pyplot.xlabel("x")
            pyplot.ylabel("psi")
            pyplot.title("psi at i:  {}  time:  {}".format(i, cur_t))

            filename = os.path.join(animation_dir, "psi{}.png".format(file_index))
            pyplot.savefig(filename)
            pyplot.close(fig_ind)

            pyplot.figure(fig_ind)
            pyplot.plot(x, numpy.real(time_prob_dens[i]))
            pyplot.xlabel("x")
            pyplot.ylabel("prob_dens")
            pyplot.title("prob_dens at i:  {}  time:  {}".format(i, cur_t))

            filename = os.path.join(animation_dir, "prob_dens{}.png".format(file_index))
            pyplot.savefig(filename)
            pyplot.close(fig_ind)

        pyplot.figure(fig_ind)
        fig, ax1 = pyplot.subplots()
        pd_line = ax1.plot(x, numpy.real(time_prob_dens[i]), label="prob_dens")
        ax1.set_xlabel("x")
        ax1.set_ylabel("prob_dens")
        ax1.set_ylim(-0.001, 0.0375)

        pyplot.title("prob_dens and psi at index i:  {}  time:  {}".format(i, cur_t))
        ax2 = ax1.twinx()
        rp_line = ax2.plot(x, numpy.real(psi), "purple", label="real(psi)", lw=0.5)
        ip_line = ax2.plot(x, numpy.imag(psi), "orange", label="imag(psi)", lw=0.5)
        ax2.set_ylim(-0.21, 0.21)
        ax2.set_ylabel("wavefunction psi")

        h, l = ax1.get_legend_handles_labels()
        all_h = list(h)
        all_l = list(l)
        h, l = ax2.get_legend_handles_labels()
        all_h.extend(h)
        all_l.extend(l)
        pyplot.legend(handles = all_h)
        fig.tight_layout()

        filename = os.path.join(animation_dir, "combined{}.png".format(file_index))
        pyplot.savefig(filename)
        pyplot.close(fig_ind)

        if i%10 == 0:
            print "animation figures progress i:  {}".format(i)



for i in [0, len(time_psi)-1]:
    psi = time_psi[i]
    cur_t = t[i]
    tpd = numpy.real(time_prob_dens[i])
    max_ind = numpy.argmax(tpd)
    max_val = tpd[max_ind]
    half_max = max_val / 2.0
    left_half_max_x = numpy.interp(half_max, tpd[:max_ind], x[:max_ind])
    right_half_max_x = numpy.interp(half_max, tpd[-1:max_ind:-1], x[-1:max_ind:-1])

    pyplot.figure(fig_ind)
    fig, ax1 = pyplot.subplots()
    pd_line = ax1.plot(x, tpd, label="prob_dens")
    ax1.set_xlabel("x")
    ax1.set_ylabel("prob_dens")
    ax1.set_ylim(-0.001, 0.0375)
    ax1.plot([left_half_max_x, left_half_max_x], [half_max, max_val*1.05])
    ax1.plot([right_half_max_x, right_half_max_x], [half_max, max_val*1.05])

    pyplot.title("prob_dens at index i:  {}  time:  {}".format(i, cur_t))

    ax2 = ax1.twinx()
    rp_line = ax2.plot(x, numpy.real(psi), "purple", label="real(psi)", lw=0.25)
    ip_line = ax2.plot(x, numpy.imag(psi), "orange", label="imag(psi)", lw=0.25)
    ax2.set_ylim(-0.21, 0.21)
    ax2.set_ylabel("wavefunction psi")

    h, l = ax1.get_legend_handles_labels()
    all_h = list(h)
    all_l = list(l)
    h, l = ax2.get_legend_handles_labels()
    all_h.extend(h)
    all_l.extend(l)
    pyplot.legend(handles = all_h)
    pyplot.text(15, 0.175, "initial width:\n{}".format("%.2f"%(right_half_max_x-left_half_max_x)))
    fig.tight_layout()

    file_int = 0 if i == 0 else i+1+initial_file_ind
    file_index = "%05d" % file_int
    source_filename = "combined{}.png".format(file_index)
    pyplot.savefig(os.path.join(animation_dir, source_filename))
    pyplot.close(fig_ind)

    for j in xrange(1, initial_file_ind):
        file_index = "%05d" % (j + file_int)
        print file_index
        filename = os.path.join(animation_dir, "combined{}.png".format(file_index))
        os.symlink(source_filename, filename)
