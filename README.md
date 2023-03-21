# Bubble-Shooter
Synopsis- PSDL Mini Project 2022-23

BUBBLE SHOOTER GAME


1. Problem Statement
To create a Bubble Shooter Game using the Tkinter library.

2. Keywords
●	Paddle-
 A rectangular element that initially holds the ball and from which the ball bounces off.
●	Ball-
The shooter of the game that strikes the bubbles and hence increases the score.
●	Bubble-
The 4 rows of circular bubbles that are to be popped in order to win the game.

3. Abstract
We have developed a game popularly known as BUBBLE SHOOTER. The game consists of  a paddle and a ball.To start the game, press the SpaceBar.The ball acts as a shooter to hit the bubbles that are arranged in 4 layers of different colors.Move the paddle in such a way that the ball does not drop. Player is supposed to hit the bubbles and the score increases according to the colors of the bubbles.  You will have 5 lives to play the game. If you complete the game You Win appears on the screen or else You Lose.








4. Module-wise description
Tkinter library:
GUI is created to make the BUBBLE SHOOTER GAME.
The project has 5 classes:
1.	GameObject: It has functions like get_position(), move() and delete() which are common to all objects. It returns the coordinates of the object, moves the object to the desired coordinates and deletes the object respectively.
2.	Ball: This class is made for the shooter and inherits properties from the GameObject class. The ball has attributes like speed, radius, direction, color(orange)and is circular in shape. Functions like update() and collide() are used to update the coordinates of the ball while it moves on the screen and to change the direction of the ball after collision with any of the game objects respectively.
3.	Paddle: This class also inherits GameObject and is used to perform operations on the paddle. It has the function move() which is used to move the paddle along the x-axis only, according to the offset.
4.	Bubble: This class  mainly focuses on the hits and the updation of the score after collision of the ball with the bubble.It also deletes the bubble after collision.
5.	Game: This class combines the functionality of all the elements of the game.It arranges all the bubbles one after the other,adds text wherever required, controls the key inputs given by the user and performs operations accordingly. It is also responsible for looping the game till the user wins or loses the game.

6. Technology Selected and Technology features covered

We have used the tkinter library for developing the graphics of the game.
The tkinter package (“tk interface”) is the standard Python interface to the Tcl/Tk GUI
toolkit. Both Tk and tkinter are available on most UNIX platforms , including macOS, as well as Windows Systems.
Some of the inbuilt functions used in the project, include:
●	create_oval():
Ovals, mathematically, are ellipses, including circles as a special case. The ellipse is fit into a rectangle defined by the coordinates (x0, y0) of the top left corner and the coordinates (x1, y1) of a point just outside of the bottom right corner.
The shape of the bubble and the ball hitting the bubble is decided using the create_oval functionality.



●	create_rectangle():
Similar to Create_oval() , the create_rectangle is used for designing the paddle on which the ball rests.

●	draw_text():
The draw_text() function is used to give certain fonts to the texts appearing throughout the game . The size and color of the text can also be managed using draw_text()

●	unbind():
 Tkinter provides the unbind option to undo the effect of an earlier binding. Once the binding action is completed and after a certain amount of time if we want to undo the effect, unbind can be used.
●	bind():
To bind an event, in the game the player needs to start the game by pressing the ‘space’ key. This binding of starting the game and pressing the ‘space’ key is done using bind() key.

●	label():
Tkinter Label is a widget that is used to implement display boxes where you can place text or images. The text displayed by this widget can be changed by the developer at any time you want. It is also used to perform tasks such as to underline the part of the text and span the text across multiple lines. It is important to note that a label can use only one font at a time to display text.

●	delete() :
 If we want to delete a label that is defined in a tkinter application, then we have to use the destroy() method. Once the ball hits the bubbles, the bubbles are destroyed, basically deleted from the game.
●	len():
The len() function returns the number of items in an object. When the object is a string, the len() function returns the number of characters in the string.

Interface implemented: GUI (Graphical User Interface)
IDE(used): Spyder

8. References
https://docs.python.org/3/library/tkinter.html
https://www.w3schools.com/python/
https://www.geeksforgeeks.org/python-programming-language/

