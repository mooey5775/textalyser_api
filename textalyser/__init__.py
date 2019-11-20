import os
from .base import Textalyser

__version__ = '0.1.0'
__license__ = 'MIT'
__author__ = 'Edward Li'

PACKAGE_DIR = os.path.dirname(os.path.abspath(__file__))

__all__ = [
    'Textalyser'
]
