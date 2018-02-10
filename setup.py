from setuptools import setup

packages_degiropy = ['degiropy']

if __name__ == '__main__':
    setup(name='degiropy',
          version='0.1',
          description='A python interface to interact with the degiro trading platform.',
          author='Henrique Miranda',
          author_email='miranda.henrique@gmail.com',
          packages=packages_degiropy,
          )
