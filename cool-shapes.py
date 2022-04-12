from turtle import*
bgcolor('blue')
speed(0)
hideturtle()
for i in range(220):
    color('red')
    circle(i)
    color('green')
    circle(i*0.8)
    right(3)
    forward(3)
done()