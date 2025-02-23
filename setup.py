from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_Requirements(file_path):
    requiremants=[]
    with open(file_path, mode='r') as f:
        for line in f:
            requiremants.append(line.strip())
        
    if HYPEN_E_DOT in requiremants:
        requiremants.remove(HYPEN_E_DOT)
    return requiremants


setup(
name='myproject',
version='1.0',
author="sush",
author_email="sbmutnale512@gmail.com",
packages=find_packages(),
install_requires=get_Requirements("requirment.txt")
)
    