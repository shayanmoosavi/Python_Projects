import vpython as vpy

# creating a ball
ball = vpy.sphere(
    pos=vpy.vector(0, 0, 0),
    color=vpy.vector(16 / 256, 178 / 256, 173 / 256),
    radius=0.5,
)
ball.velocity = vpy.vector(3, 0, 0)  # initial velocity

# creating walls
wall1 = vpy.box(
    pos=vpy.vector(3, 0, 0),
    size=vpy.vector(0.3, 4, 5),
    color=1 / 256 * vpy.vector(149, 52, 4),
)
wall2 = vpy.box(
    pos=vpy.vector(-3, 0, 0),
    size=vpy.vector(0.3, 4, 5),
    color=1 / 256 * vpy.vector(149, 52, 4),
)

vel = vpy.arrow(
    pos=ball.pos, axis=0.5 * ball.velocity, round=True, opacity=0.7, color=vpy.color.red
)  # creating a velocity vector attached to the ball

t = 0  # initial time
dt = 0.001  # timestep

vpy.graph(xtitle="t", ytitle="x")
x = vpy.gcurve(color=1 / 256 * vpy.vector(16, 178, 173), label="x(t)")

while t < 15:
    vpy.rate(1000)
    if (
        ball.pos.x + ball.radius >= wall1.pos.x - wall1.size.x / 2
        or ball.pos.x - ball.radius <= wall2.pos.x + wall2.size.x / 2
    ):  # condition for collision
        ball.velocity.x = -ball.velocity.x
    x.plot(pos=(t, ball.pos.x))
    ball.pos.x += ball.velocity.x * dt
    vel.pos.x = ball.pos.x
    vel.axis.x = 0.5 * ball.velocity.x
    t += dt
