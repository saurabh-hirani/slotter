from setuptools import setup, find_packages
setup(
  name='slotter',
  license='MIT',
  version='0.0.1',
  url='https://github.com/saurabh-hirani/slotter',
  description=('Python library to slot stuff'),
  author='Saurabh Hirani',
  author_email='saurabh.hirani@gmail.com',
  packages=find_packages(),
  install_requires=[
    'blist'
  ],
  entry_points = {}
)
