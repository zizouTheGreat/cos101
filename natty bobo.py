


def a():
    displacement=int(input("what is the displacement:"))
    time=int(input("what is time:"))
    #velocity=displacement/time
    output=str(displacement/time)
    print(output+" m/s")

def b():
    velocity=float(input("input your velocity:"))
    #displacement=velocity*time
    time=float(input("What is the time?"))
    output=str(velocity*time)
    print(output+"m")

def c():
    length=int(input("what is length"))
    breadth=int(input("what is breadth"))
    height=int(input("what is height"))
    #volume=length*breadth*height
    output=str(length*breadth*height)
    print(output)

def d():
    mass=int(input("what is mass"))
    acceleration=int(input("what is acceleration"))
    #force=mass*acceleration
    output=str(mass*acceleration)
    print(output)

def e():
    force=int(input("what is force"))
    distance=int(input("what is distance"))
    #work done= force*distance
    output=str(force*distance)
    print(output)


def main():
    user_choice=input("choose from a-e: ")
    if user_choice=="a":
        a()
    elif user_choice=="b":
        b()
    elif user_choice=="c":
        c()
    elif user_choice=="d":
        d()
    elif user_choice=="e":
        e()
if __name__=='__main__':
        main()


