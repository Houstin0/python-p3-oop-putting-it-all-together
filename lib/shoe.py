#!/usr/bin/env python3

class Shoe:
    
    def __init__(self,brand,size,condition="worn"):
        self.brand=brand
        self._size=size
        self.condition=condition
        

    def get_size(self):
        return self._size  

    def set_size(self,size):
        if type(size) == int:
            self._size=size
        else:
            print("size must be an integer")

    size=property(get_size,set_size)

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition="New"


nike=Shoe("Nike","9")
nike.size=17  
nike.cobble()
print(nike.condition)
            