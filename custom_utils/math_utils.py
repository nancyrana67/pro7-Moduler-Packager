import math

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def kilometers_to_miles(km):
    return km * 0.621371

def calculate_cylinder_volume(radius, height):
    # Custom formula using the built-in math module constants
    return math.pi * (radius ** 2) * height