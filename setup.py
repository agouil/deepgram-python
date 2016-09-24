from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='deepgram',
      version='0.1',
      description='A python wrapper for the Deepgram API',
      author='agouil',
      author_email='andreas.williams12@gmail.com',
      url='https://github.com/agouil/deepgram-python',
      packages=['deepgram'],
      install_requires=required)
