import numpy as np

RESOURCE_NAMES = ["lumber", "clay", "iron", "crop"]

class Resources:

    def __init__(self, lumber, clay, iron, crop):
        self.vector = np.array([lumber, clay, iron, crop])

    def __getitem__(self, key):
        return self.vector[RESOURCE_NAMES.index(key)]

    def min(self):
        best_index = np.where(self.vector == np.amin(self.vector))[0][0]
        return RESOURCE_NAMES[best_index]

    def max(self):
        best_index = np.where(self.vector == np.amax(self.vector))[0][0]
        return RESOURCE_NAMES[best_index]

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
    
    def __mul__(self, other):
        if type(other) == Resources:
            new_resources = self.vector * other.vector

        else:
            new_resources = self.vector * np.array(other)
            
        return Resources(*new_resources)
    
    def __truediv__(self, other):
        if type(other) == Resources:
            new_resources = self.vector / other.vector

        else:
            new_resources = self.vector / np.array(other)
            
        return Resources(*new_resources)
        
    def __str__(self):
        return '|{0}|{1}|{2}|{3}|'.format(*self.vector)
    
    def __repr__(self):
        return self.__str__()
