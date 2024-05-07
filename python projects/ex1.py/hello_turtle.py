import turtle


#################################################################
# FILE : hello_turtle.py
# WRITER : orin levi , orin.levi , 206440075
# EXERCISE : intro2cs2 ex1 2021
# DESCRIPTION: A simple program that draw a flower garden
# STUDENTS I DISCUSSED THE EXERCISE WITH: pnina, itamar
# NOTES: its my first program to write so i needed help from other students
#################################################################


def draw_petal():
	"""in this steps im going to draw a petal"""
	turtle.forward(30)
	turtle.right(45)
	turtle.forward(30)
	turtle.right(135)
	turtle.forward(30)
	turtle.right(45)
	turtle.forward(30)
	turtle.right(135)


def draw_flower():
	"""the following steps will draw a flower"""
	turtle.left(45)
	draw_petal()
	turtle.left(90)
	draw_petal()
	turtle.left(90)
	draw_petal()
	turtle.left(90)
	draw_petal()
	turtle.left(135)
	turtle.forward(150)


def draw_flower_and_advance():
	"""the following steps will also draw a flower but also will move the
	turtle head for drawing more flowers"""
	draw_flower()
	turtle.right(90)
	turtle.up()
	turtle.forward(150)
	turtle.right(90)
	turtle.forward(150)
	turtle.left(90)
	turtle.down()


def draw_flower_bed():
	"""the following steps will draw a garden :)"""
	turtle.up()
	turtle.forward(200)
	turtle.left(180)
	turtle.down()
	draw_flower_and_advance()
	draw_flower_and_advance()
	draw_flower_and_advance()


if __name__ == "__main__":
	draw_flower_bed()
	turtle.done()
