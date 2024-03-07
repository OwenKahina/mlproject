
#Used for building our application as a package

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements to be used in the setup
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        
        #List comprehension to remove the '\' at the end of each item in requirements
        requirements=[req.replace("\n","") for req in requirements]
        
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements



setup(
    name='mlproject',
    version='0.0.1',
    author='Owen',
    author_email='owenlkahina@gmail.com',
    packages=find_packages(),
    #install_requires=['pandas','numpy','seaborn'] 
    install_requires=get_requirements('requirements.txt')
)