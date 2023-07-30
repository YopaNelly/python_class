# function to calcilate area of o cirle

def circle_area(radius):
    return 3.14*(radius**2)

# function to calculate circumference of circle

def circle_circumference(radius):
    return 2 * 3.14 * radius

# function to calculate the factorial of a number

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
