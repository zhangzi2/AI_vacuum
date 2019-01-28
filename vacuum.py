import random
import numpy as np

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

class Environment(object):
    def __init__(self,k):
        # instantiate locations and conditions
        # 0 indicates Clean and 1 indicates Dirty
        self.locationCondition = np.zeros((10,10))
        # randomize conditions in locations A and B
        random.seed(k)
        for i in range(len(self.locationCondition[:, 1])):
            for j in range(len(self.locationCondition[1, :])):
                self.locationCondition[i, j] = random.randint(1, 1)
        #print self.locationCondition
class ReflexAgent(Environment):
    def __init__(self, Environment, iter):
        # starting location and orientation: lower left of room facing north
        self.ratio = 0.0
        self.orientation = 'N'
        self.wall = 0
        self.location = [9, 0]
        # moves the vacuum forward one step by incrementing/decrementing location indices
        def move_forward(self):
            if self.orientation == 'N' :
                if self.location[0] - 1 < 0:
                    self.location[0] = self.location[0]
                self.location[0] -= 1
            elif self.orientation == 'E' :
                if self.location[1] + 1 > 9:
                    self.location[1] = self.location[1]
                self.location[1] += 1
            elif self.orientation == 'W' :
                if self.location[1] - 1 < 0:
                    self.location[1] = self.location[1]
                self.location[1] -= 1
            else :
                if self.location[0] + 1 > 9:
                    self.location[0] = self.location[1]
                self.location[0] += 1
        # turns the vacuum right by changing its orientation
        def turn_right(self):
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'W':
                self.orientation = 'N'
            else:
                self.orientation = 'W'
        # turns the vacuum left by changing its orientation
        def turn_left(self):
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'W':
                self.orientation = 'S'
            else:
                self.orientation = 'E'
        # checks to see if vacuum is at wall
        def wall_sensor(self):
            if self.orientation == 'N':
                if self.location[0] - 1 < 0:
                    self.wall = 1
                else:
                    self.wall = 0
            elif self.orientation == 'E':
                if self.location[1] + 1 > 9:
                    self.wall = 1
                else:
                    self.wall = 0
            elif self.orientation == 'W':
                if self.location[1] - 1 < 0:
                    self.wall = 1
                else:
                    self.wall = 0
            else:
                if self.location[0] + 1 > 9:
                    self.wall = 1
                else:
                    self.wall = 0

        for i in range(iter):
            if Environment.locationCondition[self.location[0],self.location[1]] == 0:
                #print "the tile is clean"
                wall_sensor(self)
                if self.wall == 0:
                    #print "there is no wall ahead"
                    move_forward(self)
                else:
                    #print "there is a wall ahead"
                    turn_right(self)
                    move_forward(self)
            elif Environment.locationCondition[self.location[0],self.location[1]] == 1:
                #print "the tile is dirty"
                Environment.locationCondition[self.location[0], self.location[1]] = 0  # succ
                #print "the tile has been cleaned"
                wall_sensor(self)
                if self.wall == 0:
                    #print "there is no wall ahead"
                    move_forward(self)
                else:
                    #print "there is a wall ahead"
                    turn_right(self)
                    move_forward(self)

            #if self.location == [9,0]:
            #    print "back at starting location, done vacuuming"
            #    break
            #print "location:", self.location,',', "orientation:", self.orientation
        self.ratio = 100.0*(np.size(Environment.locationCondition)-np.sum(Environment.locationCondition))/np.size(Environment.locationCondition)
        #print Environment.locationCondition
        print "reflex agent:", self.ratio, "% cleaned in", iter, "iterations"


class RandomReflexAgent(Environment):
    def __init__(self, Environment, iter):
        # starting location and orientation: lower left of room facing north
        self.ration = 0.0
        self.orientation = 'N'
        self.wall = 0
        self.location = [9, 0]

        # moves the vacuum forward one step by incrementing/decrementing location indices
        def move_forward(self):
            if self.orientation == 'N':
                if self.location[0] - 1 < 0:
                    self.location[0] = self.location[0];
                else:
                    self.location[0] -= 1
            elif self.orientation == 'E':
                if self.location[1] + 1 > 9:
                    self.location[0] = self.location[1];
                else:
                    self.location[1] += 1
            elif self.orientation == 'W':
                if self.location[1] - 1 < 0:
                    self.location[0] = self.location[1];
                else:
                    self.location[1] -= 1
            else:
                if self.location[0] + 1 > 9:
                    self.location[0] = self.location[0];
                else:
                    self.location[0] += 1

        # turns the vacuum right by changing its orientation
        def turn_right(self):
            if self.orientation == 'N':
                self.orientation = 'E'
            elif self.orientation == 'E':
                self.orientation = 'S'
            elif self.orientation == 'W':
                self.orientation = 'N'
            else:
                self.orientation = 'W'

        # turns the vacuum left by changing its orientation
        def turn_left(self):
            if self.orientation == 'N':
                self.orientation = 'W'
            elif self.orientation == 'E':
                self.orientation = 'N'
            elif self.orientation == 'W':
                self.orientation = 'S'
            else:
                self.orientation = 'E'

        # checks to see if vacuum is at wall
        def wall_sensor(self):
            if self.orientation == 'N':
                if self.location[0] - 1 < 0:
                    self.wall = 1
                else:
                    self.wall = 0
            elif self.orientation == 'E':
                if self.location[1] + 1 > 9:
                    self.wall = 1
                else:
                    self.wall = 0
            elif self.orientation == 'W':
                if self.location[1] - 1 < 0:
                    self.wall = 1
                else:
                    self.wall = 0
            else:
                if self.location[0] + 1 > 9:
                    self.wall = 1
                else:
                    self.wall = 0

        for i in range(iter):
            if Environment.locationCondition[self.location[0],self.location[1]] == 0:
                #print "the tile is clean"
                wall_sensor(self)
                if self.wall == 0:
                    #print "there is no wall ahead"
                    x = random.randint(0, 1)
                    if x == 0:
                        turn_right(self)
                    else:
                        turn_left(self)
                    move_forward(self)
                else:
                    #print "there is a wall ahead"
                    x = random.randint(0,1)
                    if x == 0:
                        turn_right(self)
                    else:
                        turn_left(self)
                    move_forward(self)
            elif Environment.locationCondition[self.location[0],self.location[1]] == 1:
                #print "the tile is dirty"
                Environment.locationCondition[self.location[0], self.location[1]] = 0  # succ
                #print "the tile has been cleaned"
                wall_sensor(self)
                if self.wall == 0:
                    #print "there is no wall ahead"
                    x = random.randint(0, 1)
                    if x == 0:
                        turn_right(self)
                    else:
                        turn_left(self)
                    move_forward(self)
                else:
                    #print "there is a wall ahead"
                    x = random.randint(0, 1)
                    if x == 0:
                        turn_right(self)
                    else:
                        turn_left(self)
                    move_forward(self)

            #if self.location == [9,0]:
                #print "back at starting location, done vacuuming"
                #break

            #print "location:", self.location,',', "orientation:", self.orientation
        self.ratio = 100.0*(np.size(Environment.locationCondition)-np.sum(Environment.locationCondition))/np.size(Environment.locationCondition)
        #print Environment.locationCondition
        print "random agent:", self.ratio, "% cleaned in",iter,  "iterations"

maxit = 100
x = np.arange(0,100)
r = np.zeros(maxit)
for k in range(maxit):
    theEnvironment = Environment(k) #randomly generate environment with seed k
    theVacuum = ReflexAgent(theEnvironment, k) #run reflex agent for k iterations
    #randomVacuum = RandomReflexAgent(theEnvironment, k) #run random agent for k iterations
    r[k] = theVacuum.ratio
np.savetxt("r.csv", r, delimiter=",")



