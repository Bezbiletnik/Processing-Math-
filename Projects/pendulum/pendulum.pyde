def setup():
    global p
    size(1000, 950)
    p = Pendulum(PVector(width/2, 500), 300)
    
    
def draw():
    background(255)
    p.go()
    
def mousePressed():
    p.clicked(mouseX, mouseY)
    
def mouseReleased():
    p.stopDragging()
    

class Pendulum(object):
    
    def __init__(self, origin, r):
        self.origin = origin.get()
        position = PVector()
        L = r
        angle = PI/2
        aVelocity = 0.0
        aAcceleration = 0.0
        damping = 0.995
        ballr = 100
        
    def go(self):
        update()
        drag()
        display()
        
    def update(self):
        if !dragging:
            gravity = 0.05
            aAcceleration = sqrt((gravity/L)) * cos(angle)
            aVelocity += aAcceleration
            aVelocity *= damping
            angle += aVelocity
            
    def display(self):
        position.set(L*cos(angle), L*sin(angle), 0)
        position.add(origin)
        
        stroke(0)
        strokeWeight(5)
        
        line(origin.x, origin.y, position.x, position.y)
        ellipseMode(CENTER)
        ellipse(position.x, position.y, 2*ballr, 2*ballr)
        
    def clicked(self, mx, my):
        d = dist(mx, my, position.x, position.y)
        if d < ballr:
            dragging = True
            
    def stopDragging(self):
        if dragging:
            aVelocity = 0
            dragging = False
            
    def drag(self):
        if dragging:
            diff = PVector.sub(origin, PVector(mouseX, mouseY))
            angle = atan2(-1*diff.x, diff.y) - radians(90)
