from random import randint



heat = 0
time = 0

timecomp = randint(2,9)
heatcomp = randint(2,9)


while heat <= 10 and time <= 10:
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
if heat or time >= 10:
    print("the resistance has been compromised! run for your lives!")




