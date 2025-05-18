# Write your own function
def add_two(num1, num2):
    out = num1 + num2
    return out

# Example of creating your own class
# Note the uppercase
class Vector:

    # Use CONSTRUCTOR to create an instance
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    # Define how it is represented
    # We can use an f-string (which we just saw)
    def __repr__(self):
        return f"Vector2D({self.v1}, {self.v2})"

    # Define a method to return the norm of a vector
    def norm(self):
        return (self.v1 ** 2.0  + self.v2 ** 2.0) ** 0.5

    # Define a method to return the normalized vector
    # Here, the vector doesn't just give you a value, but a new instance
    # of a Vector() object
    def normalize(self):
        v_norm = self.norm()
        return Vector(self.v1 / v_norm, self.v2 / v_norm)

    # Define a method to return the addition of two vectors
    def addition(self, other):
            return Vector(self.v1 + other.v1, self.v2 + other.v2)

    # Define a method to return the addition of two vectors
    # But this time, define how it interacts with the + operator
    def __add__(self, other):
            return Vector(self.v1 + other.v1, self.v2 + other.v2)
