import turtle

width = int(input())
length = int(input())

turtle.shape("turtle")  # show turtle on cursor

# 사각형 그리기
for i in range(2):
    turtle.forward( width )
    turtle.left( 90 )
    turtle.forward( length )
    turtle.left( 90 )
