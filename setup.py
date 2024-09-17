from setuptools import setup, find_packages

setup(
    name='calculadora_avancada',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        # Lista de dependências, se houver
    ],
    tests_require=['unittest'],
    description='Um pacote para cálculos básicos e avançados',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/seu_usuario/calculadora_avancada',
    author='Seu Nome',
    author_email='seu_email@exemplo.com',
    license='MIT',
)
