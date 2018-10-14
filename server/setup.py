from setuptools import setup

setup(
    name='asciiii',
    version='0.1.0',
    packages=['asciiii'],
    include_package_data=True,
    install_requires=[
        'Flask==0.12.2',
        'sh==1.12.14',
    ],
)
