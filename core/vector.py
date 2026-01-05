import math
from collections.abc import Mapping

class Vector:
    def __init__(self, values):
        # accept dict (sparse) or list (dense); we use sparse
        if isinstance(values, Mapping):
            self.data = dict(values)
        else:
            self.data = {i: v for i, v in enumerate(values)}
            
    def __mul__(self, other):
        if not isinstance(other, Vector):
            raise ValueError("Dot product require another Vector.")
        total = 0
        for key in self.data:
            if key in other.data:
                total += self.data[key] * other.data[key]
        return total
    
    def norm(self):
        return math.sqrt(sum(v ** 2 for v in self.data.values()))
    
    def cosine_similarity(self, other):
        denom = self.norm() * other.norm()
        if denom == 0:
            return 0.0
        return (self * other) / denom