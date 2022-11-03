# DAMPED OSCILLATOR

import vpython as vpy 

wall = vpy.box(
      pos=vpy.vector(-0.1, 0, 0), 
      size=vpy.vector(0.2, 3, 3),
      color=vpy.color.blue
) # creating wall

spring = vpy.helix(
      pos=vpy.vector(0, 0, 0),
      axis=vpy.vector(4.75, 0, 0),
      color=1/256*vpy.vector(158, 158, 158),
      coils=8, radius=0.5, thickness=0.05, 
      stiffness=100
) # creating spring

ball = vpy.sphere(
      pos=spring.pos+spring.axis,
      color=vpy.color.red,
      radius=0.4, mass=2,
      velocity=vpy.vector(0,0,0)
) # creating ball

x0 = vpy.vector(3,0,0) # equilibrium position
t = 0 # initial time
dt = 0.001 # timestep
c = 0.7

vpy.graph(xtitle='t',ytitle='x(t)')
X = vpy.gcurve(color=ball.color, label='x')

while t < 10 :
      vpy.rate(1000)
      X.plot(pos=(t,ball.pos.x))
      x = ball.pos - x0 # distance from equilibrium position
      ball.force =- spring.stiffness * x - c * ball.velocity
      ball.velocity += ball.force / ball.mass * dt
      ball.pos += ball.velocity * dt
      spring.axis = ball.pos - spring.pos
      t += dt



