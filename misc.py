import numpy as np

class Resources:
    def __init__(self, wood, clay, iron, crop):
        self.vector = np.array([wood, clay, iron, crop])
    
    def __add__(self, other):
        
        if type(other) == Resources:
            new_resources = self.vector + other.vector
        
        else:
            new_resources = self.vector + np.array(other)
            
        return Resources(*new_resources)
    
    def __sub__(self, other):
        
        if type(other) == Resources:
            new_resources = self.vector - other.vector
        
        else:
            new_resources = self.vector - np.array(other)
            
        return Resources(*new_resources)
        
    def __str__(self):
        return '|{0}|{1}|{2}|{3}|'.format(*self.vector)
    
    def __repr__(self):
        return self.__str__()
