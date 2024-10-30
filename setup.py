from setuptools import setup

setup(
    name='DemoPackage',
    version='0.1',
    url='https://github.com/m-lindsay/DS5100-m09',
    author='m-lindsay',
    author_email='',
    description='Demo package for module 09',
    packages=['demo']  
    install_requires=['numpy >= 1.11.1', 'matplotlib >= 1.5.1']
)