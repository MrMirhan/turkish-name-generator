import __init__ as trn

randomName = trn.randomName() # If you won't send any arguments there will no gender selection. Default is 0.
print("Random Name:", randomName)
randomWomanName = trn.randomName(2)
print("Random Woman Name:", randomWomanName)
randomManName = trn.randomName(1)
print("Random Man Name:", randomManName)

randomFirstName = trn.firstName() # If you won't send any arguments there will no gender selection. Default is 0.
print("Random Firstname:", randomFirstName)
randomWomanFirstName = trn.firstName(2)
print("Random Woman Firstname:", randomWomanFirstName)
randomManFirstName = trn.firstName(1)
print("Random Man Firstname:", randomManFirstName)

randomLastName = trn.lastName() # There is no gender selection here.
print("Random Lastname:", randomLastName)