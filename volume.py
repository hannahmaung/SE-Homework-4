#Program to find the volume of a cube 


def calculate(x,l):
    
    if(type(l) is int):
        if(l > 0):
            return x*x*x
        else:
            print("invalid input")
    else:
        print("invalid input")