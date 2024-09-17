from setuptools import setup, find_packages

setup(
    name='calculadora_avancada',
    version='0.0.0.1',
    packages=find_packages(),
    tests_require=['unittest'],
    description='Um pacote para cálculos básicos e avançados',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/Vajean1/calculadora-avancada-package',
    author='Vajean1',
    author_email='bkrt53301@gmail.com',
)
