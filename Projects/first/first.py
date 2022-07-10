NUMBER = 36

def setup():
    size(600, 600)
    
def draw():
    translate(width/2,height/2)
    for _ in range(NUMBER):
        ellipse(200, 0, 50, 50)
        rotate(radians(360/NUMBER))
