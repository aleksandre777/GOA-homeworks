from turtle import *

# ვაშენებთ სახლს 

# Step 1 : ვხატავთ კვადრატს

speed(5) 
width(5) 
color("blue") 
begin_fill() 
forward(200) 
left(90) 

forward(200)
left(90)

forward(200) 
left(90) 

forward(200)
left(90) 

end_fill()

# კვადრატის დასრულება

# კარების დახატვა 
 
forward(70)  
color("green") 
begin_fill()
left(90) 
forward(120)
right(90) 
forward(60) 
right(90) 
forward(120)
end_fill() 

# კარის დასრულება

# სახურავის დაწყება

penup() 
goto(200, 200)
color("orange") 
begin_fill()
pendown() 

right(150) 
forward(200)
left(120) 
forward(200) 
end_fill() 

# სახურავის დასრულება

# ფანჯრების დაწყება

# პირველი ფანჯარა

penup()
goto(140, 130)
color("purple") 
begin_fill()
pendown()
right(150)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

end_fill()

# პირველი ფანჯრის დასრულება

# მეორე ფანჯარა 

penup()
goto(60, 130)
begin_fill()
pendown()
left(0)
forward(50)
right(90)
forward(50)
right(90)
forward(50)
right(90)
forward(50)

end_fill()

# მეორე ფანჯრის დასასრული 

exitonclick() 