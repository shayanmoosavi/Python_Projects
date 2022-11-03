import vpython as vpy

ball = vpy.sphere(
    pos=vpy.vector(0, 0, 0),
    color=1/256*vpy.vector(16, 178, 173),
    radius=0.5
)
ball.velocity = vpy.vector(5, 2, 0)

xwall1 = vpy.box(
    pos=vpy.vector(3, 0, 0),
    size=vpy.vector(0.3, 6, 5),
    color=1 / 256 * vpy.vector(27, 216, 14),
)
xwall2 = vpy.box(
    pos=vpy.vector(-3, 0, 0),
    size=vpy.vector(0.3, 6, 5),
    color=1 / 256 * vpy.vector(27, 216, 14),
)
ywall1 = vpy.box(
    pos=vpy.vector(0, 3, 0),
    size=vpy.vector(6, 0.3, 5),
    color=1 / 256 * vpy.vector(177, 43, 163),
)
ywall2 = vpy.box(
    pos=vpy.vector(0, -3, 0),
    size=vpy.vector(6, 0.3, 5),
    color=1 / 256 * vpy.vector(177, 43, 163),
)

vel = vpy.arrow(pos=ball.pos, axis=0.5 * ball.velocity, 
round=True, opacity=0.7, color=vpy.color.red)

t = 0
dt = 0.001

vpy.graph(xtitle='t', ytitle='position')
x=vpy.gcurve(color=xwall1.color, label='x(t)')
y=vpy.gcurve(color=ywall1.color, label='y(t)')

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
    
    x.plot(pos=(t,ball.pos.x))
    y.plot(pos=(t,ball.pos.y))
    
    ball.pos.x += ball.velocity.x * dt
    ball.pos.y += ball.velocity.y * dt
    
    vel.pos.x = ball.pos.x
    vel.axis.x = 0.3 * ball.velocity.x
    vel.pos.y = ball.pos.y
    vel.axis.y = 0.3 * ball.velocity.y
    
    t += dt
