from setuptools import setup

setup(
    name='asciiii',
    version='0.1.0',
    packages=['asciiii'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'sh==1.12.14',
        'opencv-python>3.0',
        'scipy==1.1.0',
        'imageio==2.3.0',
        'Pillow==5.1.0'
    ],
)
