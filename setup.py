from setuptools import  find_packages, setup     

def get_requirements()-> List[str]:
    requirements_list : List[str] = []
    return  requirements_list


setup(
name ='SENSOR_FAULT_PREDICTION',
version ="0.0.1",
author ="Rohan",
author_email ='rohandeshpande1632@gmail.com',
packages = find_packages(),
install_requires = get_requirements()

)
