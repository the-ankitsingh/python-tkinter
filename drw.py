import turtle

sc=turtle.Screen()
cb = turtle.Turtle()

def draw () :
    for i in range(4) :
        cb.forward(30)
        cb.left(90)

    cb.forward(30)

if _name_== "_main_":

    sc.setup(400,600)
    cb.speed(100)

    for i in range(8) :
        cb.up()
        cb.setpos(-100,30 * i)
        cb.down()

        for j in range(6):
            if(i+j) % 2 ==0 :
                col ='black'
        else:
            col='white'
            cb.fillcolor(c00l)
