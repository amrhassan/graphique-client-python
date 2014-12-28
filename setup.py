
from setuptools import setup, find_packages

setup(name='graphique-client',
      version='1.0',
      description='A Python client to Graphique',
      author='Amr Hassan',
      author_email='amr.hassan@gmail.com',
      url='https://github.com/amrhassan/graphique-client-python',
      license='MIT',
      packages=find_packages(),
      install_requires=['requests>=2.5.0'],
      )