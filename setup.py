from setuptools import find_packages,setup
from typing import List
Hypen="-e ."

def requirements(file_path:str)->List[str]:
    """

    The Function returns the requirements

    """
    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]


        if Hypen  in requirements:
            requirements.remove(Hypen)

    return requirements

setup(
name="weather",
version="0.0.1",
author="maneesh",
author_email="maneesh6301@gmail.com",
packages=find_packages(),
install_requires=requirements("requirements.txt")

)