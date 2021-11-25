# Paint Area Calculator
import math

def paint_area_calculator(height, width):
    return math.ceil(height * width / 5)
    
print(paint_area_calculator(2,4))