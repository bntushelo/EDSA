from setuptools import setup, find_packages

setup(
    name='functions',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA analyze functions',
    long_description=open('README.md').read(),
    install_requires=['numpy', "pandas"],
    url='https://github.com/<username>/<package-name>',
    author='Jonre Pienaar',
    author_email='jonrepienaarcs@gmail.com'
)