#!/usr/bin/python3
"""
Rectangle that inherits from BaseGeometry 
"""
from 7-base_geometry import BaseGeometry

class Rectangle(BaseGeometry):
    """
    Inicializa un objeto Rectangle.

    Args:
        width (int): El ancho del rectángulo.
        height (int): La altura del rectángulo.

    Raises:
        TypeError: Si width o height no es un entero.
        ValueError: Si width o height no son estrictamente positivos.
    """
    def __init__(self, width, height):
        self._width = width
        self.height = height
        BaseGeometry.integer_validator(width)
        BaseGeometry.integer_validator(height)