import turtle

def isprime(n):
    if n < 2:
        return False
    for i in range(2,(n//2)+1):
        if (n % i == 0):
            return False
    return True
    


def ulam_spiral(numOfSteps):
    t = turtle.Turtle()
    step = 1
    stepSize = 20
    stepCount = 1
    turnCounter = 0
    t.width(2)
    for i in range(200):
        t.forward(stepSize)
        if isprime(step):
            t.dot()
            print(step)
        t.speed(1000)
        if (step % stepCount == 0):
            t.left(90)
            turnCounter += 1
            if (turnCounter % 2 == 0):
                stepCount += 1
        step += 1
    turtle.done()

print(ulam_spiral(200))

