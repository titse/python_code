'''
Title: Rock, Paper, and Scissors 
Written by Tiffany Tse

'''

# Rock-paper-scissors-lizard-Spock template
import random

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    hand = ""
    if name == "rock": 
        hand = 0
    elif name =="Spock":
        hand = 1
    elif name =="paper":
        hand = 2
    elif name =="lizard":
        hand = 3
    elif name =="scissors":
        hand = 4
    else:
        print "You didnt play a hand"
    return hand 
        

def number_to_name(number):
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    numb_hand = ""
    if number == 0:
        numb_hand = "rock"
    elif number ==1:
        numb_hand ="Spock"
    elif number == 2:
        numb_hand = "paper"
    elif number == 3:
        numb_hand = "lizard"
    elif number == 4:
        numb_hand = "scissors"
    else:
        print "Error! You need a number"
    return numb_hand

def rpsls(player_choice): 
    
    
    # print a blank line to separate consecutive games
    print 
    # print out the message for the player's choice
    print "The player has chosen", player_choice
    # convert the player's choice to player_number using the function name_to_number()
    player_number = name_to_number(player_choice)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice = number_to_name(comp_number);
    # print out the message for computer's choice
    print "The comptuer choice is:  ", comp_choice
    # compute difference of comp_number and player_number modulo five
    difference = (comp_number - player_number) % 5
    # use if/elif/else to determine winner, print winner message
    
    #use result to tell the user if he or she won!
    result = ""
    
    if difference ==0:
        result = "Sorry it's a tie between player and computer"
    elif difference == 1 :
       result = "Computer Wins"
    elif difference == 2 :
        result = "Computer Wins"
    elif difference == 3 :
        result = "Player Wins"
    elif difference == 4:
        result = "Player Wins"
    print result        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


