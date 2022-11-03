# UNIFORM CIRCULAR MOTION

import vpython as vpy 

ball = vpy.sphere(
      pos = vpy.vector(4,0,0),
      color = vpy.color.magenta,
      radius = 0.5
) # creating a sphere

t = 0 # initial time
dt = 0.001 # timestep

while t < 10 :
      vpy.rate(1000)
      ball.pos.x = 4 * vpy.cos(3 * t)
      ball.pos.y = 4 * vpy.sin(3 * t)
      t += dt