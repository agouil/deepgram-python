from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(name='deepgram',
      version='0.1.1',
      description='A python wrapper for the Deepgram API',
      author='agouil',
      author_email='andreas.williams12@gmail.com',
      url='https://github.com/agouil/deepgram-python',
      download_url='https://github.com/agouil/deepgram-python/tarball/0.1.1',
      packages=['deepgram'],
      keywords=['deepgram', 'audio', 'voice', 'transcription', 'api'],
      install_requires=required)
