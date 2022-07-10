time = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB, 90)

def draw():
    global time 
    background(90)
    translate(width/2, height/2)
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix()
        translate(200, 0)
        rotate(radians(time + 2*i*360/90))
        stroke(i, 255, 255)
        tri(100)
        popMatrix()
    time += 1

def tri(length):
    '''
        Draws an equilateral triangle
        around center of triangle
    '''
    noFill()
    triangle(0, -length,
        -length*sqrt(3)/2, length/2,
        length*sqrt(3)/2, length/2)
