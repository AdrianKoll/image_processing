from setuptools import setup, find_packages

setup(
    name="image_processing",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0"
    ],
    author="Seu Nome",
    author_email="seu.email@example.com",
    description="Pacote de processamento de imagens com Python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)