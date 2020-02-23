#!C:\Users\Lee\AppData\Local\Programs\Python\Python38-32\python.exe
import random
import json

class Brain:
    def __init__(self, player, weights):
        self.player = player
        self.weights = weights

red_brains = []
for y in range(50):
    temp = []
    for x in range(9):
        temp.append(round(random.uniform(0,4),2))
    red_brains.append(temp)

black_brains = []
for y in range(50):
    temp = []
    for x in range(9):
        temp.append(round(random.uniform(0,4),2))
    black_brains.append(temp)

with open("red_bots.json","w") as red_bots:
    red_bots.write(json.dumps(red_brains))
    red_bots.close()

with open("black_bots.json","w") as black_bots:
    black_bots.write(json.dumps(black_brains))
    black_bots.close()

