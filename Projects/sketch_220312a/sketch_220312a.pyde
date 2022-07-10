import math

#Radiuses
r1 = 300
#Always use float number instead of int
r2 = 175.0
r3 = 5.0

#Time
t = 0

#Set of points
points = []

#Coefficient
prop = 0.8

def setup():
    size(600, 600)
    
def draw():
    global r1, r2, r3, t, points, prop
    translate(width/2, height/2)
    background(255)
    
    #Cirlce 1
    noFill()
    stroke(0)
    ellipse(0, 0, 2*r1, 2*r1)
    
    #Circle 2
    x2 = (r1 - r2) * cos(t)
    y2 = (r1 - r2) * sin(t)
    ellipse(x2, y2, 2*r2, 2*r2)
    
    #Circle 3
    x3 = x2 + (prop * (r2 - r3)) * cos(-((r1 - r2)/r2) * t)
    y3 = y2 + (prop * (r2 - r3)) * sin(-((r1 - r2)/r2) * t)
    fill(255, 0, 0)
    ellipse(x3, y3, 2*r3, 2*r3)
    
    points = [[x3,y3]] + points[:10000]
    for i, p in enumerate(points):
        if i < len(points) - 1:
            stroke(255, 0, 0)
            line(p[0], p[1], points[i+1][0], points[i+1][1])
    t += 0.5
