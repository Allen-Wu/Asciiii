"""
AsciiStyleConverter python package configuration.

"""

from setuptools import setup

setup(
    name='asciiii',
    version='0.1.0',
    packages=['asciiii'],
    include_package_data=True,
    install_requires=[
        'Flask>=0.12.2',
        'requests>=2.18.4',
        'opencv-python>=3.4.3',
        'numpy>=1.15.2',
        'scipy>=1.1.0',
        'imageio>=2.3.0',
        'pillow>=5.3.0',
        'Flask>=0.12.2',
        'sh>=1.12.14'
    ],
)
