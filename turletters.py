import turtle

def turtleLetter(letter,tur):
    if letter=="box":
        tur.setheading(0)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
        tur.right(90)
        tur.forward(40)
        tur.right(90)
        tur.forward(60)
   
elif letter == "A":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.pu()
        #fixes
        tur.right(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(35)
        #tur.right(180)
    elif letter == "B":
        tur.setheading(0)
        tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.left(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.forward(15)
        tur.left(90)
        tur.fd(20)
        #fix
        tur.pu()
        tur.left(180)
        tur.fd(35)
        
        
    elif letter == "C":
        tur.pu()
        tur.fd(20)
        tur.right(180)
        tur.pd()
        tur.circle(15,180)
        #fix
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
    elif letter == "D":
        tur.pd()
        tur.right(90)
        tur.fd(30)
        tur.left(90)
        tur.circle(15,180)
        #fix
        tur.pu()
        tur.right(180)
        tur.fd(30)
    elif letter == "E":
        tur.pd()
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        #fix
        tur.pu()
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(10)
    elif letter == "F":
        tur.pd()
        tur.fd(20)
        tur.right(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(15)
        tur.left(180)
        tur.fd(15)
        tur.left(90)
        tur.fd(15)
        #fix
        tur.pu()
        tur.left(180)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
    
    elif letter == "G":
	tur.penup()
        tur.forward(5)
        tur.right(90)
        tur.forward(5)
        tur.left(90)
        tur.pendown()
        tur.forward(30)
        tur.left(180)
        tur.forward(30)
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(30)
        tur.left(90)
        tur.forward(20)
        tur.left(90)
        tur.forward(10)
        tur.penup()
        tur.forward(10)
        tur.right(90)
        tur.forward(30)
        tur.right(90)
        tur.forward(25)	
    elif letter == "H":
	tur.right(90)
        tur.fd(30)
        tur.left(180)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(180)
        tur.fd(30)
        #fix
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.right(90)
    elif letter == "I":
	tur.fd(20)
        tur.left(180)
        tur.fd(10)
        tur.left(90)
        tur.fd(30)
        tur.left(90)
        tur.fd(10)
        tur.left(180)
        tur.fd(20)
        #fix
        tur.pu()
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
    elif letter == "J":
	    pass
    elif letter == "K":
	    pass
    elif letter == "L":
	    pass
    elif letter == "M":
	    pass
    elif letter == "N":
	    pass
    elif letter == "O":
	    pass
    elif letter == "P":
	    pass		
    elif letter == "Q":
	tur.pu()
        tur.fd(5)
        tur.right(90)
        tur.fd(30)
        tur.pd()
        tur.left(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(30)
        tur.right(180)
        tur.fd(30)
        tur.left(30)
        tur.fd(23)
        tur.right(90)
        tur.fd(5)     
    elif letter == "R":
	tur.pu()
        tur.right(90)
        tur.fd(5)
        tur.pd()
        tur.fd(30)
        tur.pu()
        tur.right(180)
        tur.fd(30)
        tur.right(90)
        tur.pd()
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
        tur.right(90)
        tur.fd(10)
        tur.left(90)
        tur.left(30)
        tur.fd(25)
        tur.pu()
        tur.left(150)
        tur.fd(35)
        tur.right(90)
        tur.fd(5)
    elif letter == "S":
	tur.fd(20)
        tur.left(180)
        tur.fd(20)
        tur.left(90)
        tur.fd(15)
        tur.left(90)
        tur.fd(20)
        tur.right(90)
        tur.fd(15)
        tur.right(90)
        tur.fd(20)
        #fix
        tur.pu()
        tur.right(90)
        tur.fd(30)
        tur.right(90)
        tur.fd(20)
    elif letter == "T":
	    pass
    elif letter == "U":
	    pass
    elif letter == "V":
	    pass
    elif letter == "W":
	    pass
    elif letter == "X":
	    pass
    elif letter == "Y":
	    pass
    elif letter == "Z":
	    pass		

        
    elif letter == "Ax":
        # code here
        tur.forward(40)
		
    else:
        #handles space, punctuation, and anything else
        tur.forward(40)
	
if __name__ == "__main__":
    window = turtle.Screen()
    tur = turtle.Turtle()
    tur.speed(1)
    #turtleLetter("box",tur)
    turtleLetter("A",tur)


    window.exitonclick()
