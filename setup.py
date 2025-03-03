from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj.readlines()]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

setup(
name='Medicine Recommendation System',
version='0.0.1',
author='Kaushal Prajapati',
author_email='prajapatikaushal279@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)