from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_reuirements(file_path:str)-> List[str]:
    '''
    This Function Will Return The List Of The Requirements
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='Avinash',
    author_email='avinashdurugkar69gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')     
      
    )