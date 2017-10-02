from setuptools import setup

setup(name='glycemiq_db',
      version='0.1',
      description='Data Access Layer',
      url='http://github.com/gwoody1984/glycemiq-db',
      author='Greg Woodbury',
      packages=['glycemiq_db'],
      install_requires=[
          'Flask-SQLAlchemy==2.2',
      ],
      zip_safe=False)
