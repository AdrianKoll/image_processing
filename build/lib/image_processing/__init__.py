# image_processing/__init__.py

# Reexporta funções essenciais dos módulos internos para uma interface mais simples
from .core import load_image, convert_to_grayscale
from .filters import apply_blur, apply_sharpen

# Define os nomes que serão exportados quando for feito "from image_processing import *"
__all__ = [
    "load_image",
    "convert_to_grayscale",
    "apply_blur",
    "apply_sharpen"
]

# Metadados do pacote
__version__ = "0.1"
__author__ = "Seu Nome"