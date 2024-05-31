from setuptools import  find_packages, setup     

def get_requirements()-> list[str]:
    requirements_list : list[str] = []
    return  requirements_list


setup(
name ='SENSOR_FAULT_PREDICTION',
version ="0.0.1",
author ="Rohan",
author_email ='rohandeshpande1632@gmail.com',
packages = find_packages(),
install_requires = get_requirements()

)
