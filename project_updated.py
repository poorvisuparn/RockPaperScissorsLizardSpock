#importing required libraries:
from tkinter import *
import random

rpsls=Tk() #creating a window
rpsls.title("Let's Play!") #adding a title to the window

#creating a list of tuples as (winning_choice,losing_choice) combinations:
inputs=[('Scissors','Paper'),('Paper','Rock'),('Rock','Lizard'),('Lizard','Spock'),('Spock','Scissors'),('Scissors','Lizard'),('Lizard','Paper'),('Paper','Spock'),('Spock','Rock'),('Rock','Scissors')]
choices=['Rock','Paper','Scissors','Lizard','Spock']

#displaying image in tkinter:
myimg=PhotoImage(file='pcps.png')
mylabel=Label(image=myimg,padx=20,pady=20,bg='black')
mylabel.pack(side=LEFT)

space1=Label(text='\n \n').pack(side=LEFT)
l=Label(rpsls,text='Welcome to Rock-Paper-Scissors-Lizard-Spock!\nThe rules are as follows:\n⦁Scissor cuts Paper\n⦁Paper covers Rock\n⦁Rock crushes Lizard\n⦁Lizard poisons Spock\n⦁Spock smashes Scissors\n⦁Scissors decapitate Lizard\n⦁Lizard eats Paper\n⦁Paper disproves Spock\n⦁Spock vaporises Rock\n⦁Rock crushes Scissors',fg='white',bg='black',padx=10,pady=10,font="Times")
l.pack(side=LEFT)

#function to determine the winner and display the results:
def win(player_choice,comp_choice):
        player=0;comp=0
        if player_choice==comp_choice:
                res=Label(rpsls,text=f"Computer chose:\n {comp_choice}\n You chose:\n {player_choice}\n It's a Tie!!",font="Times").pack()
                player+=1;comp+=1
        elif (player_choice,comp_choice) in inputs:
                res=Label(rpsls,text=f"Computer chose:\n {comp_choice}\n You chose:\n {player_choice}\n You Win!!",font="Times").pack()
                player+=1
        else:
                res=Label(rpsls,text=f"Computer chose:\n {comp_choice}\n You chose:\n {player_choice}\n You Lose!!",font="Times").pack()
                comp+=1
        playagain=Button(rpsls,text='Play Again!',command=play,font="Times",fg='white',bg='black').pack() 

#assigning player's choice to the variable and generating computer's choice through random:
"""def Rock():
    comp_choice=random.choice(choices)
    win('Rock',comp_choice)
def Paper():
    comp_choice=random.choice(choices)
    win('Paper',comp_choice)
def Scissors():
    comp_choice=random.choice(choices)
    win('Scissors',comp_choice)
def Lizard():
    comp_choice=random.choice(choices)
    win('Lizard',comp_choice)
def Spock():
    comp_choice=random.choice(choices)
    win('Spock',comp_choice)"""

def action(your_choice):
        comp_choice=random.choice(choices)
        win(your_choice, comp_choice)

#function to input player's choice through buttons:
def play():    
        take_a_pick=Label(rpsls,text='Take your Pick!',font="Times").pack(pady=10)
        sb1=Button(rpsls,text='Rock',command=lambda: action('Rock'),font="Times").pack()
        sb2=Button(rpsls,text='Paper',command=lambda: action('Paper'),font="Times").pack()
        sb3=Button(rpsls,text='Scissors',command=lambda: action('Scissors'),font="Times").pack()
        sb4=Button(rpsls,text='Lizard',command=lambda: action('Lizard'),font="Times").pack()
        sb5=Button(rpsls,text='Spock',command=lambda: action('Spock'),font="Times").pack()
    
PL=Button(rpsls,text="Let's Play!",command=play,fg='white',bg='black',font="Times").pack()       

rpsls.mainloop()
