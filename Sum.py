"""
Static Methods: A static method is a method 
that is defined inside a class but does not 
operate on any instance-specific data. It's 
basically a regular function that is bound to
the class instead of an instance of the class.
Static methods are often used for utility 
functions that don't depend on the state of an object.
"""


class Sum:

    @staticmethod
    
    # Define the function getSum(), which takes in a variable-length argument list called arg

    def getSum(*arg):
        sum = 0
        for i in arg:
            sum += i
        print(sum)
    

Sum.getSum(8, 5,578)
