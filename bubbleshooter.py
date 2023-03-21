# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 09:53:15 2022

@author: 91986
"""
 
import tkinter as tk
from tkinter import *
from PIL import Image ,ImageTk
import random


class GameObject(object):
    def __init__(self, canvas, item):
        self.canvas = canvas
        self.item = item

    def get_position(self):
        return self.canvas.coords(self.item)

    def move(self, x, y):
        self.canvas.move(self.item,   x, y)

    def delete(self):
        self.canvas.delete(self.item)
   

class Ball(GameObject):
    def __init__(self, canvas, x, y):
        self.radius = 18    #radius of the ball
        self.direction = [1, -1]        # increase the below value to increase the speed of ball
        self.speed=10   
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                  fill='orange')
        super(Ball, self).__init__(canvas,item)

    def update(self):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] <= 0 or coords[2] >= width:    #direction of the flow of the ball
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1
        x = self.direction[0] *self.speed
        y = self.direction[1] * self.speed
        self.move(x, y)

    def collide(self, game_objects):
        coords = self.get_position()
        score_update = 0
        x = (coords[0] + coords[2 ]) * 0.5
        if len(game_objects) > 2:
            self.direction[1] *= -1
        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()
            if x > coords[2]:
                self.direction[0] = 1       #direction of x1
            elif x < coords[0]:
                self.direction[0] = -1
            self.direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Bubble):
                score_update += game_object.hit()
               
        return score_update


class Paddle(GameObject):
    def __init__(self, canvas, x, y):
        self.width = 150
        self.height = 30
       
        
        #Shape of the paddle
        item = canvas.create_rectangle(x - self.width / 2,
                                       y - self.height / 2,
                                       x + self.width / 2,
                                       y + self.height / 2,
                                       fill='black')
        super(Paddle, self).__init__(canvas, item)

    def set_ball(self, ball):
        self.ball = ball


    def move(self,offset):
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super(Paddle, self).move(offset, 0)
            #if self.ball is not None:
             #   self.ball.move(offset, 0)


class Bubble(GameObject):
    COLORS = { 1:'blue', 2: 'purple', 3: 'black',4:'powder blue'}
    #COLORS = ["PeachPuff3", "dark slate gray", "rosy brown", "light goldenrod yellow", "turquoise3", "salmon",
                 # "light steel blue", "dark khaki", "pale violet red", "orchid", "tan", "MistyRose2",
                 #"DodgerBlue4", "wheat2", "RosyBrown2", "bisque3", "DarkSeaGreen1"]
   
    def __init__(self, canvas, x, y, hits):
        
        self.radius=30
        self.hits = hits
        color = Bubble.COLORS[hits]
        #Shape of the bubbles
        item = canvas.create_oval(x-self.radius, y-self.radius,
                                  x+self.radius, y+self.radius,
                                       fill=color, tags='Bubble')
        super(Bubble, self).__init__(canvas, item)
        

    def hit(self): #updating the score according to the color the ball hits the bubble
        self.hits -= 1
        score_update = 0
        if self.hits == 2:
            score_update += 5
            self.delete()
            
        elif self.hits==1:
            score_update +=10
            self.delete()
            
        else:
            score_update += 15
            self.delete()
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item,
                                   fill=Bubble.COLORS[self.hits])
        return score_update
           
   

class Game(tk.Frame):
    def __init__(self, master):
        super(Game, self).__init__(master)
        self.lives = 5
        self.width = 1500
        self.height = 800
        self.score = 0
       
       
       
        self.canvas = tk.Canvas(self, bg="pink",
                                width=self.width,
                                height=self.height)
        #img=PhotoImage(file="final.png")
        #canvas.create_image(20,20,anchor=NW,image=img)

        self.canvas.pack()      #packing the background of the game
       
       
        self.pack()        
        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width/2, 700)
        self.items[self.paddle.item] = self.paddle
            
        for x in range(5, self.width - 5, 60):      #range of the bubbles
            #creating the four layers of the bubbles
            self.add_Bubble(x + 37.5, 65, 3)
            self.add_Bubble(x + 6, 120, 2)
            self.add_Bubble(x + 37.5, 175, 1)
            self.add_Bubble(x + 6, 230, 4)


        self.hud = None
        self.sud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind('<Left>',
                         lambda _: self.paddle.move(-10))
        self.canvas.bind('<Right>',
                         lambda _: self.paddle.move(10))

    def setup_game(self):
           self.add_ball()
           self.update_lives_text()
           self.update_score()
           self.text=self.name_text(1400, 750 ,text="Made by: \n Sanika Chavan \n Gouri Dhampalwar \n Rajasi Barapatre \n Anushka Chaudhari")
           self.text = self.draw_text(750, 500,
                                      'Press Space to start',size='30')
           
           self.canvas.bind('<space>', lambda _: self.start_game())
           

    def add_ball(self):     #when lives get reduce the ball gets placed on the paddle back
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 665  )
        self.paddle.set_ball(self.ball)         #setting the ball onto the paddle

    def add_Bubble(self, x, y, hits):       # the four layers of the bubble 
        bubble = Bubble(self.canvas, x, y, hits)
        self.items[bubble.item] = bubble

    def draw_text(self, x, y, text, size='40'):     # All the text written are called using this function
        font = ('Consolas 24 ', size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)
    def name_text(self,x,y,text,size='10'):
        
        font = ('Consolas 24 ', size)
        return self.canvas.create_text(x, y, text=text,
                                       font=font)
    def update_lives_text(self):        #when ball falls off the paddle lives reduces (calling)
        text = 'Lives: %s' % self.lives
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text, 15)
        else:
            self.canvas.itemconfig(self.hud, text=text)
           
    def update_score(self):             #score update function
        text = 'Score: %s' % self.score
        if self.sud is None:
            self.sud = self.draw_text(1450, 20, text, 15)
        else:
            self.canvas.itemconfig(self.sud, text = text)

    def start_game(self):
        self.canvas.unbind('<space>')
        self.canvas.delete(self.text)
        self.paddle.ball = None
        self.game_loop()

    def game_loop(self):
        self.check_collisions()
        num_Bubbles = len(self.canvas.find_withtag('Bubble'))       #checks the no.of bubble  left
        if num_Bubbles == 0:
            self.ball.speed = None
            self.draw_text(750, 500, 'You win :) !.')               #if none left displays you win
        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1
            if self.lives <=  0:
                self.update_lives_text()                            #if lives=0 =>> You lose
                self.draw_text(750, 500, 'You Lose! Game Over :( !')               
            else:
                self.after(1000, self.setup_game)  #after 1000 milliseconds it starts again
        else:
            self.ball.update()
            self.after(50, self.game_loop)

    def check_collisions(self):
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]
        self.score += self.ball.collide(objects)
        self.update_score()        
   



if __name__ == '__main__':
    root = tk.Tk()
    root.title('BUBBLE SHOOTER!')
    game = Game(root)
    game.mainloop()




