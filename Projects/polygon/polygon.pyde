def setup():
    size(600, 600)
    
def draw():
    translate(width/2, height/2)
    polygon(5, 200)
    
def polygon(sides, sz):
    '''
    Draws a polygon given the number
    of sides and length from the center
    '''
    beginShape()
    step = radians(360/sides)
    for i in range(sides):
        vertex(sz*cos(step*i), sz*sin(step*i))
    endShape(CLOSE)
