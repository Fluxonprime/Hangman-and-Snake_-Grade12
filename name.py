import turtle
import time
c=turtle.Turtle()
def p(l,x,y,b,p) :
    s=list(l)
    print(s)
    for i in range(0,len(s)) :
        c.color(p)
        c.penup()
        c.setpos(x+((b)*i),y)
        c.pendown()
        c.write(s[i],font=("Consolas",b,"normal"))
        time.sleep(0.1)
    
                           
    
    
