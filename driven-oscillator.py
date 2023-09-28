# DRIVEN OSCILLLATOR
# shayan moosavi - 97311061 ; 00/2/22

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint


# setting up the problem
def driven(y, t, gamma, omega_0, F0, omega):
    # x''+(gamma)x'+(omega_0)^2x=cos((omega)t)
    x, v = y
    dxdt = v
    dvdt = F0 * np.cos(omega * t) - 2 * gamma * v - omega_0 ** 2 * x
    dydt = [dxdt, dvdt]
    return dydt


# input data
t0 = 0  # initial time
tf = 5  # final time
y0 = (1, 0)  # initial conditions
t_interval = np.arange(t0, tf, 0.01)  # time interval
gamma = [0.0, 0.2, 0.3, 0.5, 0.7, 1.0]  # a list of damping coefficients
omega_0 = 5  # natural frequency
F0 = 6  # driving amplitude
omega_r = np.zeros(len(gamma), dtype='float64')

with np.errstate(divide='ignore', invalid='ignore'):  # ignoring these warnings
    for i in range(len(gamma)):
        omega_r[i] = (np.sqrt(omega_0 ** 2 - (2 * gamma[i] ** 2)))  # resonant frequency
    labels = ['0.0', '0.2', '0.3', '0.5', '0.7', '1.0']  # labels to put on legend


    def A(omega, gamma):  # amplitude as a function of frequency
        return F0 / np.sqrt((omega_0 ** 2 - omega ** 2) ** 2 + (2 * gamma * omega) ** 2)


    # plotting the result
    omega = np.arange(0, 10, 0.1)  # frequency interval
    fig = plt.figure()  # creating figure
    fig.suptitle('Resonance')  # figure title
    ax1 = plt.subplot2grid((1, 2), (0, 0))
    ax2 = plt.subplot2grid((1, 2), (0, 1))
    ax1.plot([], [])  # empty plot
    ax2.plot([], [])

    ax1.grid()
    ax2.grid()
    ax1.set_xlabel('t')
    ax2.set_xlabel(r'$\omega$')
    ax1.set_ylabel('x(t)')
    ax2.set_ylabel(r'$A(\omega)$')
    ax1.set_title("position vs time")
    ax2.set_title("amplitude vs frequency")
    ax1.tick_params(top=True, labeltop=False, right=True, labelright=False, direction='in')
    ax2.yaxis.set_label_position('right')
    ax2.yaxis.tick_right()
    ax2.tick_params(top=True, labeltop=False, left=True, labelleft=False, direction='in')

    for i in range(len(gamma)):
        sol = odeint(driven, y0, t_interval, args=(gamma[i], omega_0, F0, omega_r[i]))
        ax1.plot(t_interval, sol[:, 0], label=r'$\gamma=$' + labels[i])
        ax2.plot(omega, A(omega, gamma[i]), label=r'$\gamma=$' + labels[i])

plt.tight_layout(w_pad=9)
plt.legend(title='Dampening Factor', title_fontsize='small',
           bbox_to_anchor=(0, 0.5),
           loc='center right', fontsize=8)
plt.show()
