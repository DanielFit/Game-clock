from random import randint

"""This input loop is to assist running tabletop role playing games that use "clocks" as a mechanic. 
Each time a player takes an action depending on if it is significantly aggressive or meticulous it may increase the segments of a clock. 
At a random interval before the game over limit is reached a complication may be introduced. Ideally the complication would appear once and then disappear after further inputs, but I can't figure out how. 
This would better represent the flow of the game were after a certain number of segments has been filled in ie: 5 or more heat segments the guards would appear at the players location. The players would deal with the issue and then the guards would no longer present an issue even though players may add further segments to the heat clock (until the game over limit."""


heat = 0
time = 0

timecomp = randint(2,9)
heatcomp = randint(2,9)

gameover = 10

while heat <= gameover and time <= gameover:
 clock = input("enter clock time or heat \n")
 if clock == "heat":
     segment = input("enter segments \n")
     segmnum = int(segment)
     heat += segmnum
     print ("heat = ",heat, "time = ",time)
     while heat >= heatcomp:
         print("oh no! its the popo!")

 if clock == "time":
     segment = input("enter segments \n")
     segmnum = int(segment)
     time += segmnum
     print ("heat = ",heat, "time = ",time)
     while time >= timecomp:
         print("Times up!")
if heat or time >= gameover:
    print("the resistance has been compromised! run for your lives!")




