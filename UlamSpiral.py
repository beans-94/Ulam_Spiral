import turtle

def isprime(n):
    if n < 2:
        return False
    for i in range(2,(n//2)+1):
        if (n % i == 0):
            return False
    return True
    


def ulam_spiral():
    t = turtle.Turtle()
    step = 1
    stepSize = 20
    numSteps = 1
    turnCounter = 0
    t.width(2)
    for i in range(200):
        t.forward(stepSize)
        if isprime(step):
            t.dot()
            print(step)
        t.speed(1000)
        if (step % numSteps == 0):
            t.left(90)
            turnCounter += 1
            if (turnCounter % 2 == 0):
                numSteps += 1
        step += 1
    turtle.done()


def ulamspiral(numOfSteps):
    step = 1
    stepCount = 1
    stepSize = 20
    turnCounter = 1
    t = turtle.Turtle()
    for i in range(numOfSteps):
        t.width(3)
        t.forward(stepSize)
        if isprime(step):
            t.dot()
        if  step % stepCount == 0:
            t.left(90)
            turnCounter += 1
            if turnCounter % 2 == 0:
                stepCount += 1
        step += 1
    turtle.done()

print(ulamspiral(200))

