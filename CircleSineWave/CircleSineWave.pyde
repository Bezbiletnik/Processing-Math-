r1 = 100
r2 = 10
t = 0
circleList = []

def setup():
    size(600, 600)

def draw():
    global t, circleList
    background(0)
    translate(width/4, height/2)
    noFill()
    stroke(255)
    ellipse(0, 0, 2*r1, 2*r1)
    
    x = r1 * cos(t)
    y = r1 * sin(t)
    circleList = [y] + circleList[:249]
    fill(255, 0, 0)
    ellipse(x, y, r2, r2)
    stroke(0, 255, 0)
    line(x, y, 200, y)
    fill(0 , 255, 0)
    ellipse(200, y, r2, r2)
    for i, c in enumerate(circleList):
        ellipse(200+i, c, 5, 5)j
    t += 0.05
    
