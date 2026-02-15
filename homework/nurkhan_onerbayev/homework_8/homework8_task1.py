from random import random, randint, choice

sallary = int(input("What is your sallary? "))
bonus = choice([True, False])
rised_sallary = 0

if bonus:
    rised_sallary = int(random() * 1000)
    rised_sallary += sallary
    print(f"{sallary}, {bonus} - '${rised_sallary}'")
else:
    print(f"{sallary}, {bonus} - '${sallary}'")
