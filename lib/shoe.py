#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = None
        self.size = size  # Use the property setter to validate size
        self.condition = None  # Default condition is None

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = 'New'

if __name__ == "__main__":
    # Example usage
    stan_smith = Shoe("Adidas", 9)
    stan_smith.cobble()  # Output: Your shoe is as good as new!
    print(stan_smith.condition)  # Output: New
