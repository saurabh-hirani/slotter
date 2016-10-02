from setuptools import setup, find_packages
exec(open('slotter/version.py').read())
setup(
  name='slotter',
  license='MIT',
  version=__version__,
  url='https://github.com/saurabh-hirani/slotter',
  description=('Python library to slot stuff'),
  author='Saurabh Hirani',
  author_email='saurabh.hirani@gmail.com',
  packages=find_packages(),
  install_requires=[
    'blist',
    'pytest'
  ],
  entry_points = {}
)
