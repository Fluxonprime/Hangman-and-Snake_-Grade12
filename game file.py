import name
import turtle
window=turtle.Screen()
window.bgcolor("blue")
name.p("Snake 2.0",-300,200,50,"yellow")
name.p("done by",-300,150,35,"yellow")
name.p("R.Sakthi vignesh",-200,100,30,"white")
name.p("S.Mohan",-200,65,30,"white")
name.p("R.Harshavardhan",-200,30,30,"white")
name.p("B.Preethi",-200,-5,30,"white")
name.p("students of XII A10",-200,-40,30,"white")
name.p("press s to play snake xenzia",-200,-95,20,"white")
name.p("press h to play hangman",-200,-115,20,"white")
name.p("press x to exit",-200,-135,20,"white")
def x():
    turtle.bye()
def s():
    turtle.bye()
    import final
def h():
    turtle.bye()
    import hangman
turtle.listen()
turtle.onkey(x,"x")
turtle.onkey(s,"s")
turtle.onkey(h,"h")
    
    


