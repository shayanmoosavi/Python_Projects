# QUANTUM HARMONIC OSCILLATOR
# shayan moosavi - 973111061


# SECTION 1 : INPUT DATA AND INITIALIZATION
#-----------------------------------------------

import numpy as np
from scipy.special import hermite
from math import factorial,sqrt
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

omega=20*2*np.pi # oscillation frequency
m=1 # mass
h_bar=1 # reduced planck's constant

x0=-3 
xf=3
t0=0
tf=10 
dx=0.01 # x stepsize
dt=0.01 # t stepsize
x=np.arange(x0,xf+dx,dx) # interval of x
V=1/2*m*(omega**2)*x**2 # potential function
t=np.arange(t0,tf+dt,dt) # interval of t

n=5 # state number
A_n=(((m*omega)/(np.pi*h_bar))**(1/4))/sqrt((2**n)*factorial(n)) #normalization constant

E_n=h_bar*omega*(n+1/2) # energy of the nth state
ksi=sqrt((m*omega)/h_bar)*x

# SECTION 2 : PLOTTING AND ANIMATING THE RESULT
#-----------------------------------------------

fig=plt.figure() # creating figure
fig.suptitle('the wave function') # setting the title

# setting the subplots
ax1=plt.subplot2grid((3,1),(0,0))
ax2=plt.subplot2grid((3,1),(1,0))
ax3=plt.subplot2grid((3,1),(2,0))

ax1.grid()
ax2.grid()
ax3.grid()

ax1.set_xlim(x0,xf)
ax1.set_ylim(-10,10)
ax2.set_xlim(x0,xf)
ax2.set_ylim(-10,10)
ax3.set_xlim(x0,xf)
ax3.set_ylim(-10,10)

ax1.set_xlabel(r'$x$')
ax1.set_ylabel(r'$\Re{(\psi)}$')
ax2.set_xlabel(r'$x$')
ax2.set_ylabel('$\Im{(\psi)}$')
ax3.set_xlabel(r'$x$')
ax3.set_ylabel(r'$|\psi|^2$')

curve1, =ax1.plot(0,0,label='Re',color='#da0b0b',linestyle='-')
curve2, =ax2.plot(0,0,label='Im',color='#4095fc',linestyle='--')
curve3, =ax3.plot(0,0,label='mod',color='#3fd312',linestyle='-.')

def anim_frame(i) :
      Psi_n_Re=A_n*np.polyval(hermite(n),ksi)*np.exp(-(ksi**2)/2)*np.cos((E_n/h_bar)*i)
      Psi_n_Im=A_n*np.polyval(hermite(n),ksi)*np.exp(-(ksi**2)/2)*np.sin((E_n/h_bar)*i)
      Psi_n_mod=Psi_n_Re**2+Psi_n_Im**2
      curve1.set_xdata(x)
      curve1.set_ydata(Psi_n_Re)
      curve2.set_xdata(x)
      curve2.set_ydata(Psi_n_Im)
      curve3.set_xdata(x)
      curve3.set_ydata(Psi_n_mod)
      return curve1, curve2, curve3

anim=FuncAnimation(
      fig,anim_frame,frames=t,interval=50
)
ax1.legend()
ax2.legend()
ax3.legend()
plt.show()


# anim.save('quantum harmonic oscillator.gif')












