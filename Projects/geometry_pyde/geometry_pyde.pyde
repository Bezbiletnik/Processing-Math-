NUMBER = 30
TIME = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    
def draw():
    global TIME
    background(255)
    translate(width/2,height/2)
    rotate(radians(TIME))
    for _ in range(NUMBER):
        pushMatrix()
        translate(200, 0)
        rotate(radians(TIME))
        rect(0, 0, 50, 50)
        popMatrix()
        rotate(radians(360/NUMBER))
    TIME += 1
