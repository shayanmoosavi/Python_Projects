import vpython as vpy

# creating a ball
ball = vpy.sphere(
    pos=vpy.vector(0, 0, 0),
    color=1/256*vpy.vector(16, 178, 173),
    radius=0.5
)
ball.velocity = vpy.vector(5, 3, 4) # initial velocity

# creating walls
xwall1 = vpy.box(
    pos=vpy.vector(3, 0, 0),
    size=vpy.vector(0.3, 6, 6),
    color=1 / 256 * vpy.vector(27, 216, 14),
    opacity=0.4
)
xwall2 = vpy.box(
    pos=vpy.vector(-3, 0, 0),
    size=vpy.vector(0.3, 6, 6),
    color=1 / 256 * vpy.vector(27, 216, 14),
    opacity=0.4
)
ywall1 = vpy.box(
    pos=vpy.vector(0, 3, 0),
    size=vpy.vector(6, 0.3, 6),
    color=1 / 256 * vpy.vector(177, 43, 163),
    opacity=0.4
)
ywall2 = vpy.box(
    pos=vpy.vector(0, -3, 0),
    size=vpy.vector(6, 0.3, 6),
    color=1 / 256 * vpy.vector(177, 43, 163),
    opacity=0.4
)
zwall1 = vpy.box(
    pos=vpy.vector(0, 0, 3),
    size=vpy.vector(6, 6, 0.3),
    color=1 / 256 * vpy.vector(244, 126, 16),
    opacity=0.4
)
zwall2 = vpy.box(
    pos=vpy.vector(0, 0, -3),
    size=vpy.vector(6, 6, 0.3),
    color=1 / 256 * vpy.vector(244, 126, 16),
    opacity=0.4
)

vel = vpy.arrow(pos=ball.pos, axis=0.3 * ball.velocity, 
round=True, opacity=0.7, color=vpy.color.red) # creating a velocity vector attached to the ball

t = 0 # initial time
dt = 0.001 # timestep

vpy.graph(xtitle='t', ytitle='position')
x=vpy.gcurve(color=xwall1.color, label='x(t)')
y=vpy.gcurve(color=ywall1.color, label='y(t)')
z=vpy.gcurve(color=zwall1.color, label='z(t)')

while t < 15:
    vpy.rate(1000)
    if (
        ball.pos.x + ball.radius >= xwall1.pos.x - xwall1.size.x / 2
        or ball.pos.x - ball.radius <= xwall2.pos.x + xwall2.size.x / 2
    ):
        ball.velocity.x = -ball.velocity.x
    if (
        ball.pos.y + ball.radius >= ywall1.pos.y - ywall1.size.y / 2
        or ball.pos.y - ball.radius <= ywall2.pos.y + ywall2.size.y / 2
    ):
        ball.velocity.y = -ball.velocity.y
    if (
        ball.pos.z + ball.radius >= zwall1.pos.z - zwall1.size.z / 2
        or ball.pos.z - ball.radius <= zwall2.pos.z + zwall2.size.z / 2
    ):
        ball.velocity.z = -ball.velocity.z
    
    x.plot(pos=(t, ball.pos.x))
    y.plot(pos=(t, ball.pos.y))
    z.plot(pos=(t, ball.pos.z))

    ball.pos.x += ball.velocity.x * dt
    ball.pos.y += ball.velocity.y * dt
    ball.pos.z += ball.velocity.z * dt

    vel.pos.x = ball.pos.x
    vel.axis.x = 0.3 * ball.velocity.x
    vel.pos.y = ball.pos.y
    vel.axis.y = 0.3 * ball.velocity.y
    vel.pos.z = ball.pos.z
    vel.axis.z = 0.3 * ball.velocity.z
    
    t += dt
